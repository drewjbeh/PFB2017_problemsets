#!/usr/bin/env python3

# Read gene sets and find common genes with sets

input_tf = open('alpaca_transcriptionFactors.tsv','r')
input_stemcell = open('alpaca_stemcellproliferation_genes.tsv','r')

tf_set = set()
stemcell_set = set()

for line in input_tf:
   line = line.strip()
   if "ENS" in line:
      tf_set.add(line)

for line in input_stemcell:
   line = line.strip()
   if "ENS" in line:
      stemcell_set.add(line)

tf_prolif = stemcell_set & tf_set
print(tf_prolif)
