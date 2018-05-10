import boto3
import json

dynamodb = boto3.resource('dynamodb')

meta_table = dynamodb.create_table(
    TableName='META',
    KeySchema=[
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("META Table status:", meta_table.table_status)

twtr_table = dynamodb.create_table(
    TableName='TWTR',
    KeySchema=[
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'datetime',
            'KeyType': 'RANGE'  #sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'datetime',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("TWTR Table status:", twtr_table.table_status)

audio_table = dynamodb.create_table(
    TableName='AUDIO',
    KeySchema=[
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("AUDIO Table status:", audio_table.table_status)
