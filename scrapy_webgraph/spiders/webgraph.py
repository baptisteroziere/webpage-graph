# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.url import urljoin_rfc
from scrapy_webgraph.items import webgraphItem

site_considere = 'cdiscount.com'
class GraphspiderSpider(CrawlSpider):
    name = 'webgraph'
    allowed_domains = [site_considere]
    start_urls = ['http://www.cdiscount.com']

    rules = (
        Rule(SgmlLinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        self.log('>>>>>>>> PARSE START URL: %s' % response)
        return self.parse_item(response)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = webgraphItem()
        i['node'] = response.url
        print "#######################"
        print response.url
        print "#######################"
       # i['http_status'] = response.status
        llinks=[]
        seen = {}
        for anchor in hxs.select('//a[@href]'):
            href=anchor.select('@href').extract()[0]
            if href.startswith("http://www.cdiscount.com") and not (href in seen):
                seen[href]=True
                llinks.append(urljoin_rfc(response.url,href))
        i['edge'] = llinks
        return i
   
