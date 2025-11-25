# Handsome Chat 🖤💬

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) 
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.104-green.svg)](https://fastapi.tiangolo.com/)
[![WebSocket](https://img.shields.io/badge/WebSocket-Enabled-yellow.svg)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
[![Deploy Status](https://img.shields.io/badge/Render-Online-brightgreen.svg)](https://mini-chat-app-xtcw.onrender.com/)

**Handsome Chat** is a sleek, real-time web chat application built with FastAPI, WebSocket, and a responsive frontend. Chat with your friends instantly and enjoy a smooth, modern UI.

---

## 🌐 Demo & Try It Live

**Live Demo:** [Handsome Chat on Render](https://mini-chat-app-xtcw.onrender.com/)  

Click below to try it now:  

[![Try Handsome Chat](https://img.shields.io/badge/💬-Try+It+Live-blueviolet)](https://mini-chat-app-xtcw.onrender.com/)

---

## ✨ Features

- Real-time messaging via WebSocket  
- Usernames saved in browser localStorage  
- Mobile-friendly and fully responsive UI  
- Connection status indicator  
- Smooth animations and auto-scroll  
- Auto-reconnect if the connection drops  

---

## 🛠 Technology Stack

| Layer       | Technology |
|------------|------------|
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Python, FastAPI |
| Real-time  | WebSocket |
| Database   | PostgreSQL (optional) |
| Deployment | Render.com |

---

## 📷 Screenshots

![Chat Screenshot](https://via.placeholder.com/800x400.png?text=Handsome+Chat+Screenshot)  
*Screenshot of the chat interface*  

![Chat GIF](https://via.placeholder.com/800x400.gif?text=Chat+Demo+GIF)  
*GIF demo showing real-time chat interaction*

---

## 📦 Folder Structure

```

handsome-chat/
├── app/
│   ├── main.py          # FastAPI app entry
│   ├── websocket.py     # WebSocket connection handlers
│   ├── database.py      # Optional DB connection
│   └── models.py        # Optional ORM models
├── static/
│   ├── index.html       # Frontend HTML
│   └── style.css        # Optional external CSS
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md

````

---

## ⚙ How It Works

1. **Frontend**:  
   - User enters username and messages.  
   - Messages sent via WebSocket to backend.  
   - Messages displayed in real-time for all users.  

2. **Backend**:  
   - FastAPI handles WebSocket connections.  
   - Broadcasts messages to all connected clients.  
   - Optionally persists messages to PostgreSQL.  

3. **WebSocket Connection**:  
   - Connects to `wss://<your-app-url>/ws`  
   - Handles connection open, message receive, close, and error events  
   - Auto-reconnects on disconnection  

---

## 🚀 Installation & Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/handsome-chat.git
cd handsome-chat
````

### 2. Backend Setup

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

**Create `.env` file** with database or host settings:

```env
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=yourdb
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

Run the backend server:

```bash
uvicorn app.main:app --reload
```

### 3. Frontend

Open `static/index.html` in your browser or serve via any HTTP server.

Update WebSocket URL if hosted:

```js
const WS_HOST = "wss://mini-chat-app-xtcw.onrender.com/ws";
```

---

## 💬 Usage

1. Enter your username (saved automatically).
2. Type a message and click **Send** or press **Enter**.
3. Messages appear instantly for all connected users.
4. Connection status shows at the top (Connected/Disconnected).

---

## 🤝 Contributing

Contributions are welcome!

* Fork the repository
* Create a new branch (`git checkout -b feature-name`)
* Commit your changes (`git commit -m 'Add new feature'`)
* Push to the branch (`git push origin feature-name`)
* Open a Pull Request

---

## 📜 License

MIT License. Feel free to use, modify, and share.

---

Made with ❤️ by **[Your Name]**
A handsome chat app for everyone! 🎨




<!-- =============================================== -->
// To start the Mini-chat app

mini-chat\

docker-compose up --build

Frontend: http://localhost:3000
Backend: http://localhost:8000
Database: internal (PostgreSQL container)

<!-- ================================================ -->
//To build desktop app
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\electron-builder\Cache"

npm run build
