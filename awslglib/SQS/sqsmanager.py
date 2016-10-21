#!/usr/bin/env python
import boto.sqs



class SqsManager(object):

  def __init__(self,object):
    self.conn = self.__get_boto_conn(object)


  def __get_boto_conn(self,object):


    conn = boto.sqs.connect_to_region(object._iniconfigs['region'], aws_access_key_id=object._iniconfigs['AWS_ACCESS_KEY'],
                                                                 aws_secret_access_key=object._iniconfigs['AWS_SECRET_KEY'])
    if not conn:
      print "Connection cannot be established with AWS, check your region and credentials please"
      raise

    return conn


  def get_all_queues(self, prefix=None):
      return self.conn.get_all_queues(prefix)
