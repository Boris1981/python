#!/usr/bin/env python3

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
for cmac in mac:
    mac_cisco.append(cmac.replace(':','.'))
print(mac_cisco)
