# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
# from scrapy.http import HtmlResponse
import re
import time

from rec_driver import *
# from pyredis import RedisKv

#from pymysql import PyMysql
import common

#from pymongo import MongoClient


class AttentionSpider(scrapy.spiders.Spider):
    name = "attention"
    # allowed_domains = ['weibo.com', 'weibo.cn', 'sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl='http://hq.sinajs.cn/list=sz000402,sz000971'
    #web_domain = 'http://photo.poco.cn'

    # spider_sep_per_time=3600

    iteminfo = {}
    def start_requests(self):

        return [scrapy.Request(url=self.surl, callback=self.see_list
                               )]

    def see_list(self, response):
        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta
        # return
        # print 'cookies'
        # print type(response.request.headers.getlist('Cookie')[0])
        # print response.request.headers.getlist('Cookie')[0]
        # return

        body = response.body
        # print type(body)
        # return
        res = []
        body_utf8 = body.decode('gb2312').encode('UTF-8')
        # print body_utf8

        m1 = re.finditer(r'var hq_str_sz(.*)=\"(.*)\";', body_utf8)
        # print m1
        if m1:
            for m in m1:
                name_tmp = m.groups()[0]
                str_tmp = m.groups()[1]
                list_tmp = str_tmp.split(',')
                current_scope = float(list_tmp[3])
                data_time = list_tmp[30] + ' ' + list_tmp[31]
                data_time_unix = int(time.mktime(time.strptime(data_time, "%Y-%m-%d %H:%M:%S")))
                res_dict = {'name':name_tmp,'scope':current_scope,'data_time':data_time_unix}
                res.append(res_dict)
        else:
            print 'not found'
        if not res:
            return
        res_text = common.of_upload(res)
        print res_text
        return
        # with open('hot2.txt', 'wb') as f:
        #     f.write(str)
        # return









