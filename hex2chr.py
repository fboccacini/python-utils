#!/usr/bin/python3.7

# Hex to char converter, version 2.0

import sys

verbose = True
reverse = False
spaced = True
rotate = 0

oidx = 0
output = ''

# Check options and codes
for opt in range(1,len(sys.argv)):

    if sys.argv[opt][0] == '-':
        oidx = opt
        for o in range(1,len(sys.argv[opt])):
            if sys.argv[opt][o] == 's':
                verbose = False
            if sys.argv[opt][o] == 'i':
                reverse = True
            if sys.argv[opt][o] == 'u':
                spaced = False
            if sys.argv[opt][o] == 'r': # TODO: implement rotation
                try:
                    rotate = int(sys.argv[opt+1])
                    oidx = opt+1
                except:
                    print('Invalid rotation number.')
                    exit()

string = ''
for s in sys.argv[oidx+1:len(sys.argv)]:
    string += s + ' '

# If string wasn't as argument ask for one
if len(string) < 1:
    if reverse:
        string = input('String: ')
    else:
        string = input('Hex string: ')

if reverse:
    for char in string:
        if verbose:
            print(char, ord(char), format(ord(char), "x"))
        output += format(ord(char), "x")
        if spaced:
            output += ' '
else:
    # Remove spaces
    string = ''.join(string.split(' '))
    # Split string in bytes
    for c in range(0,len(string),2):
        if c > len(string) - 2:
            char = '0' + string[len(string)-1]
        else:
            char = string[c:c+2]

        if verbose:
            print(char, int(char,16), chr(int(char,16)), sep=' - ')
        output += chr(int(char,16))


# Loop through codes and add to the string
# for char in splt:
#     if reverse:
#         if verbose:
#             print(char, ord(char), format(ord(char), "x"))
#         output += format(ord(char), "x") + ' '
#     else:
#         if verbose:
#             print(char, int(char,16), chr(int(char,16)), sep=' - ')
#         output += chr(int(char,16))

print(output)
