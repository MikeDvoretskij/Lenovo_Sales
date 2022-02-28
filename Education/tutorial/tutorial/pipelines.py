from itemadapter import ItemAdapter
import json

class TutorialPipeline:

    def open_spider(self, spider):
        self.file = open('items.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        a=json.dumps(ItemAdapter(item).asdict(), indent=4)
        self.file.write(a)
        return item