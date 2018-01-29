#!/usr/bin/env python

# Config :: loads configuration data and makes it available

class Config(object):

  def __init__(self):

    import yaml
    with open("config.yaml", 'r') as stream:
      try:
        self.config= yaml.safe_load(stream)
      except yaml.YAMLError as exc:
        print(exc)


  def excluded_users(self):
    return self.config['excluded_users']

