#!/usr/bin/env python3

print('Test9.2a')

trunk_dict={'FastEthernet0/1':[10,20],
            'FastEthernet0/2':[11,30],
            'FastEthernet0/4':[17]}

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan']

def generate_trunk_config(trunk):
    ''' 
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    
    tr_keys=[]
    for intr in trunk:
        tr_keys.append(intr)
    result=dict.fromkeys(tr_keys)

    for intr in trunk:
        output=[]
        for line in trunk_template:
            if line.endswith('allowed vlan'):
                addline=line + ' ' + str(trunk[intr]).strip('[]')
                output.append(addline)
            else:
                output.append(line)
        result[intr]=output
    return result

print(generate_trunk_config(trunk_dict))
