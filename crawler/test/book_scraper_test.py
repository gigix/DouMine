from ..model.book_scraper import BookScraper

def test_scrape_reader_ids_of_give_book():
	scraper = BookScraper(1140457)
	assert len(scraper.readers()) >= 1064