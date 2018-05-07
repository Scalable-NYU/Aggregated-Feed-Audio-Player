import boto3

dynamodb = boto3.resource('dynamodb')
user_table = dynamodb.Table('USER')

response = user_table.get_item(
	Key={
		'User':'Lizi',
	}
)

user_item = response['Item']
name = user_item['User']
userid = user_item['Id']

print(name)
print(userid)

secret_table = dynamodb.Table('SECRET')

response = secret_table.get_item(
	Key={
		'User_ID':userid
	}
)

secret_item = response['Item']
consumer_key = secret_item['consumer_key']
consumer_secret = secret_item['consumer_secret']
access_token_key = secret_item['access_token_key']
access_token_secret = secret_item['access_token_secret']

print(consumer_key)
print(consumer_secret)
print(access_token_key)
print(access_token_secret)
