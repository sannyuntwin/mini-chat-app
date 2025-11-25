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
