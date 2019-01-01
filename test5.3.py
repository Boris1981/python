#!/usr/bin/env python3
print('Test 5.3 _NOT_COMPLETED')

mode=input('Enter interface mode (access/trunk): '.strip())
#interface=input('Enter interface type and number: ')
#vlan=input('Enter vlan(s): ')

access_template=['switchport mode access',
		 'switchport access vlan {}',
		 'switchport nonegotiate',
 		 'spanning-tree portfast',
		 'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q',
		  'switchport mode trunk',
		  'switchport trunk allowed vlan {}']

template=access_template

print('-'*30)
#print('interface '+interface)
print(template)
