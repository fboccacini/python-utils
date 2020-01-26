#!/usr/bin/python

# Port scanner v1.0
'''
Usage portscan.py [target address]
    If no target is given own will be used
'''

import sys
import time
import socket

from libs import TCPPacket

# Validates a given IP address
def validate_ip(addr):
    octets = addr.split('.')

    if len(octets) != 4:
        return False

    for octet in octets:
        if int(octet) < 0 or int(octet) > 255:
            return False

    return True

# Get own current address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

target = None

# Check options and targets
if len(sys.argv) > 1:
    if validate_ip(sys.argv[len(sys.argv)-1]):
        target = sys.argv[len(sys.argv)-1]
    else:
        print('Invalid target: ' + sys.argv[len(sys.argv)-1])
        exit(1)

for opt in sys.argv:
    # no options yet
    pass

# If no target is given use own
if target is None:
    target = get_ip()

own_ip = get_ip()
print('Scanning ' + target + ' from ' + own_ip + '..')

for port in range(1,65536):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    info = 'Trying port ' + str(port)
    print(info, end='')
    try:
        reply = s.connect_ex((target, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        print("\b" * len(info), end='')
        print('Port ' + str(port) + ' is open.')
    except:
        print("\b"  * len(info), end='')
    finally:
        s.close()

    # pkt = TCPPacket.TCPPacket(port,65530,target,own_ip,'Blabla')
    # pkt.assemble_tcp_fields()
    # print(pkt.raw)
    # s.sendall(pkt.raw)
    # print(str(s))
    # reply = s.sendall(b'blabla')
    # reply = s.recv(131072) # 131072


    # if reply == 0:
    #     print('Port ' + str(port) + ' is open.' )
    #     time.sleep(1)
    # else:
    #     print('Port ' + str(port) + ' is closed.' )
