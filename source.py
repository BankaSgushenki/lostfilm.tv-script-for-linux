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
		name = lines[i][170:-13]		
		print unicode(name, 'cp1251')
	
