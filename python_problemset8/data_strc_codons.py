#!/usr/bin/env python3

import sys
import re

# Take input fasta, read into dict, split into codons and write fasta of codons

class NotValidSeq(Exception):
   pass

try:
   file = sys.argv[1]
   print(file, "provided")
   if not file.endswith(('.fa','.fasta','.nt')):
      raise ValueError("Not a valid file")
   file = open(file,'r')

   output = open('Python_08.codons-frame-1.nt','w')
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
         if re.search("[^ACGTN]+",seq_dict[seq_name]):
            raise NotValidSeq("Invalid sequence")
         
   for seq in seq_dict:
      codons = re.findall(r".{3}", seq_dict[seq])
      seq_dict[seq] = codons # Change seq value in dict to list of codons
      for codon in codons:
         output.write(">" + seq + "\n" + codon + "\n")

   file.close()
   output.close()

except IndexError:
   print("Please provide a file!")
except IOError as ex:
   print("File does not exist:", ex.strerror)
except ValueError:
   print ("Not a valid file format")
except NotValidSeq:
   print("Invalid characters in sequence data")
