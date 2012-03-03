import os

from ..model.book_scraper import BookScraper	

def test_scrape_reader_ids_of_given_book():
	# Given
	scraper = BookScraper(1766670)
	scraper.set_page_loader(StubBookPageLoader())
	
	# When
	reader_ids = scraper.readers()
	
	# Then
	assert len(reader_ids) == 40
	assert reader_ids[0] == "53516791"
	
	
class StubBookPageLoader:
	def load(self, url):
		file_name = "blank_book_page.html" if url.endswith("?start=40") else "full_book_page.html"
		return open(os.path.dirname(__file__) + "/fixture/" + file_name).read()
