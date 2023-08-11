import json


class IftttInitalizerParser:
    def __init__(self, json_file: str) -> None:
        with open(json_file, "r") as f:
            self.input_data = json.load(f)

    def parser(self, output_file: str) -> None:
        self.output_data = [
            {"module_name": item["module_name"]}
            for item in self.input_data["preloadedServices"]
        ]
        output_str = json.dumps(self.output_data, indent=4)

        with open(output_file, "w") as f:
            f.write(output_str)


if __name__ == "__main__":
    iip = IftttInitalizerParser("./data/output.json")
    iip.parser("./data/device_name.json")
