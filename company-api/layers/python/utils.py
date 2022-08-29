#sample
import boto3
import logging
from boto3.dynamodb.conditions import Key

logger = logging.getLogger("Analytics Ref Archs")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

class Dynamo:
    def __init__(
        self,
        dynamo_table: str = None,
        dynamo_key: str = None,
        item: dict = None,

    ):
        self._dynamo_table = dynamo_table
        self._dynamo_key = dynamo_key
        self._item = item

    @property
    def dynamo_table(self) -> str:
        return self._dynamo_table

    @dynamo_table.setter
    def dynamo_table(self, name: str):
        self._dynamo_table = name

    @property
    def dynamo_key(self) -> str:
        return self._dynamo_key

    @dynamo_key.setter
    def dynamo_key(self, name: str):
        self._dynamo_key = name

    @property
    def item(self) -> dict:
        return self._item

    @item.setter
    def item(self, data: dict):
        self._item = data

    def getItem(self) -> list:
        """[summary]
        Returns:
            dict: last refresh history
        """
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(self._dynamo_table)

        try:
            response = table.query(
                Limit=1,
                KeyConditionExpression=Key("companyName").eq(self._dynamo_key)
            )
            return response["Items"]
        except Exception as error:
            print(error)
            return None
    
    def litsItems(self)->list:
        client = boto3.client("dynamodb")
        try:
            results = client.scan(
                TableName=self._dynamo_table,
                Select="ALL_ATTRIBUTES",
                ConsistentRead=True,
            )
            if len(results["Items"]) == 0:
                return []
            items = []
            for result in results["Items"]:
                _item = {}
                for _key, _value in result.items():
                    for _, value in _value.items():
                        _item[_key] = value
                items.append(_item)
            return items
        except Exception as e:
            logger.error('Error', e)
            return []

    def addItem(self,) -> bool:
        """[summary]
        Returns:
            bool: [description]
        """

        dynamodb = boto3.resource("dynamodb")

        table = dynamodb.Table(self._dynamo_table)
        try:
            response = table.put_item(Item=self._item)
            logger.info(response)
            return True
        except Exception as error:
            logger.error("Error", error)
            return False