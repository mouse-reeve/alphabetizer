''' tweet out alphabetized versions of tweets '''
from alphabetizer import alphabetize
import settings
from TwitterAPI import TwitterAPI

api = TwitterAPI(settings.API_KEY,
                 settings.API_SECRET,
                 settings.ACCESS_TOKEN,
                 settings.ACCESS_SECRET)

stream = api.request('statuses/filter',
                     {'track': 'alphabetize,alphabetizer,alphabetized'})

for item in stream.get_iterator():
    if 'text' in item and not item['user']['screen_name'] == 'alphabotizer':
        print '--- I found a tweet! ---'
        text = item['text']
        print text
        tweet_id = item['id']
        url = 'https://twitter.com/%s/status/%d' % (item['user']['screen_name'],
                                                    tweet_id)

        alphabetized = '%s %s' % (alphabetize(text), url)
        print alphabetized

        resp = api.request('statuses/update', {
            'in_reply_to_status_id': tweet_id,
            'status': alphabetized
        })
        print resp.response
        if resp.status_code != 200:
            print resp.text
        print '\n\n\n'
