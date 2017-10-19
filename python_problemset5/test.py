#!/usr/bin/env python3

import sys

input = open(sys.argv[1],'r')
output = open(sys.argv[2],'w')

for line in input:
   line.rstrip()
   output.write(line)
