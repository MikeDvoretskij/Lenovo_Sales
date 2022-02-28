import scrapy, re, json, pathlib

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ["shop.lenovo.ru"]
    start_urls = ['https://shop.lenovo.ru/noutbuki/a_sales/?available=yes',]

    def parse(self, response):
        name=response.xpath("//div[@class='catalog-item__title']/text()").getall()
        p=response.xpath("//div[@class='catalog-item__price']/text()").getall()
        u=response.xpath("//a[@class='catalog-item-go']/@href").getall()
        url=[]
        price=[]
        file_data="Bot/Data/data.json"
        for i in p:
            s = re.sub(' +', '', i)
            c = s.replace('\r\n', "")
            d = c.replace("\xa0", "")
            if len(d)>0:
                price.append(d)

        for i in u:
            s=f"https://shop.lenovo.ru{i}"
            url.append(s)

        with open(file_data,"w") as file:
            a=[]
            for i in range(len(url)):
                data={
                    "name":name[i],
                    "price":price[i],
                    "url":url[i]
                }

                a.append(data)
            json.dump(a, file, indent=4, ensure_ascii=False)


