#!/usr/bin/env python3

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }
print('REM Configure access vlans \n')
for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
print('\nREM Configure trunk vlans\n')
for inf, vln in fast_int['trunk'].items():
    print('interface FastEthernet'+inf)
    for cmd in trunk_template:
        if cmd.endswith('trunk allowed vlan'):
            a=vln[0]
            b=','.join(vln[1:])
            c=a+' '+b
            print(' {} {}'.format(cmd,c))
        else:
            print(' {}'.format(cmd))
