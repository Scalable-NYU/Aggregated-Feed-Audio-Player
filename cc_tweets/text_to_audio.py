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
    sum = ""
    sci = ""
    business = ""
    sport = ""
    world = ""
    for tweet in user_tweets:
        datetime_local = utc2local(datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'))
        sum += tweet['screenName'] + " at " + datetime_local.strftime('%-I:%M %p') + " posts, \"" + tweet['text'] + "\" "
        # if tweet['category'] == 0:
        #     sci += tweet['screenName'] + " at " + datetime_local.strftime('%-I:%M %p') + " posts, \"" + tweet['text'] + "\" "
        # elif tweet['category'] == 1:
        #     business += tweet['screenName'] + " at " + datetime_local.strftime('%-I:%M %p') + " posts, \"" + tweet['text'] + "\" "
        # elif tweet['category'] == 2:
        #     sport += tweet['screenName'] + " at " + datetime_local.strftime('%-I:%M %p') + " posts, \"" + tweet['text'] + "\" "
        # else:
        #     world += tweet['screenName'] + " at " + datetime_local.strftime('%-I:%M %p') + " posts, \"" + tweet['text'] + "\" "

    return sum, sci, business, sport, world

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
        sci_list = []
        business_list = []
        sport_list = []
        world_list = []

        res = twtr_table.get_item(Key={'user_id':usr, 'datetime':cur_time_str})
        user_tweets = res['Item']['tweets']
        text = get_text(user_tweets)

        for i in range(0, len(text)):
            if text[i] != "":
                # text to speech
                audio = gTTS(text[i], lang='en')
                audio.save('./audio/tmp.mp3')

                # upload to s3
                s3.upload_file("./audio/tmp.mp3",
                            "cc-project-s3",
                            "{0}/{1}_{2}.mp3".format(usr, cur_time.strftime('%H'), i),
                            ExtraArgs={'ACL': 'public-read'}
                            )

if __name__ == "__main__":
    main()
