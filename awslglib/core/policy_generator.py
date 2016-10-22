import json
import random


def generate_policy(sqs=None, effect='Allow', sqs_perms=None, sns=None, iam=None):

  sid = str(random.randint(19999999,999999999))

  # json.dumps({

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
                "Action": 'SQS:' + sqs_perms,
                "Resource": "arn:aws:sqs:us-west-1:072182941009:" + sqs
            },
            {
                "Sid": str(sns) + "-" + str(sid),
                "Effect": effect,
                "Principal": "*",
                "Action": 'SQS:' + sqs_perms,
                "Resource": "arn:aws:sqs:us-west-1:072182941009:" + sqs,
                "Condition": {
                    "StringEquals": {
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
                  "Action": 'SQS:' + sqs_perms,
                  "Resource": "arn:aws:sqs:us-west-1:072182941009:" + sqs
              }
          ]
      }, sort_keys=None)


  return policy

