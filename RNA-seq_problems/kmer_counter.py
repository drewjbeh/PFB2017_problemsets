#!/usr/bin/env python3

# split reads into kmers and count kmers

import sys

usage = "\n\n\tusage: {} kmer_length fq_file num_top_kmers\n\n".format(sys.argv[0])

if len(sys.argv) < 4:
	sys.stderr.write(usage)
	sys.exit(1)

kmer_length = int(sys.argv[1])
fq_file = sys.argv[2]
num_top_kmers = int(sys.argv[3])

fq_file = open(fq_file,'r')
line_num = 0

kmers = {}

def count_kmers(kmer_dict, sequence, kmer_length):
	while sequence:
		kmer = sequence[0:kmer_length]
		if len(kmer) == kmer_length:
			if kmer in kmer_dict:
				kmer_dict[kmer] += 1
			else:
				kmer_dict[kmer] = 1

			#look up collections.default.dict for this

		sequence = sequence[1:len(sequence)]

for line in fq_file:
	line = line.rstrip()
	line_num += 1
	if line_num % 4 == 2:
		count_kmers(kmers, line, kmer_length)

top_kmers = sorted(kmers, key=lambda x:kmers[x], reverse = True)[0:num_top_kmers]
for item in top_kmers:
	print("{}\t{}".format(item,kmers[item]))

sys.exit(0) # this is good practice to set exit status to 0, i.e. everything went well
	    # good for bioinformatics pipelines where you want to check exit status between issuing new 
	    # commands or going on to next step
