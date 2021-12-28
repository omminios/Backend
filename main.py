import boto3

def lambda_handler (event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Visitors')
    response = table.update_item(
        Key={
            "ID": 0
        },
        ExpressionAttributeNames = {
            "#c": "Counter"
        },
        UpdateExpression= "set #c = #c + :val",
        ExpressionAttributeValues={
            ":val": 1
        },
    ReturnValues= "UPDATED_NEW"
    )
   
    responseBody = response["Attributes"]["Counter"]

    return {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Headers': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': responseBody
        }