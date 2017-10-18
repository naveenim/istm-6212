#!/usr/bin/env python

#A filter that converts upper to lower case. 

stopwords = ["and", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "the"]

import fileinput
import re

def process(line):
	words = line.split()
	words = [word for word in words if word not in stopwords]
	for a in words: print(a)

for line in fileinput.input():
	process(line)
