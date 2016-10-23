#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argparse
import os, sys
import logging

from awslglib.core.config import Config
from awslglib.core.policy_generator import *
from awslglib.SNS.snsmanager import SnsManager
from awslglib.IAM.iammanager import IamManager
from awslglib.SQS.sqsmanager import SqsManager


# Example:
# ./queue_manager.py --iam sqs_stg-narcis --sqs narcis-sqs --sqsact '*' --sns narcis-sns --snsact SendMessage DeleteMessage




def main():

  logging.getLogger('boto').setLevel(logging.CRITICAL)
  logging.basicConfig(level=logging.INFO)

  usage = 'Usage: %prog [options] arg1 arg2'
  parser = argparse.ArgumentParser()
  actions = [ 'SendMessage', '*', 'ReceiveMessage', 'DeleteMessage', 'ChangeMessageVisibility' 'GetQueueAttributes']

  parser.add_argument('-u', '--iam',     dest='username', type=str,  help = 'Username who want to create or associate a resource')
  parser.add_argument('-q', '--sqs',     dest='sqs',      type=str,  help = 'SQS name')
  parser.add_argument('-a', '--sqsact',  dest='sqsact',   type=str,  nargs='*', help = 'SQS Actions')
  parser.add_argument('-s', '--sns',     dest='sns',      type=str,  help = 'SNS name')
  parser.add_argument('-p', '--snsact',  dest='snsact',   type=str,  nargs='*', help = 'SNS Actions')

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
    logging.info("User created: " + iam.show_user_name())
    print "ID for user " +  iam.show_user_name() + ": " + iam.show_secretID()
    print "Keys for user " +  iam.show_user_name() + ": " + iam.show_secretKey()


  # Create queue
  if sqsname:
    queue    = sqs.create_queue(sqsname)
    queuearn =  sqs.get_arn()
    queueurl =  sqs.get_url()


  # Create SNS and subscribe the SQS
  if snsname:
    sns.create_topic(snsname)
    topicarn = sns.get_topciarn()
    sns.subscribe_to_topic(topicarn, queuearn)

    #Policy
    my_policy = generate_policy(sqs=sqsname, sns=snsname, sqs_perms=sqsact, iam=username, sns_perms=snsact)
  else:
    my_policy = generate_policy(sqs=sqsname, sqs_perms=sqsact, iam=username)

  sqs.attach_policy(my_policy)























if __name__ == "__main__":
    main()