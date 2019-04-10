# udp-packet-count

UDP Client Server program to count the number of packets received. Useful in debugging packet loss in network.

### Server

Run `python3 server.py` on recipient server.

### Client

Edit `UDP_IP_ADDRESS` in `client.py` to the IP address or hostname of recipient server.

Run `python3 client.py <number of packets>`. This program will send packets of 128 bytes in each message. Compare the number of sent packets and received packets to check if you lost any message.
