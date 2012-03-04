import os

from ..model.scrapers import BookScraper	

class TestBookScraper:
	def setUp(self):
		self.scraper = BookScraper(1766670)
		self.scraper.set_page_loader(StubBookPageLoader())
	
	def test_scrape_reader_ids_of_given_book(self):
		# When
		reader_ids = self.scraper.readers()
	
		# Then
		assert len(reader_ids) == 40
		assert reader_ids[0] == "53516791"
	
	def test_persistent_reader_ids_of_given_book(self):
		# Given
		basedir = "/tmp/books"
		self.clean_temp_directory(basedir)

		# When
		self.scraper.persistent(basedir)
	
		# Then
		assert len(os.listdir(basedir)) == 1

	def test_spawn_book_scrapers(self):
		# When
		reader_scrapers = self.scraper.spawn()

		# Then
		assert len(reader_scrapers) == 40
		assert reader_scrapers[0].id == '53516791'

	def clean_temp_directory(self, basedir):
		try: 
			os.removedirs(basedir) 
		except: 
			pass
	
class StubBookPageLoader:
	def load(self, url):
		file_name = "blank_book_page.html" if url.endswith("?start=40") else "full_book_page.html"
		return open(os.path.dirname(__file__) + "/fixture/" + file_name).read()
