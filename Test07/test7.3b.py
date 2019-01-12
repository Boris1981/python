#!/usr/bin/env python3
from sys import argv
print('Test 7.3b')
try:
    vlan=argv[1]
except IndexError:
    print('Add Vlan number')
input=open('CAM_table.txt','r')
outlist=[]
for line in input:
    if len(line)>17:
        if (line[12]=='.') and line[17]=='.':
            #print(line.rstrip())
            outlist.append(line)
outlist.sort()
input.close()
count=0
for line in outlist:
    if line.strip().startswith(vlan):
        count +=1
        print(line.rstrip())
if count==0:
    print('Vlan '+vlan+' is not avaiable')

