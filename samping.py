from samp_client.client import SampClient
import sys
import threading

ip = input("IP : ")
udp = input("port : ")

def CUDP(ip, port):
    while True:
        with SampClient(ip, port, rcon_password="jomblo123") as client:
            while True:
                client.connect()

CUDP(ip, udp)
