from samp_client.client import SampClient
import sys
import threading

ip = sys.argv[1]
udp = sys.argv[2]

def CUDP(ip, port):
    while True:
        with SampClient(ip, port, rcon_password="jomblo123") as client:
            while True:
                client.connect()

CUDP(ip, udp)