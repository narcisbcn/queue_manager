#!/usr/bin/env python
import time
import re
import os
import boto.sns
import argparse



class SnsManager(object):

  def __init__(self,config):
    self.config = config
    self.conn = self.__get_boto_conn()

  def __get_boto_conn(self):
    conn = boto.sns.connect_to_region(self.config._iniconfigs['region'], aws_access_key_id=self.config._iniconfigs['AWS_ACCESS_KEY'],
                                                                 aws_secret_access_key=self.config._iniconfigs['AWS_SECRET_KEY'])
    if not conn:
      print "Connection cannot be established with AWS, check your region and credentials please"
      raise

    return conn



  def create_topic(self, name):
    return self.conn.create_topic(name)

  def subscribe_to_topic(self, arntopic, arnendpoint, protocol='sqs'):
    return self.conn.subscribe(arntopic, protocol, arnendpoint)

  # set subscription attributes





