#!/usr/bin/env python3

import sys
import re
import numpy

input_fq = open(sys.argv[1],'r')

seq_count = 0
line_num = 0
seq_length = []
seq_qual = []
total_qual = []

for line in input_fq:
	line_num += 1
	line = line.strip()
	if line_num % 4 == 1:
		seq_count += 1
	elif line_num % 4 == 2:
		seq_length.append(len(line))
	elif line_num % 4 == 3:
		continue
	elif line_num % 4 == 0:
		for base in line:
			seq_qual.append(ord(base) - 33)
		total_qual.append(numpy.average(seq_qual))

avg_length = numpy.average(seq_length)
SD_length = numpy.std(seq_length)
avg_qual = numpy.average(total_qual)
SD_qual = numpy.std(total_qual)
print (seq_count, "sequences, with average length of",avg_length,"and std deviation of",SD_length)
print ("Average quality:", avg_qual, "with std deviation of", SD_qual)
