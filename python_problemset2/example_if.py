#!/usr/bin/env python3

import sys

test_num = float(sys.argv[1])

if test_num > 0:
   if test_num < 50:
      if test_num % 2 == 0:
         print("Number is positive, smaller than 50 and even")
      else:
         print("Number is positive, smaller than 50 and odd")
   elif test_num > 50:
      if test_num % 3 == 0:
         print("Number is positive, larger than 50 and divisible by 3")
      else:
         print("Number is positive, larger than 50 and not divisible by 3")
   else:
      print("Number is exactly 50")
elif test_num < 0:
   print("Number is negative")
else:
   print("Number is 0")
