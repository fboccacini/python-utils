#!/usr/bin/python

# Hex to char converter

import sys

if len(sys.argv) < 2:
    string = input('Hex string (space separated): ')
    splt = string.split(' ')
else:
    splt = sys.argv[1:]

print('')

new_str = ''

for char in splt:
    print(char, int(char,16), chr(int(char,16)), sep=' - ')
    new_str += chr(int(char,16))
print('\n')

print(new_str)
