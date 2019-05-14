num = int(input('Dev num (0..1): '))

import usb.core
import usb.util

file = open('IDs.txt', 'r')
lines = file.readlines()
file.close()

dev = list(usb.core.find(find_all=True, idVendor=int(lines[0][10:-1],16),\
                         idProduct=int(lines[1][11:-1],16)))

while len(dev)==0:
    list(usb.core.find(find_all=True, idVendor=int(lines[0][10:-1],16),\
                         idProduct=int(lines[1][11:-1],16)))

dev[num].set_configuration()
#dev[1].set_configuration()



while 1:

    input('Flash?')

    file = open('Sorted.txt', 'r')
    for line in file:

        packet = ((int(line[-5:],16)),
                 (int(next(file)[-3:])),
                 (int(next(file)[-7:],16)),
                 (int(next(file)[-8:-2],16)),
                 (int(next(file)[-2:])))
        
        dev[num].ctrl_transfer(packet[0],packet[1],packet[2],packet[3],packet[4])
        #dev[1].ctrl_transfer(packet[0],packet[1],packet[2],packet[3],packet[4])
        
    file.close()

