# scrapy_projects
可以作为 scrapy 学习项目
[TOC]
## 项目一
### 爬取[一生必须知道的50幅中国名画，每一幅你都不容错过](http://www.sohu.com/a/157709282_661623) 这篇文章中的50幅名画

1. **items创建**

```
painter = scrapy.Field()
pic_name = scrapy.Field()
picture = scrapy.Field()
```

2. **scrapy配置**
```
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
```
3. **pipelines自定义存储**
```
with open(picPath, 'wb') as fp:
    response = urlopen(item['picture'])
    fp.write(response.read())
```
4.**修改配置文件,注册自定义存储文件**
```
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'famousPicSpider.pipelines.FamouspicspiderPipeline': 300,
}
```
5、`scrapy crawl famousPic`