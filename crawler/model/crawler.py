from Queue import Queue

from scrapers import BookScraper, ReaderScraper

class Crawler:
	def __init__(self, book_id, basedir="data", limit=1000):
		self.limit = limit
		self.basedir = basedir
		self.scrapers_queue = Queue()
		self.scrapers_queue.put(BookScraper(book_id, self.basedir))
		
	def run(self):
		while(self.limit > 0 and not self.scrapers_queue.empty()):
			self.limit -= 1
			scraper = self.scrapers_queue.get()
			scraper.persistent()
			for new_scraper in scraper.spawn():
				self.scrapers_queue.put(new_scraper)
			print "Scraped item " + scraper.id + ", " + str(self.limit) + " items to go."