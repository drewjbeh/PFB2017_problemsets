#!/usr/bin/env python3

import re

sequence = open('Python_06_ApoI.fasta','r')

restr_frag = []
seq_dict = {}
seq_dict_cut = {}
key = ""
value = ""

for line in sequence:
   line = line.strip()
   if line.startswith(">"):
      key = line
      seq_dict[line] = value
   else:
      value += line
      seq_dict[key] = value

for id,seq in seq_dict.items():
   cut = re.findall(r'[AG]AATT[CT]',seq)
   print(cut)
   seq_dict_cut[id] = re.sub(r'([AG])(AATT[CT])',r'\1^\2', seq)
   print('\n',seq_dict_cut[id])
   restr_frag = seq_dict_cut[id].split("^")
   restr_frag_sort = sorted(restr_frag,key=len, reverse=True)
print('\n',restr_frag_sort)
