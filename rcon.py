#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""usage: rcon.py host[:port] password command"""

import sys
import socket

def main():
    if len(sys.argv) < 4:
        print __doc__
        return 2
    host = sys.argv[1].split(':')
    port = 27733 if len(host) < 2 else int(host[1])
    host = host[0]
    password = sys.argv[2]
    command = ' '.join(sys.argv[3:])
    packet = '\xff\xffrcon\xff%s\xff%s\xff' % (password, command)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(packet, (host, port))
    data = sock.recv(20480)[12:]
    sys.stdout.write(data)
    sock.close()
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
