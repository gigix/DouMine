import mechanize
from lxml import etree

br = mechanize.Browser()
response = br.open("http://book.douban.com/subject/2042269/collections")

def get_url(element):
	return element.get("href")

page_content = response.read()
page_dom = etree.HTML(page_content)
links = page_dom.xpath("//div[@id='collections_tab']//div[@class='sub_ins']//div[@class='pl2']//a")
urls = map(get_url, links)
print urls

# for link in br.links(url_regex="http://book.douban.com/people/(.+)/"):
# 	print link.url
# 	
# # print response.read()
# 
# br.open("http://book.douban.com/people/keeplazy/collect")
# for link in br.links(url_regex="http://book.douban.com/subject/(.+)/"):
# 	print link.url