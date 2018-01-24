#!/usr/bin/env python

# going to use this source file for some sandbox code. It will be thrown away.
#
# The other thing that is going on: I am learning to use git and github. So, while this all appears messy, the true intention is to become familiar with the tools, confront some hurdles and make some mistakes but ultimately get experience.

#import sys
#import os
import pwd
import grp
#import subprocess

def printAllUsers( ):
  print("")
  for u in pwd.getpwall():
    print(u[0], u[2])


def printUserGroups( ):
  print("")
  for p in pwd.getpwall():
    print ( p[0], grp.getgrgid(p[3])[0] )

def printUser(n):
  print("")
  uid = pwd.getpwuid(n)
  print(uid)
  print(uid.pw_name)

def printUserNam(name):
  print("")
  nam = pwd.getpwnam(name)
  print(nam)


#printUser(1000)
#printUserNam('root')
printAllUsers( )
#printUserGroups( )
