import re
import urllib.parse
import scrapy
from scrapy.crawler import CrawlerProcess


class CoupangSpider(scrapy.Spider):
    name = 'coupang'

    def start_requests(self):
        base_url = "https://www.coupang.com/np/search"
        searches = getattr(self, 'searches', None)

        if searches is not None:
            if type(searches) is str:
                searches = re.sub('\'|\"', '', searches)
                search_list = searches.split(',')
            elif type(searches) is list:
                search_list = searches

            for search in search_list:
                query = {
                        'q': search.strip(),
                        'isPriceRange': False,
                        'page': 1,
                        'filterSetByUser': True,
                        'channel': 'user',
                        'rating': 0,
                        'sorter': 'scoreDesc',
                        'listSize': 72
                }
                url = base_url + "?" + urllib.parse.urlencode(query)
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result = dict()

        search_result = response.css('div.search-result > em')

        search_keyword = search_result.css('::text').get()
        if search_keyword and search_keyword.strip():
            search_keyword = re.sub('\'|\"', '', search_keyword)
            result['search_word'] = search_keyword.strip()

        search_count = search_result.css('strong::text').get()
        if search_count and search_count.strip():
            search_count = re.sub('\(|\)|,', '', search_count)
            result['count'] = search_count.strip()

        result['content'] = list()
        product_list = response.css('ul#productList > li.search-product')
        for product in product_list:
            result['content'].append(product.css('div.name::text').get())

        word_list = ' '.join(result['content']).split(' ')
        word_count = dict()
        for word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # sort
        word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)

        result['word_count'] = word_count
        yield result


def search(keywords):
    '''쿠팡 상품 검색

    [keywords 형식]
    '키워드,키워드' 또는 ['키워드','키워드']
    '''

    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.jsonl": {
                "format": "jsonlines",
                "encoding": "utf8",
                },
        },
        "LOG_ENABLED": False
    })

    process.crawl(CoupangSpider, searches=keywords)
    process.start() # the script will block here until the crawling is finished

