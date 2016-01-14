import urllib2
import sys

from bs4 import BeautifulSoup


HDR = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': '', 'Accept-Language': 'es,en-US;q=0.7,en;q=0.3', 
	'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 
	'Cockie' : '_ga=GA1.2.18416288.1377687530; DRUPAL_UID=-1; TS014dfc77=017ccc203ce856eea4772c5cc70fa4efc44e8133a567e08b7e2bfe4c96191d5b50f40a54dd; has_js=1; _gat=1',
	'Host': 'lema.rae.es', 
	'Referer': 'http://dle.rae.es/srv/fetch/?w=',
	'User-Agent': 'Mozilla'}

URL = 'http://dle.rae.es/srv/fetch/?w='


def get_html(url, headers):
	req = urllib2.Request(url, headers=headers)
	r = urllib2.urlopen(req)
	page = r.read()
	return page


def get_means(page):
	return None

def get_all_key_words(page):
	return None

if __name__ == '__main__':
	p = sys.argv
	if len(p) > 1:
		final_url = URL + p[1]	
		HDR['Referer'] = final_url
		print get_html(final_url, HDR) 