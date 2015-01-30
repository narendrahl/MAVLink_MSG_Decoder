

#!/usr/bin/python

import sys , re

from pymavlink import mavutil

#PORT = raw_input("INPUT PORT: ")

#BAUDRATE = raw_input("INPUT BAUDRATE: ")

invalid_crc = "BAD_DATA"
#invalid_crc = "invalid MAVLink"

master = mavutil.mavlink_connection(sys.argv[1],baud=int(sys.argv[2]))

COUNT = 0

while True:

   msg = master.recv_msg()

   if msg != None:
       msg = str(msg)
       msg = msg.strip()
       print msg
       if (re.search(invalid_crc,msg)):
         COUNT += 1
#         print msg
         print COUNT

#print COUNT





