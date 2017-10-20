#!/usr/bin/env python3

import re

# Find header and description in sequence fasta file

sequences = open('Python_06.fasta','r')
for line in sequences:
   header_search = re.search(r"^(>\S+)\s?(.*)",line)
   if header_search:
      print(header_search.group(1) + ":extracted seq name", header_search.group(2) + ":extracted description")

      
