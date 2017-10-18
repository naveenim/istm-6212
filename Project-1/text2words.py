#!/usr/bin/env python

#A NEW filter that splits lines of text into one word per line. 

import fileinput
import re

def process(line):
	select = re.compile('\w+')
	line = select.findall(line)

	for i in line:
		if len(i)>=2:
			print (i)

for line in fileinput.input():
	process(line)
