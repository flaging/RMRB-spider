# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:21:12 2018

@author: Lee
"""

import requests
from bs4 import BeautifulSoup
import re
import string
import os
import time
import PyPDF2


def getHTMLText(url):
    try:
        kv={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
        r = requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"

def getIP(html):
    ip = re.findall('(?<=<td>)\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{2,3}(?=</td>)',html)
    port = re.findall('(?<=<td>)\d{1,5}(?=</td>)',html)
    return ip,port
def main():
    html = getHTMLText('http://www.xicidaili.com/nn/')
    #print(html)
    ip,port = getIP(html)
    print(ip[2],port[2])
    
main()