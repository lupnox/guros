# app.py
import os
import boto3
import uuid
from flask import Flask, jsonify, make_response, request
from dna_check import cerebro

app = Flask(__name__)


dynamodb_client = boto3.client('dynamodb')

if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


USERS_TABLE = os.environ['DNA_TABLE']


@app.route('/', methods=['POST'])
def hasMutation():
    dna = request.json.get('dna')
    if not dna:
    	#log error
        return jsonify({'error': 'Expected data in "dna" key'}), 400
    if(cerebro(dna)):
	    dynamodb_client.put_item(
	        TableName=DNA_TABLE, Item={'dnaId': {'S': str(uuid.uuid1())}, 'mutation': {'B': mutant}}
	    )
    	return jsonify({'Mutation found!'}),200
    else:
    	return jsonify({'No mutations found'}),403


@app.route('/', methods=['GET'])
def get_results():
    result = dynamodb_client.get_item(
        TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
    )
    item = result.get('Item')
    if not item:
        return jsonify({'error': 'Could not find user with provided "userId"'}), 404

    return jsonify(
        {'userId': item.get('userId').get('S'), 'name': item.get('name').get('S')}
    )


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)