#!/usr/bin/env python

import mavutil


msg_desc = pymavlink.mavutil.mavlink_connection("udp::14555", dialect="array_test")

while True:
   msg = msg_desc.recv_msg()
   if msg is not None:
   print(msg)


