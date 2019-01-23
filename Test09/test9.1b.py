#!/usr/bin/env python3
print('Test 9.1a')

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }


access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

port_security=['switchport port-security maximum 2',
               'switchport port-security violation restrict',
               'switchport port-security']

def function(intf, psecurity=False):
    '''Creating config for interfaces in access mode'''
    interfaces=list(intf.keys())
    vlans=list(intf.values())
    outdict=dict.fromkeys(interfaces, [])
    z=0
    for i in interfaces:
        output=[]
        for line in access_template:
            if line.endswith('vlan'):
                d=line + ' ' + str(vlans[z])
                z+=1
                output.append(d)
            else:
                output.append(line)
        if psecurity:
            output.extend(port_security)
        
    outdict[i].extend(output)
    return outdict
    

print(function(access_dict,psecurity=True))
