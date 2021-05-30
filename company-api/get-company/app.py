from utils import Dynamo
import json

def handler(event: dict, context: dict):

    response = {"statusCode": 204, "body": "No results found"}
    table = 'learn-api-dynamo-database'
    
    print(event)

    if "queryStringParameters" in event and event['queryStringParameters'] is not None and 'companyName' in event['queryStringParameters']:
        companyName = event['queryStringParameters']['companyName']
        if companyName is None:
            response['statusCode'] = 404
            response['body'] = 'You must pass companyName as parameter in your request'
        dynamo = Dynamo(dynamo_table=table, dynamo_key=companyName)
        result = dynamo.getItem()
        if result is not None:
            response['statusCode'] = 200
            response['body'] = json.dumps(result)
            return response
        return response
    return response
