#DynamoDB handler
#EMV
import os
import uuid
import json
import boto3
import logging
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DNA_TABLE'])


def save_entry(result):
    entry = {
        'dnaId': str(uuid.uuid1()),
        'mutation': result,
    }
    # write the todo to the database
    table.put_item(Item=entry)
    return

def get_count(args):
    #scan dynamo table
    done = False
    start_key = None
    while not done:
        if start_key:
            args['ExclusiveStartKey'] = start_key
        result = table.scan(**args)
        start_key = result.get('LastEvaluatedKey', None)
        done = start_key is None
    return result.get('Count')

def get_results(event,context):
    #get count of items
    scan_kwargs = {'FilterExpression':Key('mutation').eq(True)}
    mutants = get_count(scan_kwargs)
    scan_kwargs = {'FilterExpression':Key('mutation').eq(False)}
    muggles = get_count(scan_kwargs)
    ratio = mutants/muggles
    data = {"count_mutations": mutants,"count_no_mutation": muggles,"ratio": ratio}
    response = {
        "statusCode": 200,
        "body": json.dumps(data)
    }
    return response 