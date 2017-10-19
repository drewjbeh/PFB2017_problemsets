#!/usr/bin/env python3

# Create gene sets and produce various subsets of these

all_genes = open('alpaca_all_genes.tsv','r')
stemcell_genes = open ('alpaca_stemcellproliferation_genes.tsv','r')
pigmentation_genes = open('alpaca_pigmentation_genes.tsv','r')

all_set = set()
stemcell_set = set()
pigmentation_set = set()

for line in all_genes:
   line = line.strip()
   if "ENS" in line:
      all_set.add(line)

for line in stemcell_genes:
   line = line.strip()
   if "ENS" in line:
      stemcell_set.add(line)

for line in pigmentation_genes:
   line = line.strip()
   if "ENS" in line:
      pigmentation_set.add(line)

not_stemcell = all_set - stemcell_set
stemcell_pigment = stemcell_set & pigmentation_set

all_genes.close()
stemcell_genes.close()
pigmentation_genes.close()
