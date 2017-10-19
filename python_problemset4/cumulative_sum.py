#!/usr/bin/env python3

values = [101,2,15,22,95,33,2,27,72,15,52]
values.sort()
odd_cum = 0
even_cum = 0

for num in values:
   if num % 2 == 0:
      even_cum += num
   else:
      odd_cum += num

print('Cumulative of even:',even_cum)
print('Cumulative of odd:', odd_cum)
