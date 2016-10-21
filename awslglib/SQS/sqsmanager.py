#!/usr/bin/env python
import boto.sqs



class SqsManager(object):

  def __init__(self,config):
    self.config = config
    self.conn = self.__get_boto_conn()

  def __get_boto_conn(self):
    conn = boto.sqs.connect_to_region(self.config._iniconfigs['region'], aws_access_key_id=self.config._iniconfigs['AWS_ACCESS_KEY'],
                                                                 aws_secret_access_key=self.config._iniconfigs['AWS_SECRET_KEY'])
    if not conn:
      print "Connection cannot be established with AWS, check your region and credentials please"
      raise

    return conn


  def get_all_queues(self, prefix=None):
    return self.conn.get_all_queues(prefix)


  def create_queue(self, name):
    queue = self.conn.create_queue(name)
    self.conn.add_permission(queue, 'NarcisSendmessage', '072182941009', 'SendMessage')