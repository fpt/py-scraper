from lxml import html
from lxml import etree
from lxml.cssselect import CSSSelector
from base import CrawlerBase
from calevent import CalEvent
import pprint

class MesseCrawler(CrawlerBase):
    def __init__(self):
        self._id = 'messe'
        self._url = 'http://www.m-messe.co.jp/event/list'
        self._force_encoding = 'UTF-8'

    def crawl(self):
        page = self._fetch_content(self._url)
        #page = page.decode('shift_jis')

        tree = html.fromstring(page)

        events = tree.cssselect('ul.event_list li')

        arr = []
        for li in events:
            ev = CalEvent()
            ev.title = li.cssselect('p.event_head a span.date')[0].tail.strip()
            ev.desc = li.cssselect('div.event_body table tr td.right')[0].text.strip()
            arr.append(ev)
            #print('date:  ', li.cssselect('p.event_head a span.date')[0].text.strip())
            #print('title: ', li.cssselect('p.event_head a span.date')[0].tail.strip())
            #print('desc:  ', li.cssselect('div.event_body table tr td.right')[0].text.strip())
        return arr

#o = MesseCrawler()
#pprint.pprint(o.crawl())


# http://docs.python-guide.org/en/latest/scenarios/scrape/
