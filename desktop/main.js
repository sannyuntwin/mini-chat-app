const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js') // if you have one
    }
  });

  // Open DevTools to see errors
  mainWindow.webContents.openDevTools();

  // Load the frontend
  if (app.isPackaged) {
    // Production: load from packaged files
    mainWindow.loadFile(path.join(__dirname, '../frontend/index.html'));
  } else {
    // Development: you can use a local server or file
    mainWindow.loadFile(path.join(__dirname, '../frontend/index.html'));
  }

  // Log any loading errors
  mainWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription) => {
    console.log('Failed to load:', errorCode, errorDescription);
  });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});