#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argparse
import os, sys
#import logging

from awslglib.core.config import Config
from awslglib.SNS.sns import SnsManager
from awslglib.IAM.iammanager import IamManager
from awslglib.SQS.sqsmanager import SqsManager






def main():
  settings = Config()

  import boto.sqs

  sqs = SqsManager(settings)

  sqs.create_queue('narcis4')
  #sqs.add_permission()
  #sqs.create_queue('narcis')
  #print dir(sqs)
  #qs = sns.get_all_queues('narcis')
  #print qs
  #print qs[0].get_timeout()
  #print dir(qs[0])


  # Crear un usari:
  #iam = IamManager(settings)
  #iam.create_user('sqs_stg-test')
  #print iam.show_user_name()
  ##-print iam.show_secretID()
  ##-print iam.show_secretKey()


















if __name__ == "__main__":
    main()