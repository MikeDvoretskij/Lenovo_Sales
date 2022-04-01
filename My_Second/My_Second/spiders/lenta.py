import scrapy, re, bs4


class LentaSpider(scrapy.Spider):
    name = 'lenta'
    allowed_domains = ['lenta.ru']
    start_urls = ['https://lenta.ru/rubrics/ussr/baltics/', "https://lenta.ru/rubrics/ussr/ukraine/",
                  "https://lenta.ru/rubrics/ussr/belarus/", "https://lenta.ru/rubrics/ussr/moldova/",
                  "https://lenta.ru/rubrics/ussr/kavkaz/", "https://lenta.ru/rubrics/ussr/middle_asia/",
                  "https://lenta.ru/rubrics/world/society/", "https://lenta.ru/rubrics/world/politic/",
                  "https://lenta.ru/rubrics/world/accident/", "https://lenta.ru/rubrics/world/conflict/",
                  "https://lenta.ru/rubrics/world/crime/", ]

    def parse(self, response, **kwargs):
        soup = bs4.BeautifulSoup(response.text, "lxml")
        urls = soup.find_all("a", {"class": "card-full-news _subrubric"})

        for url in urls:
            yield response.follow("https://lenta.ru" + str(url.get("href")), callback=self.page_parse)

    def page_parse(self, response):
        soup = bs4.BeautifulSoup(response.text, "lxml")
        trigger = soup.find("p", {"class": "topic-body__content-text"}, text=re.compile("Украина"))

        if trigger is not None:
            print(response.url)