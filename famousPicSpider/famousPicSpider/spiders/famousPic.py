# -*- coding: utf-8 -*-
# @Author: shelling
# @Date:   2019-05-29 15:58:59
# @Last Modified by:   shelling
# @Last Modified time: 2019-05-29 15:59:35

import scrapy
from famousPicSpider.items import FamouspicspiderItem

class FamouspicSpider(scrapy.Spider):
    name = 'famousPic'
    allowed_domains = ['sohu.com']
    start_urls = ['http://www.sohu.com/a/157709282_661623']

    def parse(self, response):
        pic_list = response.xpath('//article[@class="article"]/p')
        items = []
        for pic in pic_list[2:]:
        	if len(pic.extract().split('／'))>1: 
	        	item = FamouspicspiderItem()
	        	item['painter'] = pic.xpath('span/text()')[0].extract().split('／')[1]
	        	item['pic_name'] = pic.extract().split('／')[0].split('、')[1]
	        	items.append(item)
       		if pic.xpath('img/@src').extract(): 
       			items[-1]['picture'] = pic.xpath('img/@src').extract()[0]
       		
       	return items
        	
