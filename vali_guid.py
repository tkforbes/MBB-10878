#!/usr/bin/env python

# a program to report on the uid and gid states of users on the biocluster.

# 1. create a list of users from somewhere, possibly /etc/passwd

# 2. for each user in the list, get its gid and uid on biocluster

# 3. for each user in the list, ask its gid and uid from active directory (samba, wbinfo)

# domain appears to be AAFC-AAC, according to samba.

# 4. report on the exceptions in the list e.g. biocluster gid != AD gid

# 5. exit with a meaningful return code. zero for fully-matched.

import sys
import os
import subprocess

#subprocess.call(["ls", "-lh"])

#subprocess.call("exit 1", shell=True)

#subprocess.check_call(["ls", "-l"])
#rc= subprocess.run( ["exit 1"], shell=True, check=False )
#proc= subprocess.run( ["/usr/bin/wc", "vali_guid.py"], stdout=subprocess.PIPE, shell=False, check=False )
proc= subprocess.run( ["/bin/cat", "myfile.txt"], stdout=subprocess.PIPE, shell=False, check=False )

#print(proc)

while True:
  print(proc.stdout)
  break
#  line = proc.stdout.readline()
#  print(line)
#  if line != '':
    #the real code does filtering here
#    print ("test:", line.rstrip())
#  else:
#    break

#print(rc)
#print(rc.returncode)
