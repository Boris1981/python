#!/usr/bin/env python3
from sys import argv
print('Test 7.2')
try:
    confin=argv[1]
    confout=argv[2]
except IndexError:
    print('Not enouth arguments')
try:
    input=open(confin, 'r')
    output=open(confout, 'w')
    ignore = ['duplex', 'alias', 'Current configuration']
# Main code here
    for line in input:
        #if not line.startswith('!'):
            count=0
            for ign in ignore:
                if line.count(ign)!=0:
                    count +=1
            if count == 0:
                #print(line.strip())
                output.write(line)
    input.close()
    output.close()
except FileNotFoundError:
    print('There is no config file '+config)
except NameError:
    print('Please, input inbound and outbound filenames')

