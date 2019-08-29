## Spawns a tty shell with bash in order to use tools like vi, or cmds like sudo or passwd
## Ripped from the basic tty shell spawn (example found here: https://metahackers.pro/spawing-tty-shells/)
## Author - Eoin Finney

import pty
def main():
  pty.spawn('/bin/bash')
