#!/usr/bin/python3

import socket
import sys
import os

UDP_IP_ADDRESS = "service.stack"
UDP_PORT_NO = 6789

if len(sys.argv) > 1:
    Packets = int(sys.argv[1])
else:
    Packets = 10

print("Sending " + str(Packets) + " packets.")

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while(Packets > 0):
    packet = os.urandom(128)
    clientSock.sendto(packet, (UDP_IP_ADDRESS, UDP_PORT_NO))
    Packets = Packets-1
