#!/usr/bin/env python3

import sys
import pronto

ont = pronto.Ontology('/Users/admin/Desktop/pfb2017/PFB2017_problemsets/GO_problemset/go.owl')

my_genes = sys.argv[1]
my_go = sys.argv[2]

term_obj = ont[my_go]
term_name = term_obj.name 
term_children = term_obj.rchildren()

all_children = {}
all_children[my_go] = term_name

for child in term_children:
	all_children[child.id] = child.name

matched_genes = {}
my_genes = open(my_genes,'r')

for line in my_genes:
	line = line.strip()
	line = list(line.split('\t'))
	if len(line) == 3:
		if line[1] in all_children:
			go_info = [line[1],line[2]]
			matched_genes[line[0]] = go_info

for gene in matched_genes:
	print(gene, matched_genes[gene], sep = '\t')

print(len(matched_genes))
