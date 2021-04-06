import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"
    
    def start_requests(self):
        urls = [
            "http://books.toscrape.com/catalogue/page-1.html",
            "http://books.toscrape.com/catalogue/page-2.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'posts-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')