#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argparse
import os, sys
#import logging

from awslglib.core.config import Config
from awslglib.SNS.sns import SnsManager
from awslglib.IAM.iammanager import IamManager
from awslglib.SQS.sqsmanager import SqsManager
from awslglib.core.policy_generator import *





def main():
  settings = Config()

  import boto.sqs

  sqs = SqsManager(settings)
  iam = IamManager(settings)
  sns = SnsManager(settings)


  username = 'sqs_stg-narcis'
  sqsname  = 'narcis-sqs'
  snsname  = 'narcis-sns'



  # Crear un usari:
  iam.create_user(username)
  if iam.is_a_new_user():
    print "User created: " + iam.show_user_name()
    print "ID for user " +  iam.show_user_name() + ": " + iam.show_secretID()
    print "Keys for user " +  iam.show_user_name() + ": " + iam.show_secretKey()


  sys.exit(0)

  sqs.create_queue(narcis-sqs)
  #sqs.add_permission()

  #qs = sns.get_all_queues('narcis')
  #print qs
  #print qs[0].get_timeout()
  #print dir(qs[0])




  # Create SNS and subscribe the SQS
  topic = sns.create_topic('narcis-sns')
  topicarn = topic['CreateTopicResponse']['CreateTopicResult']['TopicArn']
  sns.subscribe_to_topic(topicarn,'arn:aws:sqs:us-west-1:072182941009:narcis4')




  #Policy
  #my_policy = generate_policy(sqs='narcis4',sqs_perms='SendMessage', iam='narcis.pillao')
  #sqs.attach_policy(my_policy)
























if __name__ == "__main__":
    main()