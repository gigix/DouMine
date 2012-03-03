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
			has_more_readers = False
			response = br.open("http://book.douban.com/subject/" + str(self.id) + "/collections?start=" + str(start))

			page_content = response.read()
			page_dom = etree.HTML(page_content)
			links = page_dom.xpath("//div[@id='collections_tab']//div[@class='sub_ins']//div[@class='pl2']//a")
			urls = map(lambda link: link.get("href"), links)
			print urls
			
			for url in urls:
				has_more_readers = True
				result.append(url)
			start += 20
				
		return result