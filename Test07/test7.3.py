#!/usr/bin/env python3
print('Test 7.3')
input=open('CAM_table.txt','r')
for line in input:
    if len(line)>17:
        if (line[12]=='.') and line[17]=='.':
            print(line.rstrip())
input.close()
