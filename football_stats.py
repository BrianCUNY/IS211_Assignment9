#! /usr/bin/env python3

#IS211 Assignment 9 - "football_stats.py" 1/2

from bs4 import BeautifulSoup
import lxml
from six.moves import urllib
import urllib.request
import urllib.error

htmlFile = urllib.request.urlopen('https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns')

bsObject = BeautifulSoup(htmlFile, features = "lxml")

rankingTable = bsObject.findAll("table", attrs={"class":"data"})[0].findAll('tr', attrs={"valign":"top"})

def main():
	counter = 0
	print("The top 20 players of 2019 are: ")
	for x in rankingTable:
		name = x.findAll('td')[0].findAll('a')[0].contents[0]
		position = x.findAll('td')[1].contents[0]
		team = x.findAll('td')[2].findAll('a')[0].contents[0]
		tds = x.findAll('td')[6].contents[0]
		counter += 1
		print("Ranking: {}, Name: {}, Position {}, Team: {}, TDs: {}".format(counter, name, position, team, tds))
		if counter >= 20:
			break

if __name__ == '__main__':
	main()
