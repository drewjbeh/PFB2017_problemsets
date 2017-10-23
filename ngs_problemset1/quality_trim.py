#!/usr/bin/env python3

import sys
import re

input = open(sys.argv[1],'r')
output = open(sys.argv[2],'w')

line_num = 0
seq_qual = []
trim_site = 0
untrimmed_seq = ''

for line in input:
	seq_qual = []
	line = line.strip()
	line_num += 1
	if line_num % 4 == 0:
		for base in line:
			seq_qual.append(ord(base) - 33)
		for qual in seq_qual:
			if qual < 20:
				trim_site = seq_qual.index(qual)
				break
		trimmed_qual = line[:trim_site]
		trimmed_seq = untrimmed_seq[:trim_site]
		output.write(id + '\n' + trimmed_seq + '\n' + thing + '\n' + trimmed_qual + '\n')
	elif line_num % 4 == 2:
		untrimmed_seq = line
	elif line_num % 4 == 1:
		id = line
	elif line_num % 4 == 3:
		thing = line
