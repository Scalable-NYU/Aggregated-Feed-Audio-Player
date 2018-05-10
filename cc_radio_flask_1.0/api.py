import boto3
def get_entry(user_id):
    dynamodb = boto3.resource('dynamodb')
    audio_table = dynamodb.Table('AUDIO')
    response = audio_table.get_item(
        Key={'user_id': user_id}
    )
    return response['Item']

print(get_entry('netjimmy'))