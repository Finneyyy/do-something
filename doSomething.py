#!/usr/bin/env python
#
# By Eoin Finney & Ciaran Meade
# Contact info:
# Eoin   -> B00093420@mytudublin.ie | s0meRand0mDud3@protonmail.com
# Ciaran -> B000XXXXX@mytudublin.ie
#
# This tool is designed for use with any linux system, but mainly for Kali (https://www.kali.org/)
#
# Layout for this tool ripped from Lee Baird's Discover Tool (https://github.com/leebaird/discover)
##############################################################################################################

import os
import subprocess
import sys
import time


# Global Variables
Long="==================================================================================="
medium="========================================="
short="====================="

homeDirectory= os.environ['HOME']

##############################################################################################################

def banner():
    print
    print


##############################################################################################################

def error():
    print("")
    print Green.format(medium)
    print()
    print Green.format("         *** Invalid choice or entry. ***")
    print
    print Green.format(medium)
    time.sleep(2)

##############################################################################################################

def main():
	while True:
		option=menu()
		if option=="1":
			exec("scripts/network_scanner.py")
		elif option=="2":
			exec
