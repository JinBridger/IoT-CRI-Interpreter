class RuleHandler:
    def spliter(self, rule: str):
        parts = rule.split("then")
        if_condition = parts[0]
        then_action = parts[1]

        print("If condition:", if_condition)
        print("Then action:", then_action)


if __name__ == "__main__":
    pass
