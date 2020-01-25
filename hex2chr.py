#!/usr/bin/python

# Hex to char converter, version 1.1

import sys

verbose = True

if len(sys.argv) < 2:
    string = input('Hex string (space separated): ')
    splt = string.split(' ')
else:
    splt = []
    for opt in sys.argv:

        try:
            chr(int(opt,16))
            splt.append(opt)
        except:
            if opt == '-s':
                verbose = False

new_str = ''

for char in splt:
    if verbose:
        print(char, int(char,16), chr(int(char,16)), sep=' - ')
    new_str += chr(int(char,16))

print(new_str)
