''' Tweets alphabetized version of people's tweets back at them '''
import tweepy
from tweepy.error import TweepError

import settings

def search():
    ''' finds tweets that match the pattern '''
    return ''

def create_tweet():
    ''' creates the tweet '''
    tweets = search()
    return tweets

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except TweepError:
        pass
    else:
        for _ in range(0, 4):
            content = create_tweet()
            try:
                api.update_status(status=content)
                break
            except TweepError as e:
                print 'Failed to tweet: "%s"' % content
                print 'error: %s' % e
