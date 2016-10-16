#!/usr/bin/env python

import time
import re
import os
import boto.iam


SQS_POLICY = """
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "sqs:*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
}"""

#g_sqs_stg

class IamManager(object):

  def __init__(self,object):
    self.conn = self.__get_boto_conn(object)


  def __get_boto_conn(self,object):
    #if region not in self.boto_conns:
    conn = boto.connect_iam(aws_access_key_id=object._iniconfigs['AWS_ACCESS_KEY'],
                            aws_secret_access_key=object._iniconfigs['AWS_SECRET_KEY'])
    if not conn:
      print "Connection cannot be established with AWS, check your region and credentials please"
      raise

    return conn


  def create_user(self,name):

    if self.validate_name(name):
      self.conn.create_user(name)
      self.name = name
      self.add_environment()
      self.attach_group()
      user = self.conn.create_access_key(name)
      self.secretID  = user.access_key_id
      self.secterKey = user.secret_access_key


  def attach_group(self):
      if self.env == 'stg':
          self.conn.add_user_to_group('g_sqs_stg',self.name)
      elif self.env == 'pro':
          self.conn.add_user_to_group('g_sqs_pro',self.name)

  def validate_name(self,name):
      if name.startswith('sqs_stg-') or name.startswith('sqs_pro-'):
        return True
      else:
        print "This user does not match Letgo naming connvention, name must start by sqs_ENV-*"
        raise


  def show_secretID(self):
      return self.secretID

  def show_secretKey(self):
      return self.secterKey

  def show_user_name(self):
      return self.name

  def add_environment(self):
    if self.name.startswith('sqs_stg-'):
        self.env = 'stg'

    elif self.name.startswith('sqs_pro-'):
        self.env = 'pro'



