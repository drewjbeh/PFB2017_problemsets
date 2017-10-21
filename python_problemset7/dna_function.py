#!/usr/bin/env python3

import re
import sys

fasta = open(sys.argv[1],'r')
format_fasta = open(sys.argv[3],'w')
line_length = int(sys.argv[2])

def format_dna(sequence, line_length):
	sequence = re.sub('\n','',sequence)
	new_seq = ''
	while sequence:
		if len(sequence) >= line_length:
			new_seq += sequence[0:line_length] + '\n'
			sequence = sequence[line_length:len(sequence)]
		else:
			new_seq += sequence[0:len(sequence)]
			sequence = ''
	return new_seq

out = ''

for line in fasta:
	if line.startswith(">"):
		out = line.strip()
		format_fasta.write(out + '\n')
	else:
		out = line.strip()
		out += out
		new_out = format_dna(out, line_length)
		format_fasta.write(new_out + '\n')
			 	 
