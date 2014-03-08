# -*- coding: utf-8 -*-

import urllib

def load_html():
	url = 'http://www.lostfilm.tv'
	return urllib.urlopen(url) 

infile = load_html()

lines = infile.readlines()
for i in range(len(lines)):
	line = lines[i]
	if "text-decoration:none" in line:
		serial_name = lines[i][170:-13]		
		print unicode(serial_name, 'cp1251')
		episod_name = lines[i+3][166:-13]
		print unicode(episod_name, 'cp1251')
	
