import { ipcRenderer } from "electron";

function refreshSelect(elem: HTMLSelectElement, selectDict: object) {
  elem.innerHTML = "";

  for (let item of Object.values(selectDict)) {
    let option = document.createElement("option");
    option.value = item["module_name"];
    option.text = item["name"];
    elem.add(option);
  }
}

function getAllSelects() {
  let trigger_device = document.getElementById(
    "trigger_device"
  ) as HTMLSelectElement;
  let trigger_condition = document.getElementById(
    "trigger_condition"
  ) as HTMLSelectElement;
  let action_device = document.getElementById(
    "action_device"
  ) as HTMLSelectElement;
  let action_action = document.getElementById(
    "action_action"
  ) as HTMLSelectElement;

  let return_obj = {
    trigger_device: trigger_device.options[trigger_device.selectedIndex].text,
    trigger_condition:
      trigger_condition.options[trigger_condition.selectedIndex].text,
    action_device: action_device.options[action_device.selectedIndex].text,
    action_action: action_action.options[action_action.selectedIndex].text,
  };

  return return_obj;
}

ipcRenderer.on("update-trigger-condition", (event, arg) => {
  let trigger_condition = document.getElementById(
    "trigger_condition"
  ) as HTMLSelectElement;

  refreshSelect(trigger_condition, arg);
});

ipcRenderer.on("update-action-action", (event, arg) => {
  let action_action = document.getElementById(
    "action_action"
  ) as HTMLSelectElement;

  refreshSelect(action_action, arg);
});

ipcRenderer.on("load_trigger_devices", (event, arg) => {
  let trigger_device = document.getElementById(
    "trigger_device"
  ) as HTMLSelectElement;

  refreshSelect(trigger_device, arg);
});

ipcRenderer.on("load_action_devices", (event, arg) => {
  let action_device = document.getElementById(
    "action_device"
  ) as HTMLSelectElement;

  refreshSelect(action_device, arg);
});

window.onload = () => {
  document.getElementById("start_button")?.addEventListener("click", () => {
    ipcRenderer.send("start_button_click", getAllSelects());
  });

  document.getElementById("trigger_device")?.addEventListener("change", () => {
    let trigger_device = document.getElementById(
      "trigger_device"
    ) as HTMLSelectElement;
    let select_content =
      trigger_device.options[trigger_device.selectedIndex].text;
    ipcRenderer.send("trigger_device_change", select_content);
  });

  document.getElementById("action_device")?.addEventListener("change", () => {
    let action_device = document.getElementById(
      "action_device"
    ) as HTMLSelectElement;
    let select_content =
      action_device.options[action_device.selectedIndex].text;
    ipcRenderer.send("action_device_change", select_content);
  });

  document.getElementById("refresh_button")?.addEventListener("click", () => {
    ipcRenderer.send("refresh_button_click");
  });
};
