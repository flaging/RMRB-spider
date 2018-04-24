# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:08:26 2018

@author: Lee
"""

#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import string
import os
import time
from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter

def getHTMLText(url):
    try:
        kv={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
        r = requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"

def getUrl(html):
    
    url = re.findall('/page.*?\.pdf',html)
    print(url)
    return url

def downloadUrl(url,root1):   
    kv={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
    for i in url:
        root=root1

        for j in i.split('/')[1:-2]:
            root = root + j+ '//'
            
        path = root+str(i).split('/')[-1]
        try:
            if not os.path.exists(root):
                os.makedirs(root)
            if not os.path.exists(path):
                urli='http://paper.people.com.cn/rmrb'+i
                r = requests.get(urli,timeout=30,headers=kv)
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
                    print(i+" saved success!\n")
            else:
                print(i+" already exists!\n")
        except:
            print(i+" saved unsuccess!\n")
        time.sleep(0.1)
    return root
    
def PDFMergeFun(root,pdflist,desLocation):
    os.chdir(root)
    print(desLocation)
    pdfout=open(desLocation,"wb")
    pdfw=PdfFileWriter()
    for i in pdflist:
        pdfFile=open(i,'rb')
        print('open '+i)
        pr=PdfFileReader(pdfFile)
        for PageNum in range(pr.numPages):
            pdfw.addPage(pr.getPage(PageNum))

    pdfw.write(pdfout)
    pdfout.close()
    pdfFile.close()

def getFiles(root):
    for root,dirs,files in os.walk(root):
#        print(root)
#        print(dirs)
#        print(files)
        return root,files
    
def merger_pdf(filenames, merged_name, passwords=None):
    """
    传进来一个文件列表，将其依次融合起来
    :param filenames: 文件列表
    :param passwords: 对应的密码列表
    :return:
    """
    # 计算共有多少文件
    filenums = len(filenames)
    # 注意需要使用False 参数
    pdf_merger = PdfFileMerger(False)

    for i in range(filenums):
        # 得到密码
        if passwords is None:
            password = None
        else:
            password = passwords[i]
        pdf_reader = get_reader(filenames[i], password)
        if not pdf_reader:
            return
        # append默认添加到最后
        pdf_merger.append(pdf_reader)

    pdf_merger.write(open(merged_name, 'wb'))

def get_reader(filename, password):
    try:
        old_file = open(filename, 'rb')
    except IOError as err:
        print('文件打开失败！' + str(err))
        return None

    # 创建读实例
    pdf_reader = PdfFileReader(old_file, strict=False)

    # 解密操作
    if pdf_reader.isEncrypted:
        if password is None:
            print('%s文件被加密，需要密码！' % filename)
            return None
        else:
            if pdf_reader.decrypt(password) != 1:
                print('%s密码不正确！' % filename)
                return None
    if old_file in locals():
        old_file.close()
    return pdf_reader



def getFiles(root):
    # This is a basic func for merge PDFs.
#    for root, dirs, files in os.walk(root):
#        return root, files
    return os.listdir(root)

def mergeAll(fileLocation):
    files = getFiles(fileLocation)
#    print(files)
    os.chdir(fileLocation)
    merger_pdf(files, 'rmrb20170101.pdf')    
    

def main():

    rootUrl= 'http://paper.people.com.cn/rmrb/html/2017-04/02/nbs.D110000renmrb_01.htm'
    root="D://MyRes//rmrb//"
    html=getHTMLText(rootUrl)
    url=getUrl(html)
    fileDestination = downloadUrl(url,root)
    fileDestination = root+'page//2017-04//02//'
    [root,files]=getFiles(fileDestination)
    #print(files)
    PDFMergeFun(root,files,'test.pdf')
#    PDFMergeFun(pdfFile,des)
#    
    #PDFMergeAll(root)
    
    print("Work done!")

main()
