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
      config= yaml.safe_load(stream)
      excluded_users[:] =config['excluded_users']
    except yaml.YAMLError as exc:
      print(exc)

# load excluded users from configuration
excluded_users=[]
loadConfig(excluded_users)

# get the list of users from the system
import pwd
system_users= pwd.getpwall()

# build a list of retained users by skipping any that are in the list of exclusions
retained_users=[]
for n, j in enumerate(system_users):
  if j.pw_name not in excluded_users:
    retained_users.append(j)

print('users:', retained_users)


