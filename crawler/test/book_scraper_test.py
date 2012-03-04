import os
import shutil

from ..model.scrapers import BookScraper	

class TestBookScraper:
	def setUp(self):
		self.basedir = "/tmp/books"
		self.clean_temp_directory()
		self.scraper = BookScraper(1766670, self.basedir)
		self.scraper.set_page_loader(StubBookPageLoader())
	
	def test_scrape_reader_ids_of_given_book(self):
		# When
		reader_ids = self.scraper.readers()
	
		# Then
		assert len(reader_ids) == 40
		assert reader_ids[0] == "53516791"
	
	def test_persistent_reader_ids_of_given_book(self):
		# When
		self.scraper.persistent()
	
		# Then
		assert len(os.listdir(self.basedir)) == 1

	def test_spawn_book_scrapers(self):
		# When
		reader_scrapers = self.scraper.spawn()

		# Then
		assert len(reader_scrapers) == 40
		assert reader_scrapers[0].id == '53516791'

	def test_load_scraped_data_when_initiation(self):
		# Given
		os.makedirs(self.basedir)
		shutil.copyfile(os.path.dirname(__file__) + "/fixture/book.1766670.csv", self.basedir + "/book.1766670.csv")
		
		# When
		scraper = BookScraper(1766670, self.basedir)
		
		# Then
		assert len(scraper._results) == 32
		assert scraper._results[0] == "53516791"

	def clean_temp_directory(self):
		shutil.rmtree(self.basedir, True) 
	
class StubBookPageLoader:
	def load(self, url):
		file_name = "blank_book_page.html" if url.endswith("?start=40") else "full_book_page.html"
		return open(os.path.dirname(__file__) + "/fixture/" + file_name).read()
