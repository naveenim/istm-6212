#!/usr/bin/env python

#A filter that converts upper to lower case. 

import fileinput


def process(line):
	print(line.lower().strip())

for line in fileinput.input():
	process(line)
