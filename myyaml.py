#!/usr/bin/env python

# going to use this source file for some sandbox code. It will be thrown away.
#
# The other thing that is going on: I am learning to use git and github. So, while this all appears messy, the true intention is to become familiar with the tools, confront some hurdles and make some mistakes but ultimately get experience.

import yaml

with open("config.yaml", 'r') as stream:
        try:
                    print(yaml.load(stream))
        except yaml.YAMLError as exc:
                    print(exc)
