
# Usage ./MAVLink_MSG_Decoder <USB_PORT> <BAUDRATE>
#  OR
# Usage ./MAVLink_MSG_Decoder <USB_PORT> <BAUDRATE>  > logfile

#!/usr/bin/python

import sys , re

from pymavlink import mavutil

invalid_crc = "invalid MAVLink"

m = mavutil.mavlink_connection(sys.argv[1],baud=int(sys.argv[2]))

COUNT = 0

while True:

   mesg = m.recv_msg()

   if mesg != None:
       mesg = str(mesg)
       mesg = mesg.strip()
#       print mesg               # Uncomment this to LOG messages
       if (re.search(invalid_crc,mesg)):
         COUNT += 1
#         print msg
         print "ERRONEOUS PACKETS " + str(COUNT)
         
#print COUNT





