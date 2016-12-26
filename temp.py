# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import requests

print(os.getcwd())

bd = requests.get("http://www.baidu.com")
print(bd.url)
print(bd.encoding)

print(bd.url +" "+ bd.encoding)

print("您好")

