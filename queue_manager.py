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

  usage = 'Usage: %prog [options] arg1 arg2'
  parser = argparse.ArgumentParser()

  parser.add_argument('-u', '--iam',     dest='username', type=str,  help = 'Username who want to create or associate a resource')
  parser.add_argument('-q', '--sqs',     dest='sqs',      type=str,  help = 'SQS name')
  parser.add_argument('-a', '--sqsact',  dest='sqsact',   type=str,  help = 'SQS Actions')
  parser.add_argument('-s', '--sns',     dest='sns',      type=str,  help = 'SNS name')
  parser.add_argument('-p', '--snsact',  dest='snsact',   type=str,  help = 'SNS Actions')

  args = parser.parse_args()

  username = args.username
  sqsname  = args.sqs
  sqsact   = args.sqsact
  snsname  = args.sns
  snsact   = args.snsact

  # Example:
  #username = 'sqs_stg-narcis'
  #sqsname  = 'narcis-sqs'
  #snsname  = 'narcis-sns'


  settings = Config()
  sqs = SqsManager(settings)
  iam = IamManager(settings)
  sns = SnsManager(settings)






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

  my_policy = generate_policy(sqs=sqsname, sns=snsname, sqs_perms=sqsact, iam=username)
  sqs.attach_policy(queue, my_policy)


  sys.exit(0)






















if __name__ == "__main__":
    main()