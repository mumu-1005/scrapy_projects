# -*- coding: utf-8 -*-
# @Author: shelling
# @Date:   2019-05-29 15:51:55
# @Last Modified by:   shelling
# @Last Modified time: 2019-05-29 15:57:53

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FamouspicspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    painter = scrapy.Field()
    pic_name = scrapy.Field()
    picture = scrapy.Field()

