import time

from collections import deque

from scrapers import BookScraper, ReaderScraper

class Crawler:
	def __init__(self, book_id, limit=1000, basedir="data"):
		self.limit = limit
		self.basedir = basedir
		self.scrapers_queue = deque()
		self.scrapers_queue.append(BookScraper(book_id, self.basedir))
		
	def run(self):
		while(self.limit > 0 and len(self.scrapers_queue) > 0):
			scraper = self.scrapers_queue.pop()
			if(scraper.need_scrape()):
				self.limit -= 1
			scraper.persistent()
			for new_scraper in scraper.spawn():					
				if(isinstance(new_scraper, ReaderScraper)):
					self.scrapers_queue.append(new_scraper)
				else:
					if(len(self.scrapers_queue) > 1000):
						continue
					self.scrapers_queue.appendleft(new_scraper)
			print "[" + time.asctime() + "] Scraped " + scraper.id + " at " + str(self.limit) + ". In queue: " + str(len(self.scrapers_queue))