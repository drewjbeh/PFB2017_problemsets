#!/usr/bin/env python3

# Count nucleotides in a sequence

import sys

seq = sys.argv[1]
count_dict = {}

for nucl in seq:
   if nucl in count_dict:
     count_dict[nucl] += 1
   else:
     count_dict[nucl] = 1
print(count_dict) 
