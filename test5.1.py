#!/usr/bin/env python3

ip_net=input('input net as ip/mask: \n')
#ip_net='10.95.10.0/24' #Test
net=ip_net.split('/')[0].split('.')
mask=ip_net.split('/')[1]
print('Network: ')
print("{:8} {:8} {:8} {:8}".format(net[0],net[1],net[2],net[3]))
print('{:08b} {:08b} {:08b} {:08b}'.format(int(net[0]),int(net[1]),int(net[2]),int(net[3])))

mask_bin='1'*int(mask)+'0'*(32-int(mask))
mask1=mask_bin[0:8]
mask2=mask_bin[8:16]
mask3=mask_bin[16:24]
mask4=mask_bin[24:]
print('Mask: ')
print("{:<8} {:<8} {:<8} {:<8}".format(int(mask1,2),int(mask2,2),int(mask3,2),int(mask4,2)))
print("{:8} {:8} {:8} {:8}".format(mask1,mask2,mask3,mask4))
