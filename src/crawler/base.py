import requests
import os


class CrawlerBase:

    def _fetch_content(self, url):
        # for debug
        if True:
            fname = "dump_%s.html" % (self._id)
            if os.path.isfile(fname):
                f = open(fname, 'br')
                page = f.read()
                f.close()
            else:
                f = open(fname, 'bw')
                page = requests.get(url)
                page = str.encode(page.text)
                f.write(page)
                f.close()
            return page
        else:
            page = requests.get(url)
            page = page.text
            return page


    def crawl():
        raise Exception('not impl')
