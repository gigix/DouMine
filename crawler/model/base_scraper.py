import re

import mechanize

from lxml import etree

class BaseScraper:
	def __init__(self, id):
		self.id = id
	
	def results(self):
		br = mechanize.Browser()
		has_more_items = True
		start = 0
		result = []
		
		while(has_more_items):
			response = br.open(self.url(start))
			page_content = response.read()
			page_dom = etree.HTML(page_content)
			links = page_dom.xpath(self.data_link())
			data_urls = map(lambda link: link.get("href"), links)
			result_ids = map(lambda url: re.search("http://book.douban.com/\w+/(.+)/", url).group(1), data_urls)
			
			has_more_items = len(result_ids) > 0
						
			for an_id in result_ids:
				result.append(an_id)
			
			start += self.page_size()
				
		return result