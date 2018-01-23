#!/usr/bin/env python

# going to use this source file for some sandbox code. It will be thrown away.
#
# The other thing that is going on: I am learning to use git and github. So, while this all appears messy, the true intention is to become familiar with the tools, confront some hurdles and make some mistakes but ultimately get experience.

import sys
import os
import pwd
import subprocess

uid = pwd.getpwuid(1000)
print(uid)
nam = pwd.getpwnam('root')
print(nam)
