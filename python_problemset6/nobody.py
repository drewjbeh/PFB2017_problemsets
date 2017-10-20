#!/usr/bin/env python3

import re

# Regex on Nobody

poem = open('Python_06_nobody.txt','r')
replace = open('Gabriella.txt','w')

line_num = 0
print("Start","End","Line",sep="\t")

for line in poem:
   line_num += 1
   for match in re.finditer("Nobody",line):
       print(match.start(), match.end(), line_num,sep="\t")
   output = re.sub("Nobody","Gabriella",line)
   replace.write(output)

poem.close()
replace.close()
