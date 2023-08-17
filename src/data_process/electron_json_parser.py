import json
import os


class ElectronJsonParser:
    def __init__(
        self, in_trigger_folder, in_action_folder, out_trigger_folder, out_action_folder
    ) -> None:
        self.in_trigger_folder = in_trigger_folder
        self.in_action_folder = in_action_folder

        self.out_trigger_folder = out_trigger_folder
        self.out_action_folder = out_action_folder

    def run(self):
        self.handle_all(self.in_trigger_folder, self.out_trigger_folder, "trigger")
        self.handle_all(self.in_action_folder, self.out_action_folder, "action")

    def handle_all(self, input_dir, output_dir, type):
        filenames = os.listdir(input_dir)
        for filename in filenames:
            self.handle_file(filename, input_dir, output_dir, type)

    def handle_file(self, filename, input_dir, output_dir, type):
        with open(input_dir + filename) as f:
            input_json = json.load(f)
        output_json = self.parse_json(input_json, type)
        if output_json == "":
            return
        output_str = json.dumps(output_json, indent=4)
        with open(output_dir + filename, "w+") as wf:
            wf.write(output_str)

    def parse_json(self, json_dict, type):
        if type == "trigger":
            items = json_dict["data"]["channel"]["public_triggers"]
        else:
            items = json_dict["data"]["channel"]["public_actions"]
        item_names = [item["name"] for item in items]
        if item_names == []:
            return ""
        output = {"names": item_names}
        return output


if __name__ == "__main__":
    input_trigger_dir = "./data/trigger_json/"
    output_trigger_dir = "./data/electron_json/trigger/"
    input_action_dir = "./data/action_json/"
    output_action_dir = "./data/electron_json/action/"

    ejp = ElectronJsonParser(
        input_trigger_dir, input_action_dir, output_trigger_dir, output_action_dir
    )
    ejp.run()
