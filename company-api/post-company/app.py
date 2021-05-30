from utils import Dynamo
import json

def handler(event: dict, context: dict):

    response = {"statusCode": 201, "body": "Data Added"}
    table = 'learn-api-dynamo-database'

    if 'body' not in event:

        response['statusCode'] = 401
        response['body'] = 'You must pass provide body'
        return response
    
    dynamo = Dynamo(dynamo_table=table)
    body = json.loads(event['body'])
    dynamo.item = body
    if dynamo.addItem():
        return response
    response['statusCode'] = 505
    response['body'] = 'Could not add item'
    return response
