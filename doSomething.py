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
Long="==============================================================================================================================="
medium="=================================================================="
short="========================================"

Blue="\033[01;34m{0}\033[00m"             # Bash colour codes
Red="\033[01;31m{0}\033[00m"
Yellow="\033[01;33m{0}\033[00m"
Green="\033[01;32m{0}\033[00m"

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
    print Green.format("                *** Invalid choice or entry. ***")
    print
    print Green.format(medium)
    time.sleep(2)




