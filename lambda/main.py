def lambda_handler(event, context):
    print(f"Event: {event}")
    responseMessage = "Hello, World!"
     
    return {
        "statusCode": 200,
        "body": responseMessage
    }