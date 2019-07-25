#!/usr/bin/python2
# -*- coding: utf-8 -*-

import requests


class Request_Method(object):
    cookies = None

    def requests(self,method,url,data):
        method = method.upper()
        res = None
        if method == 'GET':
            res = requests.get(url=url,params=data,cookies=self.cookies)
        elif method == 'POST':
            res = requests.post(url=url,data=data,cookies=self.cookies)
        else:
            print('请求的方式异常！！！')
        if res.cookies:
            self.cookies = res.cookies
        return res


if __name__ == '__main__':
    pass



