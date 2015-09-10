''' Tweets alphabetized version of people's tweets back at them '''
import tweepy
from tweepy.error import TweepError

from Alphabetizer import alphabetize
import settings

def create_tweets():
    ''' creates the tweet '''
    tweets = []
    counter = 1
    for tweet in tweepy.Cursor(api.search,
                               q='alphabetize',
                               rpp=10,
                               result_type='recent',
                               lang='en').items():
        text = '@%s %s' % (tweet.user.screen_name, alphabetize(tweet.text))
        if len(text) > 140:
            pass

        tweets.append({
            'text': text,
            'reply_id': tweet.id_str
        })

        if counter >= 5:
            break
        counter += 1

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
        content = create_tweets()
        for item in content:
            try:
                api.update_status(status=item['text'], in_reply_to_status_id=item['reply_id'])
            except TweepError as e:
                print 'Failed to tweet: "%s"' % content
                print 'error: %s' % e
