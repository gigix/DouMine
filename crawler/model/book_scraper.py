import re

import mechanize

from lxml import etree

class BookScraper:
	
	def __init__(self, id):
		self.id = id
	
	def readers(self):
		br = mechanize.Browser()
		has_more_readers = True
		start = 0
		result = []
		
		while(has_more_readers):
			response = br.open("http://book.douban.com/subject/" + str(self.id) + "/collections?start=" + str(start))
			page_content = response.read()
			page_dom = etree.HTML(page_content)
			links = page_dom.xpath("//div[@id='collections_tab']//div[@class='sub_ins']//div[@class='pl2']//a")
			reader_urls = map(lambda link: link.get("href"), links)
			reader_ids = map(lambda url: re.search("http://book.douban.com/people/(.+)/", url).group(0), reader_urls)
			
			has_more_readers = len(reader_ids) > 0
						
			for reader in reader_ids:
				result.append(reader)
			
			start += 20
				
		return result