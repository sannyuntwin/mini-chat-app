from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Set
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import User, Message

app = FastAPI(title="Mini Chat Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Set[WebSocket] = set()
    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active_connections.add(ws)
    def disconnect(self, ws: WebSocket):
        self.active_connections.discard(ws)
    async def broadcast(self, msg: str):
        remove = []
        for conn in list(self.active_connections):
            try:
                await conn.send_text(msg)
            except:
                remove.append(conn)
        for r in remove:
            self.disconnect(r)

manager = ConnectionManager()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket, db: Session = Depends(get_db)):
    await manager.connect(ws)
    try:
        while True:
            data = await ws.receive_text()
            # Format: "username|message"
            if "|" in data:
                username, content = data.split("|", 1)
            else:
                username, content = "anon", data

            # Save user
            user = db.query(User).filter(User.username==username).first()
            if not user:
                user = User(username=username, nickname=username)
                db.add(user)
                db.commit()
                db.refresh(user)

            # Save message
            msg = Message(user_id=user.id, content=content)
            db.add(msg)
            db.commit()

            # Broadcast
            await manager.broadcast(f"{username}: {content}")

    except WebSocketDisconnect:
        manager.disconnect(ws)
