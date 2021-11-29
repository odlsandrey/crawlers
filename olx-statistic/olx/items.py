
import scrapy


class BaseOlxItem(scrapy.Item):

    name = scrapy.Field()
    title = scrapy.Field()
    id_art = scrapy.Field()
    advert_views = scrapy.Field()
    price = scrapy.Field()
    condition = scrapy.Field()
    link = scrapy.Field()







