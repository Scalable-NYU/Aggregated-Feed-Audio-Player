from gtts import gTTS
import boto3
from datetime import datetime, timedelta
import time
from boto3.dynamodb.conditions import Key, Attr

def utc2local(utc_st):
    local_time = datetime.now()
    utc_time = datetime.utcnow()
    offset = local_time - utc_time
    return utc_st + offset

def local2utc(local_st):
    local_time = datetime.now()
    utc_time = datetime.utcnow()
    offset = local_time - utc_time
    return ocal_st - offset

def get_text(user_tweets):
    s = ""
    for tweet in user_tweets[:5]:
        datetime_local = utc2local(datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
        s += tweet['screenName'] + " at " + datetime_local.strftime('%H:%M') + " posts, \"" + tweet['text'] + "\" "
    return s

def main():
    dynamodb = boto3.resource('dynamodb')
    meta_table = dynamodb.Table('META')
    twtr_table = dynamodb.Table('TWTR')
    s3 = boto3.client('s3')

    res = meta_table.scan(ProjectionExpression="user_id")
    user_list = [dic['user_id'] for dic in res['Items']]
    cur_time = datetime.utcnow()
    cur_time_str = cur_time.strftime('%m%d%H')

    for usr in user_list:
        res = twtr_table.get_item(Key={'user_id':usr, 'datetime':cur_time_str})
        user_tweets = res['Item']['tweets']
        text = get_text(user_tweets)

        # text to speech
        audio = gTTS(text, lang='en')
        audio.save('./audio/tmp.mp3')

        # upload to s3
        s3.upload_file("./audio/tmp.mp3",
                        "cc-project-s3",
                        usr + "/" + cur_time.strftime('%H'),
                        ExtraArgs={'ACL': 'public-read'}
                        )

if __name__ == "__main__":
    main()
