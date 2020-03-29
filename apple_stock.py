#! /usr/bin/env python3

#IS211 Assignment 9 - "apple_stock.py" 2/2

from bs4 import BeautifulSoup
import lxml
from six.moves import urllib
import urllib.request
import urllib.error

htmlFile = urllib.request.urlopen('https://www.nasdaq.com/market-activity/stocks/aapl/historical')

bsObject = BeautifulSoup(htmlFile, features = "lxml")

stockData = bsObject.findAll('tr')

def main():
	for x in stockData:
		data = x.findAll('td', {"class":"data"})
		if len(data) is 6:
			date = data[0].contents[0]
			close = data[1].contents[0]
			print("The date is: {}, Price at Closing: {}".format(date, close))
			
if __name__ == '__main__':
	main()
