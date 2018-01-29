#!/usr/bin/env python

# a program to report on the uid and gid states of users on the biocluster.

# 1. create a list of users from somewhere, possibly /etc/passwd

# 2. for each user in the list, get its gid and uid on biocluster

# 3. for each user in the list, ask its gid and uid from active directory (samba, wbinfo)

# domain appears to be AAFC-AAC, according to samba.

# 4. report on the exceptions in the list e.g. biocluster gid != AD gid

# 5. exit with a meaningful return code. zero for fully-matched.

#
# program begins here
#
from config import *

cfg = Config()

## might want some sanity check here. 
## it would not be normal to have too few exclusions; that might indicate something
## is wrong with the configuration.

# build a list of users of interest
import pwd
users=[]
for i, u in enumerate(pwd.getpwall()):

  # ignore excluded users
  if u.pw_name not in cfg.excluded_users():
    users.append(u)

print('users:', users)

# request the user details from AD based on user name

# user found in AD?

# uid equal in AD?

# gid equal in AD?

# print reports
