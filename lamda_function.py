import json

def lambda_handler(event, context):
    # Parse the input event
    name = event['name']
    
    # Process the input and generate a response
    greeting = f"Hello, {name}! This is a Lambda function written in Python1."
    
    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps(greeting)
    }
