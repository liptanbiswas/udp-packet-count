#!/usr/bin/python3

import socket

UDP_IP_ADDRESS = "0.0.0.0"
UDP_PORT_NO = 6789

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
PACKET_COUNT = 0

while True:
    data, addr = serverSock.recvfrom(1024)
    PACKET_COUNT = PACKET_COUNT + 1
    print ("Received " + str(PACKET_COUNT) + " Packets as of now.")
