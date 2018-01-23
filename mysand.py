#!/usr/bin/env python

import sys
import os
import subprocess

#subprocess.call(["ls", "-lh"])
#subprocess.call("exit 1", shell=True)
#subprocess.check_call(["ls", "-l"])
#rc= subprocess.run( ["exit 1"], shell=True, check=False )
#proc= subprocess.run( ["/usr/bin/wc", "vali_guid.py"], stdout=subprocess.PIPE, shell=False, check=False )

proc= subprocess.check_output( ["grep", "in", "myfile.txt"], shell=False )

print(proc.decode("utf-8").strip())

with os.popen('ps -ef') as pse:
  for line in pse:
    print( line.strip() )


#while True:
#  print(proc.stdout)
#  break
#  line = proc.stdout.readline()
#  print(line)
#  if line != '':
    #the real code does filtering here
#    print ("test:", line.rstrip())
#  else:
#    break

#print(rc)
#print(rc.returncode)
