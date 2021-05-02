#DynamoDB handler
import os
import uuid
import boto3
import logging


USERS_TABLE = os.environ['DNA_TABLE']


def save_entry(result):
    return


def get_results(event,context):
    return