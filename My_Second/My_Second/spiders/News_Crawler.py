import scrapy, re
from bs4 import BeautifulSoup


class NewsCrawlerSpider(scrapy.Spider):
    name = 'ria'
    allowed_domains = ['lenta.ru']
    start_urls = ['https://lenta.ru/?ysclid=l1gb7h5b2t']

    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.body, "lxml")
        urls = soup.find_all("a")

        for url in urls:
            page_url = url.get("href")

            if page_url is not None:
                page_url = str(response.urljoin(page_url))
                yield response.follow(page_url, callback=self.page_parse)

    def page_parse(self, response):
         try:
             soup = BeautifulSoup(response.text, "lxml")
             page_text = soup.find(re.compile("Украин"))

             if page_text is not None:
                 print(soup)

         except Exception as ex:
             print(ex)