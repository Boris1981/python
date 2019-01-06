#!/usr/bin/env python3
while True:
    ip_octet_check=0
    ip=input('Input ip-address as XXX.XXX.XXX.XXX: ')
    ip_list=ip.split('.')

    for octet in ip_list:
        if octet.isdigit() and int(octet)>=0 and int(octet)<=255:
            #print(octet)
            ip_octet_check += 1
            #print('ip_octet_check='+ip_octet_check)
    if ip_octet_check != 4:
        print('Incorrect IPv4 address')
        
    else:
        if int(ip_list[0])<=223 and int(ip_list[0])>0:
            print('unicast')
        elif int(ip_list[0])<=239 and int(ip_list[0])>=224:
            print('multicast')
        elif int(ip_list[0])==255 and int(ip_list[1])==255 and int(ip_list[2])==255 and int(ip_list[3])==255:
            print('local broadcast')
        elif int(ip_list[0])==0 and int(ip_list[1])==0 and int(ip_list[2])==0 and int(ip_list[3])==0:
            print('unassigned')
        else:
            print('unused')
        break
print('Mission completed')
