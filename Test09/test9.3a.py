#!/usr/bin/env python3

def get_int_vlan_map(cfg):
    '''Функция ожидает в качестве аргумента имя конфигурационного файла
    и возвращает два объекта:
    словарь портов в режиме access, где ключи- номера портов, а значения-
    vlan;
    словарь портов в режиме trunk, где ключи- номера портов, а значения- 
    список разрешенных vlan.
    '''
    access_list={}
    trunk_list={}
    with open(cfg, 'r') as f:
        for line in f:
            if line.strip().startswith('interface FastEthernet'):
                intf=line.strip()
            if line.strip().startswith('switchport mode access'):
                access_list[str(intf)]='1'
            if line.strip().startswith('switchport access'):
                access_list[str(intf)]=line.strip().split()[-1]
            if line.strip().startswith('switchport trunk allowed vlan'):
                trunk_list[str(intf)]=line.strip().split(' ')[4].split(',')
    return access_list, trunk_list
print(get_int_vlan_map('config_sw2.txt'))
