#!/usr/bin/env python3
import os

from aws_cdk import App, Environment
from boto3 import client, session

from cdk.{{cookiecutter.service_name}}.service_stack import ServiceStack
from cdk.{{cookiecutter.service_name}}.utils import get_stack_name

account = client('sts').get_caller_identity()['Account']
region = session.Session().region_name
environment = os.getenv('ENVIRONMENT', 'dev')
app = App()
my_stack = ServiceStack(
    scope=app,
    id='DeployLambdaStack',
    env=Environment(account=os.environ.get('AWS_DEFAULT_ACCOUNT', account), region=os.environ.get('AWS_DEFAULT_REGION', region)),
    is_production_env=True if environment == 'production' else False,
)

app.synth()
