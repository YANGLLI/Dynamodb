from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import DecimalEncoder

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Movies')

title = "The Big New Movie"
year = 2016

response = table.put_item(
    Item = {
        'year': year,
        'title': title,
        'info': {
            'plot': 'Nothing happens at all.',
            'rating': decimal.Decimal(0)
        }
    }
)

print(json.dumps(response, indent=4, cls=DecimalEncoder.Encoder))