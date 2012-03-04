from base_scraper import BaseScraper

class ReaderScraper(BaseScraper):
	def books(self):
		return self.results()
		
	def _scraper_name(self):
		return "reader"
		
	def _spawn(self, book_id):
		return BookScraper(book_id, self.basedir)
	
	def _url(self, start):
		return "http://book.douban.com/people/" + str(self.id) + "/collect?start=" + str(start)
		
	def _data_link(self):
		return "//div[@class='item']//div[@class='pic']//a"
		
	def _page_size(self):
		return 15

class BookScraper(BaseScraper):
	def readers(self):
		return self.results()

	def _scraper_name(self):
		return "book"

	def _spawn(self, reader_id):
		return ReaderScraper(reader_id, self.basedir)

	def _url(self, start):
		return "http://book.douban.com/subject/" + str(self.id) + "/collections?start=" + str(start)

	def _data_link(self):
		return "//div[@id='collections_tab']//div[@class='sub_ins']//div[@class='pl2']//a"

	def _page_size(self):
		return 20