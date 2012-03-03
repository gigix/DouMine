import mechanize
import cookielib

br = mechanize.Browser()
response = br.open("http://book.douban.com/subject/2042269/collections")

for link in br.links(url_regex="http://book.douban.com/people/(.+)/"):
	print link.url
	
# print response.read()

br.open("http://book.douban.com/people/keeplazy/collect")
for link in br.links(url_regex="http://book.douban.com/subject/(.+)/"):
	print link.url