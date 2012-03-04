import re
import os

from lxml import etree

from page_loader import PageLoader

class BaseScraper:
	def __init__(self, id):
		self.id = id
		self.page_loader = PageLoader()
	
	def persistent(self, basedir):
		if(not os.access(basedir, os.F_OK)):
			os.makedirs(basedir)
		csv_file = open(basedir + "/" + self.scraper_name() + "." + str(self.id) + ".csv", "w")
		csv_file.write("ID\n")
		for result in self.results():
			csv_file.write(result + "\n")
		csv_file.close()
			
	def results(self):
		has_more_items = True
		start = 0
		result = []
		
		while(has_more_items):
			page_content = self.load_page(start)
			page_dom = etree.HTML(page_content)
			links = page_dom.xpath(self.data_link())
			data_urls = map(lambda link: link.get("href"), links)
			result_ids = map(lambda url: re.search("http://book.douban.com/\w+/(.+)/", url).group(1), data_urls)
			
			has_more_items = len(result_ids) > 0
						
			for an_id in result_ids:
				result.append(an_id)
			
			start += self.page_size()
				
		return result
		
	def load_page(self, start):
		return self.page_loader.load(self.url(start))
		
	def set_page_loader(self, page_loader):
		self.page_loader = page_loader
