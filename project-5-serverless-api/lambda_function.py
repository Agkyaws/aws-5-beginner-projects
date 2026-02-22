import json
import boto3
import uuid

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData')

def lambda_handler(event, context):
    # Create a random ID
    user_id = str(uuid.uuid4())
    
    # Insert data into database
    table.put_item(
        Item={
            'userid': user_id,
            'message': 'Hello from Serverless World!',
            'status': 'Success'
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully saved User ID: {user_id}')
    }
