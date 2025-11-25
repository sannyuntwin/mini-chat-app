const { app, BrowserWindow } = require('electron')
const path = require('path')

function createWindow() {
  const win = new BrowserWindow({
    width: 900,
    height: 700,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false
    }
  })

  // For development load local frontend file.
  // When packaging, bundle frontend files and update this path as needed.
  win.loadFile(path.join(__dirname, '../frontend/index.html'))

  // win.webContents.openDevTools() // uncomment for debugging
}

app.whenReady().then(createWindow)
app.on('window-all-closed', ()=> { if(process.platform !== 'darwin') app.quit() })
