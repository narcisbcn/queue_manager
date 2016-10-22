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
    self.arn = queue.arn
    self.url = queue.url
    print "Queue created successfully: " + name

  def get_arn(self):
    return self.arn

  def get_url(self):
    return self.url



  def attach_policy(self,policy):
    import json
    policy2 = json.dumps({
        "Version": "2008-10-17",
        "Id": "98728687",
        "Statement": [
          {
            "Sid": "sqs-narcis4",
            "Effect": "Allow",
            "Principal": {
              "AWS": "arn:aws:iam::072182941009:user/narcis.pillao"
           },
           "Action": "SQS:ReceiveMessage",
            "Resource": "arn:aws:sqs:us-west-1:072182941009:narcis4"
         },
          {
            "Sid": "Sid1475226761446",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "SQS:SendMessage",
            "Resource": "arn:aws:sqs:us-west-1:072182941009:narcis4",
            "Condition": {
              "StringEquals": {
                "aws:SourceArn": "arn:aws:sns:us-west-1:072182941009:narcis-sns"
              }
            }
          }
        ]
    })

    ## connection.set_queue_attribute(queue, 'Policy', json.dumps({
    queue = self.conn.create_queue('narcis4')
    print "queue created"
    print policy
    print policy2
    self.conn.set_queue_attribute(queue, 'Policy', policy )

