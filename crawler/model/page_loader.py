import mechanize
import cookielib

browser = mechanize.Browser()
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
browser.addheaders = [
	('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'),
	('Connection', 'keep-alive'),
	('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
	('Accept-Encoding', 'gzip,deflate,sdch'),
	('Accept-Language', 'en-US,en;q=0.8'),
	('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q-0.3')
]

class PageLoader:	
	def load(self, url):		
		response = browser.open(url)
		return response.read()
