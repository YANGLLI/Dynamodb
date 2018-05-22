from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import DecimalEncoder
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Movies')

title = "The Big New Movie"
year = 2016

try:
    response = table.get_item(
        Key = {
            'year': year,
            'title': title,
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print(json.dumps(response['Item'], indent=4, cls=DecimalEncoder.Encoder))