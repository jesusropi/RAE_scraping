import sys

from bs4 import BeautifulSoup

class word:
	pass

if __name__ == '__main__':

	arg = sys.argv
	if len(arg):
		html = open(arg[1], 'r')
		soup = BeautifulSoup(html, 'html.parser')
		print(soup.prettify())
	else:
		print 'Error!'