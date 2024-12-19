#!/bin/python3

import os
import sys

filename = sys.argv[1]

with open(filename) as inf:
    for line in inf.readlines():
        line = line[:-1].upper() + '\r\n'
        print(line, end='')
    
