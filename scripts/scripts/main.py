print("Please select the tool you desire.")
print("[A] MAC Changer\n[B] Network Scanner\n[C] ARP Spoofer\n[D] Packet Sniffer")
choice = input("plz choose from above: ").upper()
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
