#!/usr/bin/env python3

# Create tuple for seqs and lengths and print info

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

seq_tup = [(len(oligo), oligo) for oligo in seqs]

count = 0
for seq, length in seq_tup: #this kind of loop splits the tuple pair
   count += 1
   print (count, seq, length, sep = '\t')
