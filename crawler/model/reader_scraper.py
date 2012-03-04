from base_scraper import BaseScraper

class ReaderScraper(BaseScraper):
	def scraper_name(self):
		return "reader"
		
	def books(self):
		return self.results()
		
	def url(self, start):
		return "http://book.douban.com/people/" + str(self.id) + "/collect?start=" + str(start)
		
	def data_link(self):
		return "//div[@class='item']//div[@class='pic']//a"
		
	def page_size(self):
		return 15
