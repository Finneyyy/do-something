import scapy.all as sc
import argparse


def scan(ip):
    arping_request = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arping_request_broadcast = broadcast/arping_request
   
    # send and recieve. allows us to send packets with a custom Ether part. When it gets 
    # a response it will return 2 variables.
    # timeout waits a certain amount of time, if no response comes it justs moves on.
    # verbose gets rid of the c hunk of writing at the top.
    answered_packets, unanswered_packets = sc.srp(arping_request_broadcast, timeout=1, verbose=False)
    
    print("\nIP\t\t\t\t\tMAC Address\n----------------------------------------------------------------")
    for packet in answered_packets:
        # printing ip's
        print(packet[1].psrc + "\t\t\t\t" + packet[1].hwsrc)

def main():
        target = input("Enter the IP address or the range of your target: ")
        # options = get_arguments()
        result = scan(target)
        print(result)


