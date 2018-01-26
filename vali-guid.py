#!/usr/bin/env python

# a program to report on the uid and gid states of users on the biocluster.

# 1. create a list of users from somewhere, possibly /etc/passwd

# 2. for each user in the list, get its gid and uid on biocluster

# 3. for each user in the list, ask its gid and uid from active directory (samba, wbinfo)

# domain appears to be AAFC-AAC, according to samba.

# 4. report on the exceptions in the list e.g. biocluster gid != AD gid

# 5. exit with a meaningful return code. zero for fully-matched.

def loadConfig(excluded_users):
  import yaml
  with open("config.yaml", 'r') as stream:
    try:
      cfg= yaml.safe_load(stream)
      excluded_users[:] =cfg['excluded_users']
    except yaml.YAMLError as exc:
      print(exc)

excluded_users=[]
loadConfig(excluded_users)

import pwd
system_users= pwd.getpwall()

retained_users=[]
for n, j in enumerate(system_users):
  if False == (j.pw_name in excluded_users):
    retained_users.append(j)

print('users:', retained_users)


#print(system_users)

#print(excluded_users)
#print('==>', system_users[0].pw_name)
#for n, x in enumerate(excluded_users):
#  if x in l:
#    print(n, x)

#matches = [x for x in excluded_users if  ]

#print(excluded_users)

