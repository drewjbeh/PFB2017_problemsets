#!/usr/bin/env python3

import sys
import os
import re

rand_length = sys.argv[1]

files = os.listdir()
matched_files = []
line_dict = {}
big_dict = {}
field_names = ["qseqid", "sseqid", "percid", "alen", "mismat", "gaps", "q_start", "q_end", "s_start", "s_end", "evalue", "bits"]

for file in files:
	if re.search(rand_length,file):
		matched_files.append(file)

for match in matched_files:
	matrix = re.search('qfo_(.+?).txt', match).group(1)
	print(matrix)
	curr = open(match,'r')
	for line in curr:
		line = line.strip('\n')
		if not line.startswith('#'):
			line_dict = dict(zip(field_names, line.split('\t')))
			break
	big_dict[matrix] = line_dict
print(big_dict)
