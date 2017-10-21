#!/usr/bin/env python3

import sys
import re

# Take input fasta, read into dict, count A, C, G, T and store in dict inside dict

file = open(sys.argv[1],'r')
seq_dict = {}
full_seq = ''
seq_name = ''

for line in file:
   if line.startswith(">"):
      seq_name = re.search("^>(\w+)\s.*",line).group(1)
      seq_dict[seq_name] = full_seq
   else:
      full_seq = line.strip()
      seq_dict[seq_name] += full_seq

for seq in seq_dict:
   As = seq_dict[seq].count("A")
   Cs = seq_dict[seq].count("C")
   Ts = seq_dict[seq].count("T")
   Gs = seq_dict[seq].count("G")
   seq_dict[seq] = {"A":As, "C":Cs, "G":Gs, "T":Ts} # Change seq value in dict to another dict with count data
   print(seq, seq_dict[seq]["A"], seq_dict[seq]["T"], seq_dict[seq]["G"], seq_dict[seq]["C"], sep = "\t")   

