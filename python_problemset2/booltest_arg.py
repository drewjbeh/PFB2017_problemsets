#!/usr/bin/env python3

#Test if a number specified as arg is True

import sys

num = float(sys.argv[1]) # Needs to be float otherwise it remains a str ans is always True

if bool(num):
   print("This is True")
else:
   print("This is False")
