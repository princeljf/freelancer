#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2019-04-27 14:50:51
# Project: tusharePro

from pyspider.libs.base_handler import *
import pymongo

###获取两个字符串中间的值
def getStrBetween(str="",startStr="",endStr=""):
    sLength = len(startStr)
    eLength = len(endStr)
    if(sLength>0):
        startIndex = str.find(startStr) + sLength
    else:
        startIndex = 0
    if(eLength>0):
        endIndex = str.find(endStr)
    else:
        endIndex = len(str)
    result = str[startIndex:endIndex]
    return result;
###获取输入参数/输出参数
def getTable2tushare(pyQueryTable, fields):
    pqTable = pyQueryTable
    inputfield = fields
    inputArr = []
    for i in range(pqTable('tbody tr').length):
        tds = pqTable('tbody tr').eq(i)('td')
        index = 0
        item = {}
        for key in inputfield['keys']:
            item[key] = tds.eq(index).text()
            index+=1
        inputArr.append(item)
    return inputArr


class Handler(BaseHandler):
    def __init__(self):
        self.items = False
    crawl_config = {
    }
    
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://tushare.pro/document/2', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        self.items = response.doc('a[href^="https://tushare.pro/document/2"]').items()
        for each in self.items:
            self.crawl(each.attr.href, callback=self.detail_page)
    
    @config(priority=2)
    
    def detail_page(self, response):
        content = response.doc('.document .content')
        inputTable = content('table').eq(0)
        outputTable = content('table').eq(1)
        inputField = {
            "keys": ['name','type','required','describe'],
            "values": ['名称','类型','必选','描述']
        }
        outputField = {
            "keys": ['name','type','describe'],
            "values": ['名称','类型','描述']
        }
        inputArr = getTable2tushare(inputTable, inputField)
        outputArr = getTable2tushare(outputTable, outputField)
        apiKey = getStrBetween(content('p').eq(0).text(),'接口：','\n描述：')
        tsApi = {
            apiKey: {
                "api": apiKey,
                "name": content('#-').text(),
                "describe": getStrBetween( content('p').eq(0).text(), '\n描述：' ),
                "inputField": inputField,
                "input": inputArr,
                "outputField": outputField,
                "output": outputArr
            }
        }
    
        print('------')
        return tsApi

    def on_result(self, result):
        #print(result)
        if not result:
            return
        apiKey = {}
        for key in result:
            apiKey = result[key]
        #print(apiKey)
        if len(apiKey['input'])==0:
            return

        client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        db = client['pyspider_resultdb'] #config.json数据库配置名
        coll = db['tusharePro'] #表名

        data = apiKey
        data_id = coll.insert(data)
        print (data_id)
    
