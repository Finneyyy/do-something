import subprocess
import re


def change_mac_addr():
    # interface = input("Enter the interface you would like to change the MAC Address of: ")
    # new_mac_addr = input("Enter the new MAC Address you would like: ")

    print("\n** Changing the MAC Address for " + interface + " to " + new_mac_addr)

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac_addr])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_current_mac():
    result = subprocess.check_output(["ifconfig", interface])
    # print(result)
    
    mac_addr_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result.decode('utf-8'))
    
    if mac_addr_res:
        return mac_addr_res.group(0)
    else:
        print("[*] Could not read MAC Address")


def main():
    interface = input("Enter the interface would you like to change the MAC Address of: ")
    new_mac_addr = input("Enter the new MAC Address you would like: ")
    print("\n")
    current_mac_addr = get_current_mac()
    print("Current MAC address = " + str(current_mac_addr))
    change_mac_addr()
    current_mac_addr = get_current_mac()
    if current_mac_addr  == new_mac_addr:
        print("\n** MAC address has been changed to: " + current_mac_addr)
    else:
        print("\n** MAC address did not get changed!")



# 08:00:27:1b:e6:7e

