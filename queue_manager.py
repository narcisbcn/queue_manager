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



  # Create queue
  queue    = sqs.create_queue(sqsname)
  queuearn =  sqs.get_arn()
  queueurl =  sqs.get_url()



  # Create SNS and subscribe the SQS
  sns.create_topic(snsname)
  topicarn = sns.get_topciarn()
  sns.subscribe_to_topic(topicarn, queuearn)


  #Policy

  my_policy = generate_policy(sqs=sqsname, sqs_perms='SendMessage', iam=username)
  sqs.attach_policy(my_policy)


  sys.exit(0)






















if __name__ == "__main__":
    main()