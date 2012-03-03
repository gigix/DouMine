from ..model.reader_scraper import ReaderScraper

def test_scrape_book_ids_of_given_reader():
	scraper = ReaderScraper(41904640)
	book_ids = scraper.books()
	assert len(book_ids) == 38
	# assert book_ids[0] = 4199761