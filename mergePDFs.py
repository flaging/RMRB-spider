# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:08:26 2018

@author: Lee
"""

# coding=utf-8

import os
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter

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


def main(filedir):
    files = getFiles(filedir)
    os.chdir(filedir)
    print(files[1])
    merger_pdf(files, str(files[1])[0:-6]+str(files[1])[-4:])
    print('work down!')


main('D://MyRes//rmrb//page//2018-02//03')
