#!/usr/bin/env python3

print('Test 5.2 \n ')

london_co	=	{
				'r1'	:	{
				'location':	'21	New	Globe	Walk',
				'vendor':	'Cisco',
				'model':	'4451',
				'ios':	'15.4',
				'ip':	'10.255.0.1'
				},
				'r2'	:	{
				'location':	'21	New	Globe	Walk',
				'vendor':	'Cisco',
				'model':	'4451',
				'ios':	'15.4',
				'ip':	'10.255.0.2'
				},
				'sw1'	:	{
				'location':	'21	New	Globe	Walk',
				'vendor':	'Cisco',
				'model':	'3850',
				'ios':	'3.6.XE',
				'ip':	'10.255.0.101',
				'vlans':	'10,20,30',
				'routing':	True
				}
}
list0=list(london_co.keys())
name=input('Enter name of device ('+','.join(list0)+'): ' )

list1=list(london_co[name].keys())

#print('Enter parameter name'+','.join(list1) + ':' )
#print(list(london_co[name].keys()))

parm=input('Enter parameter name (' + ','.join(list1) + '): ')

print(london_co[name].get(parm, 'This parameter is not avaiable'))
