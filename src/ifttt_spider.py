import scrapy
import json


class IftttSpider(scrapy.Spider):
    name = "ifttt.com"
    start_urls = ["https://ifttt.com/login"]
    keys_path = "./keys/keys.json"

    def __init__(self, *args, **kwargs):
        super(IftttSpider, self).__init__(*args, **kwargs)

        # load keys
        with open(self.keys_path, "r") as f:
            keys = json.load(f)
        self.username = keys["username"]
        self.email = keys["email"]
        self.password = keys["password"]
        self.authorization = keys["authorization"]

    def parse(self, response):
        # get authenticity token
        authenticity_token = response.css(
            "input[type=hidden]:nth-child(2)::attr(value)"
        ).get()

        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                "utf8": "✓",
                "authenticity_token": authenticity_token,
                "return_to": None,
                "psu_": None,
                "user[username]": self.email,
                "user[password]": self.password,
                "commit": "Log+in",
            },
            callback=self.login_check,
        )

    def login_check(self, response):
        # check if successfully logged in
        if b"The email and password don&#39;t match." in response.body:
            self.logger.error("Login failed: Wrong username or password.")
            return

        self.logger.info("Successfully login.")
        return self.get_applet()

    def get_applet(self):
        # get all rules
        data = {
            "query": """
                query UserAppletsQuery($user_login: String) {
                    live_applets {
                        applet {
                            normalized_applet {
                                name
                            }
                        }
                    }
                    applets(user_login: $user_login, include_draft: true, include_archived: false) {
                        normalized_applet {
                            name
                        }
                    }
                }
            """,
            "variables": {"user_login": self.username},
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": 'Token jwt="' + self.authorization + '"',
        }

        yield scrapy.Request(
            url="https://ifttt.com/api/v3/graph",
            method="POST",
            body=json.dumps(data),
            headers=headers,
            callback=self.handle_applet,
        )

    def handle_applet(self, response):
        # extract applets from response and sort
        data = json.loads(response.body)
        live_applets = [
            item["applet"]["normalized_applet"]["name"]
            for item in data["data"]["live_applets"]
        ]
        applets = [
            item["normalized_applet"]["name"] for item in data["data"]["applets"]
        ]
        live_applets.sort()
        applets.sort()

        # output to file
        with open("./data/live_applets.txt", "w") as f:
            for item in live_applets:
                f.write("%s\n" % str(item))

        with open("./data/applets.txt", "w") as f:
            for item in applets:
                f.write("%s\n" % str(item))
