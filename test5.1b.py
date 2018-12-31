#!/usr/bin/env python3
from sys import argv
ip_net=argv[1]
print(ip_net)
#ip_net=input('input net as ip/mask: \n')
#ip_net='10.95.19.21/10' #Test
ip=ip_net.split('/')[0].split('.')
mask=ip_net.split('/')[1]
ip_bin='{:08b}{:08b}{:08b}{:08b}'.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))
net_bin=ip_bin[0:int(mask)]+'0'*(32-int(mask))
net_bin1=net_bin[0:8]
net_bin2=net_bin[8:16]
net_bin3=net_bin[16:24]
net_bin4=net_bin[24:]
net1=int(net_bin1,2)
net2=int(net_bin2,2)
net3=int(net_bin3,2)
net4=int(net_bin4,2)
print('IP address ' +ip_net+ ' belongs to network: ')
print("{:<8} {:<8} {:<8} {:<8}".format(net1, net2, net3, net4))
print("{:8} {:8} {:8} {:8}".format(net_bin1, net_bin2, net_bin3, net_bin4))

#print("{:8} {:8} {:8} {:8}".format(ip[0],ip[1],ip[2],ip[3])) 
#print('{:08b} {:08b} {:08b} {:08b}'.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))

mask_bin='1'*int(mask)+'0'*(32-int(mask))
mask1=mask_bin[0:8]
mask2=mask_bin[8:16]
mask3=mask_bin[16:24]
mask4=mask_bin[24:]
print('Mask: ')
print("{:<8} {:<8} {:<8} {:<8}".format(int(mask1,2),int(mask2,2),int(mask3,2),int(mask4,2)))
print("{:8} {:8} {:8} {:8}".format(mask1,mask2,mask3,mask4))
