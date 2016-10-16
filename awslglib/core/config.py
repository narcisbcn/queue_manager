import boto
import ConfigParser
import os
import logging




class Config:

  def __init__(self, override_values={}):
      self.AMS_LOGLEVEL = 'WARNING'
      self._iniconfigs = {}
      self._sources = {}
      self.load_ini()
      self.read_config()

  def load_ini(self):
      config_file_paths = [
          '~/awslglib.ini',
          '/etc/awslglib.ini',
          os.path.realpath(os.path.dirname(__file__) + '/../../defaults.ini'),
      ]

      filename = None
      for filepath in config_file_paths:
          filename = os.path.realpath(os.path.expanduser(filepath))
          if os.path.isfile(filename):
              break
          else:
              filename = None

      if not filename:
          raise NoConfigFile("No config file found in " + " or ".join(config_file_paths))

      self._inifile = filename


  def read_config(self):

      config = ConfigParser.ConfigParser()
      config.optionxform = str
      config.read(self._inifile)

      options = config.options('CONFIG')
      for option in options:
          self._iniconfigs[option] = config.get('CONFIG', option)





