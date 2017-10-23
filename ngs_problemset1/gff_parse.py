#!/usr/bin/env python3

import sys
import numpy

input = open(sys.argv[1],'r')

gene_lengths = []
exon_lengths = []
exon_count = 0
exon_counts = []

for line in input:
	if line.startswith('##'):
		continue
	if line.split('\t')[2] == 'gene':
		start = int(line.split('\t')[3])
		stop = int(line.split('\t')[4])
		gene_lengths.append(stop - start)
	if line.split('\t')[2] == 'exon':
		exon_count += 1
		start = int(line.split('\t')[3])
		stop = int(line.split('\t')[4])
		exon_lengths.append(stop - start)
	if line.split('\t')[2] == "mRNA":
		exon_counts.append(exon_count)
		exon_count = 0

exon_counts.append(exon_count)
exon_count = 0

print('Average gene length:',numpy.average(gene_lengths), '\nAverage exon length:', numpy.average(exon_lengths))
print('Average exons per mRNA:', numpy.average(exon_counts))
