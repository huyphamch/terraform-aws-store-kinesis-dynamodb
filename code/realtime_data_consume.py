import boto3
import os
import json
import time
from datetime import datetime
import base64

# Initialize DynamoDB and Kinesis resources and set up constants
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'realtime-data_table'

def lambda_handler(event, context):
    print(event)
    for i in event['Records']:
        print("Raw data :",i['kinesis']['data']);
        print("base64 decoded data :",base64.b64decode(i['kinesis']['data']));
        print("UTF-8 decoded data :",base64.b64decode(i['kinesis']['data']).decode('utf-8'));
        # Put data into DynamoDB
        # table = dynamodb.Table(table_name)
        # item = {
        #     'id': tweet_id,
        #     'timestamp': timestamp.isoformat(),
        #     'text': text,
        #     'user': {
        #         'id': user['id_str'],
        #         'screen_name': user['screen_name'],
        #         'name': user['name']
        #     }
        # }
        # table.put_item(Item=item)
    json_region = os.environ['AWS_REGION']
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Region ": json_region
        })
    }

