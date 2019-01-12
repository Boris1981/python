#!/usr/bin/env python3
print('Test 7.3')
input=open('CAM_table.txt','r')
outlist=[]
for line in input:
    if len(line)>17:
        if (line[12]=='.') and line[17]=='.':
            #print(line.rstrip())
            outlist.append(line)
outlist.sort()
input.close()
for line in outlist:
    print(line.rstrip())

