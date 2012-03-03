from ..model.book_scraper import BookScraper

def test_scrape_reader_ids_of_given_book():
	scraper = BookScraper(1766670)
	reader_ids = scraper.readers()
	assert len(reader_ids) == 32
	assert reader_ids[0] == "53516791"