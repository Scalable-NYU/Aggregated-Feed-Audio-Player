from datetime import datetime, timedelta
import time
import twitter
import json
import pytz
import sys

def get_secrets(user_id):
    """
    Get user secrets
    """
    with open('cc_tweets_example/secrets.json') as secrets:
        secrets_json = json.load(secrets)

    return secrets_json[user_id]

def get_users():
    """
    Get all user_id
    """
    with open('cc_tweets_example/user.json') as r:
        user_json = json.load(r)

    return user_json['users']

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


def parse_tweet(user_id, traceback_time):
    """
    Parse user tweets traceback to specific time
    """
    user_secrets = get_secrets(user_id)
    api = twitter.Api(consumer_key=user_secrets['consumer_key'],
                      consumer_secret=user_secrets['consumer_secret'],
                      access_token_key=user_secrets['access_token_key'],
                      access_token_secret=user_secrets['access_token_secret'])

    homeTimeLine = api.GetHomeTimeline()

    user_tweets = []
    for tweet in homeTimeLine:
        tweet_time = datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S %z %Y') # in UTC time
        if traceback_time < tweet_time:
            dic = {'screenName':tweet.user.name, 'text':tweet.text, 'time':tweet.created_at}
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

            user_tweets.append(dic)
        else:
            break
    return user_tweets


def main():
    time_slot = 1
    # time_slot = argv[1]
    cur_time = datetime.utcnow()
    traceback_time = cur_time - timedelta(hours=time_slot)
    user_list = get_users()

    result = {}
    for usr in user_list:
        result[usr] = parse_tweet(usr, traceback_time)

    with open ('cc_tweets_example/{0}00.json'.format(cur_time.strftime('%m%d%H')), 'w') as w: # UTC time
        json.dump(result, w)

    return json.dumps(result, indent=4, sort_keys=True)

if __name__ == "__main__":
    main()