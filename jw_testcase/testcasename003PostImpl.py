
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
import time,os,sys,datetime,unittest
import os
sys.path.append("../")
sys.path.append("../jw_modules")
import httplib
import unittest
import json
import urllib


class testcase_api_httpsendpost(unittest.TestCase):
    def setUp(self):
        # self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn', 81, timeout=10)

    def tearDown(self):
        # self.widget.dispose()
        # self.widget = None
        self.httpClient.close()

    def test_testcasename003(self):
        try:
            f=open("")
            strcreateoder=json.load(f)
            print strcreateoder
            params = urllib.urlencode(strcreateoder)
            headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
            self.httpClient.request('POST', "", params, headers)
            #response是HTTPResponse对象
            response = self.httpClient.getresponse()
            print response.status
            statucode=response.status
            print response.read()
            if statucode=='200' or statucode=='201':
                print "The get_order_list status is 200 or 201"
            else:
                raise "The interface has exception"
                print response.reason
                print response.read()
                #self.assertEqual(statucode, 200,'incorrect default size')
        except Exception, e:
            print e