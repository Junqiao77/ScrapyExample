import scrapy
from tutorial.items import MovieItem

class DoubanMovieTop250Spider(scrapy.Spider):
    name = "douban_movie_top250"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    class DoubanMovieTop250Spider(scrapy.Spider):
        name = "douban_movie_top250"
        allowed_domains = ["movie.douban.com"]
        start_urls = ["https://movie.douban.com/top250"]
    def parse(self, response):
        # 从页面中选择所有的电影（每个电影被定义为一个在ol.grid_view li下的元素）
        for movie in response.css('ol.grid_view li'):
            # 初始化一个新的MovieItem实例来存储信息
            item = MovieItem()
            # 电影的排名
            item['r·1ank'] = movie.css('.item .pic em::text').get()
            # 电影的标题
            item['title'] = movie.css('.item .info .hd a .title::text').get()
            # 电影的其他标题
            item['other_title'] = movie.css('.item .info .hd a .other::text').get()
            # 电影的链接
            item['link'] = movie.css('.item .pic a::attr(href)').get()
            # 电影的海报图像链接
            item['img'] = movie.css('.item .pic a img::attr(src)').get()
            # 电影的导演和演员信息
            item['director_and_actors'] = movie.css('.item .info .bd p::text').get().strip()
            # 电影的评分
            item['rating'] = movie.css('.item .info .bd .star .rating_num::text').get()
            # 电影的评论数量
            item['reviewers'] = movie.css('.item .info .bd .star span:last-child::text').get()
            # 电影的引用（一句经典或者描绘电影特色的台词或者评论）
            item['quote'] = movie.css('.item .info .bd .quote .inq::text').get()
            # 返回item实例，Scrapy将会继续处理这个item
            yield item

            next_page = response.css('span.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
