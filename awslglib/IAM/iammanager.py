#!/usr/bin/env python

import time
import re
import os
import boto.iam
import logging

class IamManager(object):

  def __init__(self,object,name):
    self.conn = self.__get_boto_conn(object)
    self.new = True
    self.name = name


  def __get_boto_conn(self,object):
    #if region not in self.boto_conns:
    conn = boto.connect_iam(aws_access_key_id=object._iniconfigs['AWS_ACCESS_KEY'],
                            aws_secret_access_key=object._iniconfigs['AWS_SECRET_KEY'])
    if not conn:
      print "Connection cannot be established with AWS, check your region and credentials please"
      raise

    return conn


  def create_user(self):

    if self.validate_name():

      try:
        self.conn.create_user(self.name)
        user = self.conn.create_access_key(self.name)
        self.secretID = user.access_key_id
        self.secterKey = user.secret_access_key

      except Exception:
        self.new = False
        logging.info("User created: " + self.name)
        pass

      self.add_environment()


  def attach_group(self):
      if self.env == 'stg':
          self.conn.add_user_to_group('g_sqs_stg',self.name)
      elif self.env == 'pro':
          self.conn.add_user_to_group('g_sqs_pro',self.name)



  def validate_name(self,):
      if self.name.startswith('sqs_stg-') or self.name.startswith('sqs_pro-'):
        return True
      else:
        logging.critical("This user does not match Letgo naming connvention, name must start by sqs_ENV-*. Aborting!")
        sys.exit(1)

  def show_secretID(self):
      if self.new:
        return self.secretID
      else:
        return None


  def show_secretKey(self):
      if self.new:
        return self.secterKey
      else:
        print "This user was already created and for security reasons I cannot access to his keys"
        return None

  def show_user_name(self):
      return self.name

  def add_environment(self):
    if self.name.startswith('sqs_stg-'):
        self.env = 'stg'

    elif self.name.startswith('sqs_pro-'):
        self.env = 'pro'


  def is_a_new_user(self):
    return self.new
