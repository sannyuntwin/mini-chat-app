# backend/main.py
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Set

app = FastAPI(title="MiniChat Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev; narrow this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConnectionManager:
    def __init__(self):
        self.active: Set[WebSocket] = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active.add(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active.discard(websocket)

    async def broadcast(self, message: str):
        remove = []
        for conn in list(self.active):
            try:
                await conn.send_text(message)
            except Exception:
                remove.append(conn)
        for r in remove:
            self.disconnect(r)

manager = ConnectionManager()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await manager.connect(ws)
    try:
        while True:
            text = await ws.receive_text()
            # optional: sanitize or process message here
            await manager.broadcast(text)
    except WebSocketDisconnect:
        manager.disconnect(ws)
    except Exception:
        manager.disconnect(ws)
