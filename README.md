# queue_manager

Overview
=========
This project allow us to create SQS queues which can be subscribed to SNS topics. We use IAM users to provide
privilege to those SQS and SNS resources


Bootstrap
=========

In order to configure your environment, the queue_manager will pick up the configuration files from those paths:

- ~/.awslglib.ini
- /etc/awslglib.ini

You can use the config file you wish. It has a hierarchy, meaning, the file on the top will be picked up first.


How looks that config file?
```
[AUTH]
AWS_ACCESS_KEY=XXXXXXXXXXXXXX
AWS_SECRET_KEY=XXXXXXXXXXXXXX
region=us-east-1
account_id=XXXXXXXXX
```


Examples
========

Creating a simple sqs queue:
```
./queue_manager.py --iam sqs_stg-service4service_domain_events --sqs stg-service_domain_events --sqsact '*'
```

Creating a simple sqs queue with limited privileges:
```
./queue_manager.py --iam sqs_stg-service4service_domain_events --sqs stg-service_domain_events --sqsact SendMessage DeleteMessage
```

Creating a sqs and sns and subscribe that sqs as a sns topic
```
./queue_manager.py --iam sqs_stg-service4service_domain_events --sqs stg-service_domain_events --sqsact SendMessage DeleteMessage ReceiveMessage --sns stg-service_domain_events --snsact ReceiveMessage
```


TODO
====

- To improve policy template
- Do not attach policies until all resources are created
- Allow a sqs to subscribe to multiple sns topics
