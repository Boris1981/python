#!/usr/bin/env python3
print('Test 9.1')

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }


access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']


def function(args):
    '''Function for functionality'''
    interfaces=list(args.keys())
    vlans=list(args.values())
    output=[]
    z=0
    for i in interfaces:
        print(i)
        output.append(i)
        for m in access_template:
            if m.endswith('vlan'):
                d=m + ' ' + str(vlans[z])
                z+=1
                output.append(d)
            else:
                output.append(m)
    return output
    

print(function(access_dict))
