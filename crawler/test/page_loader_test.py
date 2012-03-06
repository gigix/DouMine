from ..model.page_loader import PageLoader

class TestPageLoader:
	def test_return_none_if_page_does_not_exist(self):
		page_loader = PageLoader()
		assert page_loader.load("http://www.douban.com/people/does_not_exist") == None