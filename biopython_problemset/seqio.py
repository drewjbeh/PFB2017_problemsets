#!/usr/bin/env python3

from Bio import SeqIO
import sys
import re

input = sys.argv[1]
ids = []
descrips = []
species = []
species_count = {}
salmonella_records = []

for record in SeqIO.parse(input, "fasta"):
	ids.append(record.id)
	descrips.append(record.description)
	match = re.search("OS=([a-zA-Z]+? [a-zA-Z]+?) .*",record.description)
	if match:
		species.append(match.group(1))
	salmonella = re.search("OS=Salmonella paratyphi B", record.description)
	if salmonella:
		salmonella_records.append(record)

SeqIO.write(salmonella_records, 's_paratyphi.prot.fa', 'fasta')	

for item in species:
	if item in species_count:
		species_count[item] += 1
	else:
		species_count[item] = 1
print(len(ids))
print(species_count)
