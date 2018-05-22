from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
from boto3.dynamodb.conditions import Key
import DecimalEncoder

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Movies')

response = table.query(
    KeyConditionExpression=Key('year').eq(2000)
)

for item in response['Items']:
    year = item['year']
    title = item['title']
    res = table.delete_item(
        Key={
            'year': year,
            'title': title
        }
    )

    print(json.dumps(res, indent=4, cls=DecimalEncoder.Encoder))