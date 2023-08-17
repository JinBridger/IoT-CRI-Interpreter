import { app, BrowserWindow, ipcMain } from "electron";
import path = require("path");

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "renderer.js"),
    },
  });

  win.loadFile("../assets/index.html");
  console.log("start!");
};

app.whenReady().then(() => {
  createWindow();
});

ipcMain.on("button-click", (event, arg) => {
  console.log("button clicked!");
  console.log(arg);
});
