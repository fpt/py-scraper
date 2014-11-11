from lxml import html
from lxml import etree
from lxml.cssselect import CSSSelector
from base import CrawlerBase
from calevent import CalEvent
import pprint


class BigSiteCrawler(CrawlerBase):
    def __init__(self):
        self._id = 'bigsight'
        self._url = 'http://www.bigsight.jp/event/'

    def crawl(self):
        page = self._fetch_content(self._url)

        tree = html.fromstring(page)

        events = tree.cssselect('ul#EventList li')

        arr = []
        for li in events:
            ev = CalEvent()
            ev.title = li.cssselect('div.eventArea h3 a')[0].text
            ev.link = li.cssselect('div.eventArea h3 a')[0].attrib['href']
            ev.desc = li.cssselect('div.eventArea p.discription')[0].text
            arr.append(ev)
            print('date:  ', li.cssselect('div.date')[0].text)
            print('title: ', li.cssselect('div.eventArea h3 a')[0].text)
            print('link:  ', li.cssselect('div.eventArea h3 a')[0].attrib['href'])
            print('desc:  ', li.cssselect('div.eventArea p.discription')[0].text)

        return arr

o = BigSiteCrawler()
pprint.pprint(o.crawl())

# http://docs.python-guide.org/en/latest/scenarios/scrape/
