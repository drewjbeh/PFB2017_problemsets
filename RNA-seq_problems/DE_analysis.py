#!/usr/bin/env python3

import sys, itertools

DE_file = sys.argv[1]
DE_file = open(DE_file,'r')

FDR_range = [0.05, 0.001, 1e-5, 1e-10, 0]
logFC_range = [1, 2, 3, 4, 5]

params_list = list(itertools.product(FDR_range, logFC_range)))


