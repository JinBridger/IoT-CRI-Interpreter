from scrapy.crawler import CrawlerProcess
from ifttt_spider import IftttSpider
from rule_handler import RuleHandler


def run_ifttt_spider():
    process = CrawlerProcess(
        {"USER_AGENT": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"}
    )
    process.crawl(IftttSpider)
    process.start()


def load_applets_into_lists():
    with open("./data/applets.txt", "r") as file:
        applets = file.readlines()
    applets = [rule.strip() for rule in applets]
    return applets


def load_live_applets_into_lists():
    with open("./data/live_applets.txt", "r") as file:
        live_applets = file.readlines()
    live_applets = [rule.strip() for rule in live_applets]
    return live_applets


if __name__ == "__main__":
    rh = RuleHandler()
    applets = load_applets_into_lists()
    for rule in applets:
        rh.spliter(rule)
