import json


data = {
  "user": 'sqs-stg-foo',
  "sqs": [
    {
      "name": "sqs-A",
      "perms": ['send','get'],
      "sns": "sns-foo",
    },
    {
      "name": "sqs-B",
      "perms": ['*'],
      "sns": "sns-fee",
    },
  ]
}


print repr(data)
print json.dumps(data)