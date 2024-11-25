import boto3

def lambda_handler (event, context):


    dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
    dynamodb_resouce = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb_resouce.Table('Visitors')
    table_name = "Visitors"
    existing_tables = dynamodb_client.list_tables()['TableNames']
    if table_name not in existing_tables:
        dynamodb_client.create_table(
                        TableName= "Visitors",
                        KeySchema=[
                                {
                                  'AttributeName': 'ID',
                                  'KeyType': 'HASH'
                                },
                        ],
                        AttributeDefinitions=[
                                {
                                  'AttributeName': 'ID',
                                  'AttributeType': "N"
                                }
                        ],
                        ProvisionedThroughput={
                                'ReadCapacityUnits': 5,
                                'WriteCapacityUnits': 5
                        }
                )
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
