from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import DecimalEncoder

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Movies')

title = "The Big New Movie"
year = 2016

response = table.update_item(
    # Must specify full key
    Key = {
        'year': year,
        'title': title
    },
    UpdateExpression = "remove info.actors[0]",
    ConditionExpression = "info.rating <= :r",
    ExpressionAttributeValues = {
        ':r': decimal.Decimal(10),
    },
    ReturnValues = "UPDATED_NEW"
)

print(json.dumps(response, indent=4, cls=DecimalEncoder.Encoder))