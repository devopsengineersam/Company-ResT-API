from utils import *
import json
def handler(event: dict, context: dict):

    response = {"statusCode": 204, "body": "No results found"}
    table = 'learn-api-dynamo-database'
    dynamo = Dynamo(dynamo_table=table)
    
    

    comapanies =  dynamo.litsItems()

    if len(comapanies) == 0 or comapanies is None:
        return response
    
    response['statusCode'] = 200
    response['body'] = json.dumps(comapanies)
    return response
 
    