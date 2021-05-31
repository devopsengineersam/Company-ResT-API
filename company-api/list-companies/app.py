from utils import *
import json
def handler(event: dict, context: dict):

    response = {"statusCode": 204, "body": "No results found"}
    table = 'rest-dynamo-database'
    dynamo = Dynamo(dynamo_table=table)
    
    

    companies =  dynamo.litsItems()

    if len(companies) == 0 or companies is None:
        return response
    
    response['statusCode'] = 200
    response['body'] = json.dumps(companies)
    return response
 
    
