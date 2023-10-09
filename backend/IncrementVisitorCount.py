import boto3
import json
from decimal import Decimal


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('VisitorCount')

    response = table.update_item(
        Key={'siteName': 'myWebsite'},
        UpdateExpression='ADD #countAttribute :increment',
        ExpressionAttributeNames={'#countAttribute': 'count'},
        ExpressionAttributeValues={':increment': Decimal(1)},
        ReturnValues="UPDATED_NEW"
    )

    # Convert Decimal to int for JSON serialization
    count_value = int(response['Attributes']['count'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'count': count_value})
    }
