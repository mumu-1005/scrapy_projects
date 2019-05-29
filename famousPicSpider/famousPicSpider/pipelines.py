# -*- coding: utf-8 -*-
# @Author: shelling
# @Date:   2019-05-29 15:51:55
# @Last Modified by:   shelling
# @Last Modified time: 2019-05-29 15:54:56

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import os
import codecs
from urllib.request import urlopen

class FamouspicspiderPipeline(object):
    def process_item(self, item, spider):
    	scrpy_time = time.strftime('%Y%m%d',time.localtime())
    	filename = 'famousPic_' + scrpy_time + '.txt'
    	picDir = 'Pic'
    	
    	if os.path.isdir(picDir):
    		pass
    	else:
    		os.mkdir(picDir)

    	with codecs.open(filename, 'a', 'utf-8') as fp:
    		fp.write(item['painter'] + '\t')
    		fp.write(item['pic_name'] + '\t')
    		pic_name = item['pic_name']
    		fp.write(item['picture'] + '\n')
    		picPath = picDir + os.sep + pic_name + '.jpg'
    		
    		with open(picPath, 'wb') as fp:
    			response = urlopen(item['picture'])
    			fp.write(response.read())

    	return item
