#!/usr/bin/env python3

import sys
import re

usage = "\n\nUsage: {} bam_file\n\n".format(sys.argv[0])

if len(sys.argv) < 2:
	sys.stderr.write(usage)
	sys.exit(1)

bam_file = open(sys.argv[1],'r')

read_dict = {}
count_dict = {}

for line in bam_file:
	line = line.rstrip()
	line_split = line.split('\t')
	gene = line_split[2]
	gene = re.search("(.+)\^",gene).groups(1)[0]
	read_gene = line_split[0] + '*' + gene
	read_dict[read_gene] = 1

for match in read_dict:
	gene = re.search('.+\*(.+)', match).groups(1)[0]
	if gene in count_dict:
		count_dict[gene] += 1
	else:
		count_dict[gene] = 1

count_dict_sorted = sorted(count_dict, key = lambda x:count_dict[x], reverse=True)

for i in count_dict_sorted:
	print("{}\t{}".format(i, count_dict[i]))	
