#!/usr/bin/env python

# a program to report on the uid and gid states of users on the biocluster.

# 1. create a list of users from somewhere, possibly /etc/passwd

# 2. for each user in the list, get its gid and uid on biocluster

# 3. for each user in the list, ask its gid and uid from active directory (samba, wbinfo)

# domain appears to be AAFC-AAC, according to samba.

# 4. report on the exceptions in the list e.g. biocluster gid != AD gid

# 5. exit with a meaningful return code. zero for fully-matched.



# load the list of excluded users from the YAML config file
def loadConfig( ):
  import yaml
  excluded_users= []  
  with open("config.yaml", 'r') as stream:
    try:
      config= yaml.safe_load(stream)
      excluded_users[:] =config['excluded_users']
    except yaml.YAMLError as exc:
      print(exc)

    return excluded_users


#
# program begins here
#

# load excluded users from configuration
excluded_users= loadConfig( )

## might want some sanity check here. 
## it would not be normal to have too few exclusions; that might indicate something
## is wrong with the configuration.

# build a list of users of interest
import pwd
users=[]
for n, j in enumerate(pwd.getpwall()):

  # ignore excluded users    
  if j.pw_name not in excluded_users:
    users.append(j)

print('users:', users)

# request the user details from AD based on user name

# user found in AD?

# uid equal in AD?

# gid equal in AD?

# print reports
