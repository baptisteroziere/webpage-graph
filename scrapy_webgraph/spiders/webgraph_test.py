# -*- coding: utf-8 -*-
import scrapy


class WebgraphSpider(scrapy.Spider):
    name = "webgraph_test"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    #allowed_domains = ["perso.ens-lyon.fr/baptiste.roziere"]
    #start_urls = (
    #    'http://www.perso.ens-lyon.fr/baptiste.roziere/',
    #)

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        
