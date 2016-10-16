#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argparse
import os
#import logging

from awslglib.core.config import Config
from awslglib.SNS.sns import SnsManager
from awslglib.IAM.iammanager import IamManager






def main():
  settings = Config()

  sns = SnsManager(settings)
  qs = sns.get_all_queues('narcis')
  print qs[0].get_timeout()
  print dir(qs[0])

  #iam = IamManager(settings)
  #iam.create_user('sqs_stg-test')
  #print iam.show_user_name()
  #print iam.show_secretID()
  #print iam.show_secretKey()


















if __name__ == "__main__":
    main()