import mechanize
import cookielib

class PageLoader:
	def load(self, url):
		browser = mechanize.Browser()
		cj = cookielib.LWPCookieJar()
		browser.set_cookiejar(cj)
		browser.set_handle_equiv(True)
		browser.set_handle_gzip(True)
		browser.set_handle_redirect(True)
		browser.set_handle_referer(True)
		browser.set_handle_robots(False)
		browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
		
		response = browser.open(url)
		return response.read()
