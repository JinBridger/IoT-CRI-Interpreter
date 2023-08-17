import { ipcRenderer } from "electron";

function get_all_selects() {
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
    trigger_device: trigger_device.options[trigger_device.selectedIndex].value,
    trigger_condition:
      trigger_condition.options[trigger_condition.selectedIndex].value,
    action_device: action_device.options[action_device.selectedIndex].value,
    action_action: action_action.options[action_action.selectedIndex].value,
  };

  return return_obj;
}

window.onload = () => {
  document.getElementById("start_button")?.addEventListener("click", () => {
    ipcRenderer.send("button-click", get_all_selects());
  });
};
