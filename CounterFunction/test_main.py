import unittest
import boto3
from moto import mock_aws
import main as m


@mock_aws
class TestDynamodb(unittest.TestCase):
        
        def setUp(self):
                self.dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
                table = self.dynamodb.Table("Visitors")
                self.dynamodb.create_table(
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
                table.put_item(
                Item={
                'ID': 0,
                'Counter': 0
                })
        
        def tearDown(self):
                self.dynamodb = boto3.resource("dynamodb", region_name='us-east-1')
                table = self.dynamodb.Table("Visitors")
                table.delete()
            
                
        def test_update_table(self):
                self.dynamodb.Table('Visitors')
                response = m.lambda_handler(None, None)
                self.assertEqual(response['statusCode'], 200)
                self.assertEqual(response['body'], 1)
                
                
        
if __name__ =="__main__":
    unittest.main()
