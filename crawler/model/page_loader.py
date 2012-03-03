import mechanize

class PageLoader:
	def load(self, url):
		response = mechanize.Browser().open(url)
		return response.read()
