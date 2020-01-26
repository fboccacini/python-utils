#!/usr/bin/python

# Hex to char converter, version 1.2

import sys

verbose = True
splt = []

# Check options and codes
for opt in sys.argv:

    try:
        # If it's a valid character hex, apend to splt
        chr(int(opt,16))
        splt.append(opt)
    except:
        # Else check for known options
        if opt == '-s':
            verbose = False

# If string wasn't as argument ask for one
if len(splt) < 1:
    string = input('Hex string (space separated): ')
    splt = string.split(' ')

new_str = ''

# Loop through codes and add to the string
for char in splt:
    if verbose:
        print(char, int(char,16), chr(int(char,16)), sep=' - ')
    new_str += chr(int(char,16))

print(new_str)
