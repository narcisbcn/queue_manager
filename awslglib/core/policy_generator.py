import json
import random, sys
import logging


def generate_policy(sqs=None, effect='Allow', sqs_perms='*', sns=None, iam=None, sns_perms='*', account='fake', region='fake'):
  """
  Creates a json file from below parameters
  :param sqs: sqs name
  :param effect: Allow or Deny
  :param sqs_perms: Acctions: SendMessage * ReceiveMessage * DeleteMessage * ChangeMessageVisibility * GetQueueAttributes
  :param sns: sns name
  :param iam: iam username
  :param sns_perms: Acctions: SendMessage * ReceiveMessage * DeleteMessage * ChangeMessageVisibility * GetQueueAttributes
  :return: json
  """

  account = str(account)

  _sqs_perms = generate_action(sqs_perms)
  _sns_perms = generate_action(sns_perms)

  sid  = str(random.randint(1000000000000,9999999999999))
  q_id = "arn:aws:sqs:us-east-1:"+ account  + ":" + sqs + "/SQSDefaultPolicy"

  if sns is not None:
    sid2 = str(random.randint(1000000000000, 9999999999999))
    policy = json.dumps({
       "Version": "2012-10-17",
       "Id": q_id,
        "Statement":  [
            {
                "Sid": "Sid" + str(sid),
                "Effect": effect,
                "Principal": {
                    "AWS": "arn:aws:iam::" + account + ":user/" + iam
                },
                "Action": _sqs_perms,
                "Resource": "arn:aws:sqs:" + region + ":" + account + ":" + sqs
            },
            {
                "Sid": "Sid" + str(sid2),
                "Effect": effect,
                "Principal": "*",
                "Action": _sns_perms,
                "Resource": "arn:aws:sqs:" + region + ":" + account + ":" + sqs,
                "Condition": {
                    "ArnEquals": {
                        "aws:SourceArn": "arn:aws:sns:" + region + ":" + account + ":" + sns
                    }
                }
            }
        ]
    }, sort_keys=None)
  else:
      policy = json.dumps({
          "Version": "2012-10-17",
          "Id": q_id,
          "Statement": [
              {
                  "Sid": "Sid" + str(sid),
                  "Effect": effect,
                  "Principal": {
                      "AWS": "arn:aws:iam::" + account + ":user/" + iam
                  },
                  "Action": _sqs_perms,
                  "Resource": "arn:aws:sqs:" + region + ":" + account + ":" + sqs
              }
          ]
      }, sort_keys=None)

  logging.debug("Policy: " + policy)

  return policy


def generate_action(act):
    """
    Description: This function merges SQS actions, regardless whether are single or multiple actions
    params: The action
    """

    if type(act) is str:
        action = "SQS:" + act

    else:
        action = list()
        for element in act:
            action.append("SQS:" + element)

    return action
