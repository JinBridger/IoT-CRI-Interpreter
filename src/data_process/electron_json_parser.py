import json
import os


class ElectronJsonParser:
    def __init__(
        self,
        in_trigger_folder,
        in_action_folder,
        out_trigger_folder,
        out_action_folder,
        private_path,
    ) -> None:
        self.in_trigger_folder = in_trigger_folder
        self.in_action_folder = in_action_folder

        self.out_trigger_folder = out_trigger_folder
        self.out_action_folder = out_action_folder
        self.private_path = private_path

    def run(self):
        # self.handle_all(self.in_trigger_folder, self.out_trigger_folder, "trigger")
        # self.handle_all(self.in_action_folder, self.out_action_folder, "action")
        self.parse_private(self.private_path)

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

    def parse_private(self, private_path):
        with open(private_path) as f:
            private_json = json.load(f)

        items = private_json["data"]["me"]["private_channels"]
        for item in items:
            triggers = [
                trigger_item["name"] for trigger_item in item["public_triggers"]
            ]
            actions = [action_item["name"] for action_item in item["public_actions"]]
            name = item["name"]
            output_trigger_str = json.dumps({"names": triggers}, indent=4)
            with open(self.out_trigger_folder + name + ".json", "w+") as wf:
                wf.write(output_trigger_str)
            output_action_str = json.dumps({"names": actions}, indent=4)
            with open(self.out_action_folder + name + ".json", "w+") as wf:
                wf.write(output_action_str)


if __name__ == "__main__":
    input_trigger_dir = "./data/trigger_json/"
    output_trigger_dir = "./data/electron_json/trigger/"
    input_action_dir = "./data/action_json/"
    output_action_dir = "./data/electron_json/action/"
    private_json = "./data/private.json"

    ejp = ElectronJsonParser(
        input_trigger_dir,
        input_action_dir,
        output_trigger_dir,
        output_action_dir,
        private_json,
    )
    ejp.run()
