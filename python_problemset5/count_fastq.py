#!/usr/bin/env python3

# Count lines and characters in fastq

fastq = open('Python_05.fastq','r')
line_count = 0
char_count = 0

for line in fastq:
   line_count += 1
   char_count += len(line)

fastq.close()
avg_char = char_count / line_count
print('Total lines:', line_count, '\nTotal characters:',char_count,'\nAverage characters:', avg_char)
