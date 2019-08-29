#
# Created by Eoin Finney & Ciaran Meade
# Contact info:
# Eoin   -> B00093420@mytudublin.ie | s0meRand0mDud3@protonmail.com
# Ciaran -> B000XXXXX@mytudublin.ie
#
# This tool is designed for use with Kali Linux only. Kali is available here: (https://www.kali.org/)
#
# Layout for this tool borrowed from Lee Baird's Discover Tool (https://github.com/leebaird/discover)
##############################################################################################################
import os, subprocess, sys, time

homeDirectory = os.environ['HOME']

##############################################################################################################

def banner():
    print(" *** DO SOMETHING ***")

##############################################################################################################

def error():
    print(" ** Invalid Choice or Entry **")
    time.sleep(2)

##############################################################################################################

def exit():
    print("Thanks for using me!")
    sys.exit(0)

##############################################################################################################

def main():

    print("Please select the tool you desire.")
    print("[A] MAC Changer\n[B] Network "
          "Scanner\n[C] ARP Spoofer\n[D] Packet Sniffer\n[E] Metasploit - Python\n[F] Reverse TCP Shell\n[G] TTY Shell\n[H] DNS Notes\n[I] HTTP Scanners Notes\n[J] Netcat Notes\n[K] Linux PrivEsc Notes\n[L] Windows PrivEsc Notes\n[Z] Exit")
    choice = input("Please choose an option from above: ").upper()
    print("\n")
    if choice == "A":
        import mac_changer
        mac_changer.main()
    elif choice == "B":
        import network_scanner
        network_scanner.main()
    elif choice == "C":
        import arp_spoofer
        arp_spoofer.main()
    elif choice == "D":
        import packet_sniffer
        packet_sniffer.main()
    elif choice == "E":
        import meta_sploit
        meta_sploit.main()
    elif choice == "F":
        import python_reverse_tcp_shell
        python_reverse_tcp_shell.main()
    elif choice == "G":
        import meta_sploit
        meta_sploit.main()
    elif choice == "H":
        file = open("notes/dns-notes.txt")
        print(file.read())
    elif choice == "I":
        file = open("notes/http_scanners.txt")
        print(file.read())
    elif choice == "J":
        file = open("notes/netcat_commands.txt")
        print(file.read())
    elif choice == "K":
        file = open("notes/linux_priv_esc_notes.txt")
        print(file.read())
    elif choice == "L":
        file = open("notes/windows_priv_esc_notes.txt")
        print(file.read())
    elif choice == "Z":
        exit()
    else:
        error()

