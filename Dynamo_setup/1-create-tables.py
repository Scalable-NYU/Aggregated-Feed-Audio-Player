import boto3

dynamodb = boto3.resource('dynamodb')

user_table = dynamodb.create_table(
    TableName='USER',
    KeySchema=[
        {
            'AttributeName': 'User',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'User',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("User Table status:", user_table.table_status)

secret_table = dynamodb.create_table(
    TableName='SECRET',
    KeySchema=[
        {
            'AttributeName': 'User_ID',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'User_ID',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


print("Secret Table status:", secret_table.table_status)

twtr_table = dynamodb.create_table(
    TableName='TWTR',
    KeySchema=[
        {
            'AttributeName': 'User_ID',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'User_ID',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("TWTR Table status:", twtr_table.table_status)

