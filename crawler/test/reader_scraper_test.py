import os

from ..model.reader_scraper import ReaderScraper

def test_scrape_book_ids_of_given_reader():
	# Given
	scraper = ReaderScraper(41904640)
	scraper.set_page_loader(StubReaderPageLoader())
	
	# When
	book_ids = scraper.books()
	
	# Then
	assert len(book_ids) == 30
	assert book_ids[0] == '4199761'
	
def test_persistent_book_ids_of_given_book():
	# Given
	basedir = "/tmp/readers"
	scraper = ReaderScraper(41904640)
	scraper.set_page_loader(StubReaderPageLoader())
	clean_temp_directory(basedir)

	# When
	scraper.persistent(basedir)

	# Then
	assert len(os.listdir(basedir)) == 1
	assert open(basedir + "/" + "reader.41904640.csv").read().split("\n")[1] == '4199761'

def clean_temp_directory(basedir):
	try: 
		os.removedirs(basedir) 
	except: 
		pass


class StubReaderPageLoader:
	def load(self, url):
		file_name = "blank_reader_page.html" if url.endswith("?start=30") else "full_reader_page.html"
		return open(os.path.dirname(__file__) + "/fixture/" + file_name).read()
