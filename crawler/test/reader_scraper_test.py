import os
import shutil

from ..model.scrapers import ReaderScraper

class TestReaderScraper:
	def setUp(self):
		self.basedir = "/tmp/readers"
		self.clean_temp_directory()
		self.scraper = ReaderScraper(41904640, self.basedir)
		self.scraper.set_page_loader(StubReaderPageLoader())		
	
	def test_scrape_book_ids_of_given_reader(self):
		# When
		book_ids = self.scraper.books()
	
		# Then
		assert len(book_ids) == 30
		assert book_ids[0] == '4199761'
	
	def test_persistent_book_ids_of_given_book(self):
		# When
		self.scraper.persistent()

		# Then
		assert len(os.listdir(self.basedir)) == 1
		assert open(self.basedir + "/" + "reader.41904640.csv").read().split("\n")[1] == '4199761'
	
	def test_spawn_book_scrapers(self):
		# When
		book_scrapers = self.scraper.spawn()
		
		# Then
		assert len(book_scrapers) == 30

	def clean_temp_directory(self):
		shutil.rmtree(self.basedir, True) 


class StubReaderPageLoader:
	def load(self, url):
		file_name = "blank_reader_page.html" if url.endswith("?start=30") else "full_reader_page.html"
		return open(os.path.dirname(__file__) + "/fixture/" + file_name).read()
