import os


def env(keys, dflt):
    if isinstance(keys, basestring):
        keys = [ keys ]
    for key in keys:
        if os.environ.has_key(key):
            return os.environ.get(key)
    return dflt


AWS_ACCESS_KEY = env(['AWSMS_AWS_ACCESS_KEY', 'AWS_ACCESS_KEY'], 'some_aws_access_key')
AWS_SECRET_KEY = env(['AWSMS_AWS_SECRET_KEY', 'AWS_SECRET_KEY'], 'some_aws_secret_key')

DEFAULT_EBS_VOLUME_TYPE = "standard"
THROW_ERRORS = False

AMS_LOGLEVEL = 'INFO'
