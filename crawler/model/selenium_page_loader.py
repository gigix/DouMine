from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumPageLoader:
	def __init__(self):
		fp = webdriver.FirefoxProfile()
		fp.set_preference("permissions.default.image", 2)
		self.driver = webdriver.Firefox(firefox_profile=fp)
		
	def __del__(self):
		self.driver.close()
	
	def load(self, url):	
		try:	
			self.driver.get(url)
			return self.driver.page_source
		except Exception as e:
			self.driver.close()
			raise e
