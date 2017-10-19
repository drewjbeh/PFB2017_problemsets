#!/usr/bin/env python3

# Read fasta and convert sequence to rev compl

original = open("Python_05.fasta","r")
revcompl = open("Python_05_revcompl.fasta","w")
total_seq = ''

for line in original:
   line = line.rstrip()
   if ">" not in line:
      total_seq += line
   else:
      compl = total_seq.replace('A'.upper(),'t'.lower())
      compl = compl.replace('C'.upper(),'g'.lower())
      compl = compl.replace('G'.upper(),'c'.lower())
      compl = compl.replace('T'.upper(),'a'.lower())
      rev_compl = compl[::-1]
      revcompl.write(rev_compl.upper() + '\n')
      revcompl.write(line + '\n')
if len(rev_compl) > 0:
   compl = total_seq.replace('A'.upper(),'t'.lower())
   compl = compl.replace('C'.upper(),'g'.lower())
   compl = compl.replace('G'.upper(),'c'.lower())
   compl = compl.replace('T'.upper(),'a'.lower())
   rev_compl = compl[::-1]
   revcompl.write(rev_compl.upper() + '\n')
original.close()
revcompl.close()

