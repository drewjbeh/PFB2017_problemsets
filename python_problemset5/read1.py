#!/usr/bin/env python3

# Read a file, covert to upper and write

input_file = open('Python_05.txt','r')
output_file = open('Python_05_uc.txt','w')

for line in input_file:
   line = line.rstrip()
   output_file.write(line.upper())

input_file.close()
print("Wrote file to 'Python_05_uc.txt'")
