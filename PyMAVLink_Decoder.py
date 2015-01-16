#!/usr/bin/env python

import mavutil , re

msg_desc = pymavlink.mavutil.mavlink_connection("udp::14555", dialect="array_test")

count = 0

while True:

   msg = msg_desc.recv_msg()

   if msg is not None:

     bad_CRC = re.search("BAD CRC",msg)

     if bad_CRC is not None:
           
         count += 1
         display = "PACKETS WITH BAD CRCs " + str(count)
         print display
       



