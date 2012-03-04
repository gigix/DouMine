from base_scraper import BaseScraper

class BookScraper(BaseScraper):
	def scraper_name(self):
		return "book"
		
	def readers(self):
		return self.results()
		
	def url(self, start):
		return "http://book.douban.com/subject/" + str(self.id) + "/collections?start=" + str(start)
		
	def data_link(self):
		return "//div[@id='collections_tab']//div[@class='sub_ins']//div[@class='pl2']//a"
		
	def page_size(self):
		return 20
