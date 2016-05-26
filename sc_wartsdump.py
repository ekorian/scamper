#!/usr/bin/env python3
# 
# Program:      $Id: sc_wartsdump.py 1551 2015-02-11 14:14:09Z rbeverly $
# Author:       Robert Beverly <rbeverly@nps.edu>
# Description:  Parse a binary warts capture according to warts.5
#
import sys
from sc_warts import WartsReader, BinWartsReader
from itertools import *

def wartsdump(bytes): 
  w = BinWartsReader(bytes)

  exported = []
  while True:
    (flags, hops) = w.next()
    if flags == False: break  
    exported.append({"meta":flags, "pkts":hops})
  return exported

if __name__ == "__main__":
  assert len(sys.argv) == 2

  bin_input = False
  if bin_input:
    with open(sys.argv[1], 'rb') as f:
      data = f.read()
    w = BinWartsReader(data, verbose=True)
  else:
    w = WartsReader(sys.argv[1], verbose=True)

  while True:
    (flags, hops) = w.next()
    if flags == False: break
