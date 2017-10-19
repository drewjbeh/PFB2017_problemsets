#!/usr/bin/env python3

import sys
import random

seq = sys.argv[1]

for i in range(len(seq)):
   pos1 = random.randrange(0, len(seq))
   pos2 = random.randrange(0, len(seq))
   seq_list = list(seq)
   seq_list[pos1], seq_list[pos2] = seq_list[pos2], seq_list[pos1]
   seq = ''.join(seq_list)
print(seq)
