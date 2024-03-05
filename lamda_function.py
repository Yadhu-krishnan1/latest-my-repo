import json

def lambda_handler(event, context):
    # Parse input event
    name = event['name'] if 'name' in event else 'Guest'
    
    # Generate response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': f'Hello, {name}! Welcome to Lambda function11.'})
    }
    
    return response

