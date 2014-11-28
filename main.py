#!/usr/bin/env python
# coding:utf-8 

import pykka
from crawler.messe import MesseCrawler
from crawler.bigsight import BigSiteCrawler
import pprint
import sys

def safeprint(s):
    try:
        print(s)
    except UnicodeEncodeError:
        if sys.version_info >= (3,):
            print(s.encode('utf8').decode(sys.stdout.encoding))
        else:
            print(s.encode('utf8'))

def main():
    o = MesseCrawler()
    print_result(o.crawl())

    #o = BigSiteCrawler()
    #print_result(o.crawl())

def print_result(result):
    for ev in result:
        safeprint(ev.title)
        safeprint(ev.link)
        safeprint(ev.desc)

if __name__ == '__main__':
    main()

# http://stackoverflow.com/questions/5419/python-unicode-and-the-windows-console
# http://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
