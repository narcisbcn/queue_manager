import json
import random, sys


def generate_policy(sqs=None, effect='Allow', sqs_perms=None, sns=None, iam=None, sns_perms=None):
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

  _sqs_perms = generate_action(sqs_perms)
  _sns_perms = generate_action(sns_perms)

  sid = str(random.randint(19999999,999999999))

  if sns is not None:
    policy = json.dumps({
       "Version": "2008-10-17",
       "Id": sid,
        "Statement":  [
            {
                "Sid": str(sqs) + "-" + str(sid),
                "Effect": effect,
                "Principal": {
                    "AWS": "arn:aws:iam::072182941009:user/" + iam
                },
                "Action": _sqs_perms,
                "Resource": "arn:aws:sqs:us-west-1:072182941009:" + sqs
            },
            {
                "Sid": str(sns) + "-" + str(sid),
                "Effect": effect,
                "Principal": "*",
                "Action": _sns_perms,
                "Resource": "arn:aws:sqs:us-west-1:072182941009:" + sqs,
                "Condition": {
                    "ArnEquals": {
                        "aws:SourceArn": "arn:aws:sns:us-west-1:072182941009:" + sns
                    }
                }
            }
        ]
    }, sort_keys=None)
  else:
      policy = json.dumps({
          "Version": "2008-10-17",
          "Id": sid,
          "Statement": [
              {
                  "Sid": str(sqs) + "-" + str(sid),
                  "Effect": effect,
                  "Principal": {
                      "AWS": "arn:aws:iam::072182941009:user/" + iam
                  },
                  "Action": _sqs_perms,
                  "Resource": "arn:aws:sqs:us-west-1:072182941009:" + sqs
              }
          ]
      }, sort_keys=None)

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
            print element
            action.append("SQS:" + element)

    return action