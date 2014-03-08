#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

import urllib

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def load_html():
	url = 'http://www.lostfilm.tv'
	return urllib.urlopen(url) 

infile = load_html()

file = open("/home/kostya/Development/Python/lostfilmScript/lostfilm.tv-app/lost.txt", "r")
temp = file.readline()
file.close()

lines = infile.readlines()
for i in range(len(lines)):
	line = lines[i]
	if "text-decoration:none" in line:
		serial_name = lines[i][170:-13]	
		serial_name = serial_name + "  (new episod on lostfilm.tv)"			
		episod_name = lines[i+3][166:-13]
		break

if temp == serial_name:
	sendmessage(unicode(serial_name, 'cp1251'))

file = open("/home/kostya/Development/Python/lostfilmScript/lostfilm.tv-app/lost.txt", "w")
file.write(serial_name)
file.close()
		

