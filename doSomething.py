#
# By Eoin Finney & Ciaran Meade
# Contact info:
# Eoin   -> B00093420@mytudublin.ie | s0meRand0mDud3@protonmail.com
# Ciaran -> B000XXXXX@mytudublin.ie
#
# This tool is designed for use with any linux system, but mainly for Kali (https://www.kali.org/)
#
# Layout for this tool borrowed from Lee Baird's Discover Tool (https://github.com/leebaird/discover)
##############################################################################################################
import os
import subprocess
import sys
import time

# Global Variables
lineLong = "========================================================="
lineMedium = "============================================"
lineShort = "============================="

homeDirectory = os.environ['HOME']


##############################################################################################################

def banner():
    print(" *** DO SOMETHING ***")


#############################################################################################################

def error():
    print("")
    print(lineMedium)
    print("")
    print("                *** Invalid choice or entry. ***")
    print("")
    print(lineMedium)
    time.sleep(2)


#############################################################################################################

def exit():
    print("Thanks for using me!")
    sys.exit(0)


#############################################################################################################

def lists():
    # Just a placeholder to figure out how to open text files
    exit()


#############################################################################################################

def main():
    while True:
        option = menu()
        if option == "1":
            exec("/scripts/mac_changer.py")
        elif option == "2":
            exec("/scripts/meta_sploit.py")
        elif option == "3":
            exec("/scripts/network_scanner.py")
        elif option == "4":
            exec("/scripts/packet_sniffer.py")
        elif option == "5":
            exec("/scripts/python_reverse_tcp_shell.py")
        elif option == "6":
            exec("/scripts/spawn_tty_shell.py")
        elif option == "10":
            file = open("notes/dns-notes.txt")
            print(file.read())
        elif option == "11":
            file = open("notes/http_scanners.txt")
            print(file.read())
        elif option == "12":
            file = open("notes/netcat_commands.txt")
            print(file.read())
        elif option == "13":
            file = open("notes/linux_priv_esc_notes.txt")
            print(file.read())
        elif option == "14":
            file = open("notes/windows_priv_esc_notes.txt")
            print(file.read())
        elif option == "85":
            exec("scripts/windows_stuff/sweep_pass.bat")
        elif option == "99":
            print("See ya next time!")
            sys.exit(0)
        else:
            error()


#############################################################################################################

def menu():
    os.system("clear")
    banner()

    # Create Folder if one does not exist
    if not os.path.exists(homeDirectory + "/do_something/data"):
        os.makedirs(homeDirectory + "/do_something/data")

    print("Spoofers")
    print("1. Mac Changer")
    print("")
    print("Metasploit")
    print("2. Metasploit")
    print("")
    print("SCANNER")
    print("3. Network Scanner")
    print("")
    print("Sniffers")
    print("4. Packet Sniffer")
    print("")
    print("Shells")
    print("5. Reverse TCP Shell (Python)")
    print("6. Spawn a tty shell")
    print("")
    print("Notes on scanners, Privilege Escalation, Netcat and DNS")
    print("10. DNS Notes")
    print("11. HTTP Scanners")
    print("12. Netcat Command List")
    print("13. Linux PrivEsc Notes")
    print("14. Windows PrivEsc Notes")
    print("")
    print("Windows Tools")
    print("85. Search for files beginning with pass")
    print("")
    print("EXIT")
    print("99. Exit the program")
    print("")
    return input("Choice: ")

    #############################################################################################################


if __name__ == '__main__':
    main()
