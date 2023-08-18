import { app, BrowserWindow, ipcMain } from "electron";
import path = require("path");
import { readJsonFile, searchModuleName } from "./json_loader";

let win: BrowserWindow;
let trigger_devices = readJsonFile(
  "../../data/electron_json/trigger_device_names.json"
);
let action_devices = readJsonFile(
  "../../data/electron_json/action_device_names.json"
);

const createWindow = () => {
  win = new BrowserWindow({
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

ipcMain.on("start_button_click", (event, arg) => {
  console.log("button clicked!");
  console.log(arg);
});

ipcMain.on("refresh_button_click", () => {
  win.webContents.send("load_trigger_devices", trigger_devices);
  win.webContents.send("load_action_devices", action_devices);
});

ipcMain.on("trigger_device_change", (event, arg) => {
  let module_name = searchModuleName(trigger_devices, arg);

  let nameObj = readJsonFile(
    "../../data/electron_json/trigger/" + module_name + ".json"
  );
  win.webContents.send("update-trigger-condition", nameObj);
});

ipcMain.on("action_device_change", (event, arg) => {
  let module_name = searchModuleName(action_devices, arg);

  let nameObj = readJsonFile(
    "../../data/electron_json/action/" + module_name + ".json"
  );
  win.webContents.send("update-action-action", nameObj);
});
