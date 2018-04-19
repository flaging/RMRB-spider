# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:08:26 2018

@author: Lee
"""

# coding=utf-8
import requests
import re
import string
import os
import time
import PyPDF2


def mergePDFsinDir(root, pdflist, desLocation):
    # This is for merge all pages from same date, and save it as a single PDF.
    # But this don't work.
    os.chdir(root)
    print(desLocation)
    print(os.getcwd())
    pdfout = open(desLocation, "wb")
    pdfw = PyPDF2.PdfFileWriter()
    for i in pdflist:
        pdfFile = open(i, 'rb')
        print('open '+i)
        pr = PyPDF2.PdfFileReader(pdfFile)

        for PageNum in range(pr.numPages):
            pdfw.addPage(pr.getPage(PageNum))
        print(pr.pageMode)

    pdfw.write(pdfout)
    pdfout.close()
    pdfFile.close()


def getFiles(root):
    # This is a basic func for merge PDFs.
    for root, dirs, files in os.walk(root):
        return root, files


def main():
    root, files = getFiles('E://Test//')
    mergePDFsinDir('E://Test//', files, 'c1.pdf')
    print('work down!')


main()
