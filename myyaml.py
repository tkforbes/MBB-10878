#!/usr/bin/env python

# going to use this source file for some sandbox code. It will be thrown away.
#
# The other thing that is going on: I am learning to use git and github. So, while this all appears messy, the true intention is to become familiar with the tools, confront some hurdles and make some mistakes but ultimately get experience.

import yaml
with open("config.yaml", 'r') as stream:
        try:
                    cfg = yaml.safe_load(stream)
                    xusers= cfg['excluded_users']
                    print(cfg)
                    print()
                    print(xusers)
                    print()
                    for n in xusers:
                        print(n)

                    print(xusers[2])

        except yaml.YAMLError as exc:
                    print(exc)
