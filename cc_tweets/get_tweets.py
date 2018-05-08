from datetime import datetime, timedelta
import time
import twitter
import json
import pytz
import sys
import boto3
import re
from boto3.dynamodb.conditions import Key, Attr

def parse_tweet(traceback_time, cur_time_str):
    """
    Parse user tweets traceback to specific time and store in dynamodb
    """
    dynamodb = boto3.resource('dynamodb')

    # read user_list from database
    meta_table = dynamodb.Table('META')
    twtr_table = dynamodb.Table('TWTR')
    res = meta_table.scan(ProjectionExpression="user_id")
    user_list = [dic['user_id'] for dic in res['Items']]

    for usr in user_list:
        res = meta_table.get_item(Key={'user_id':usr})
        user_meta = res['Item']
        # get user tweet timeline
        api = twitter.Api(consumer_key=user_meta['consumer_key'],
                      consumer_secret=user_meta['consumer_secret'],
                      access_token_key=user_meta['access_token_key'],
                      access_token_secret=user_meta['access_token_secret'])

        homeTimeLine = api.GetHomeTimeline()

        tweet_list=[]
        for tweet in homeTimeLine:
            tweet_time = datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S +0000 %Y') # in UTC time
            if traceback_time < tweet_time:
                text = tweet.text
                clean_tweet = re.match('(.*?)http.*?\s?(.*?)', text)
                if clean_tweet:
                    text = clean_tweet.group(1)

                dic = {'screenName':tweet.user.name,
                        'text':text,
                        'created_at':tweet.created_at,
                        'tweet_id':tweet.id}
                try:
                    dic['quote_count'] = tweet.quote_count
                except:
                    dic['quote_count'] = 0
                    pass

                try:
                    dic['reply_count'] = tweet.reply_count
                except:
                    dic['reply_count'] = 0
                    pass

                try:
                    dic['retweet_count'] = tweet.retweet_count
                except:
                    dic['retweet_count'] = 0
                    pass

                try:
                    dic['favorite_count'] = tweet.favorite_count
                except:
                    dic['favorite_count'] = 0
                    pass
                dic['category'] = "any"

                tweet_list.append(dic)
            else:
                break

        twtr_table.put_item(
            Item = {
                'user_id':usr,
                'datetime':cur_time_str,
                'tweets':tweet_list
            }
        )


def main():
    time_slot = 1
    # time_slot = argv[1]
    cur_time = datetime.utcnow()
    traceback_time = cur_time - timedelta(hours=time_slot)
    cur_time_str = cur_time.strftime('%m%d%H')
    parse_tweet(traceback_time, cur_time_str)

    # with open ('cc_tweets_example/{0}00.json'.format(cur_time.strftime('%m%d%H')), 'w') as w: # UTC time
    #     json.dump(result, w)

    # return json.dumps(result, indent=4, sort_keys=True)

if __name__ == "__main__":
    main()
