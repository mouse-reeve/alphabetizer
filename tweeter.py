''' tweet out alphabetized versions of tweets '''
from alphabetizer import alphabetize
import settings
from TwitterAPI import TwitterAPI

api = TwitterAPI(settings.API_KEY,
                 settings.API_SECRET,
                 settings.ACCESS_TOKEN,
                 settings.ACCESS_SECRET)

variants = ['alphabetiz', 'alphabetis']
endings = ['e', 'ing', 'ed', 'er', 'es']
track = ','.join(v+e for v in variants for e in endings)

already_responded = [l for l in open('tweet_log').readlines()]
already_responded = already_responded + [None] * (20 - len(already_responded))
stream = api.request('statuses/filter', {'track': track})

for item in stream.get_iterator():
    try:
        if item['id'] in already_responded or \
           item['user']['screen_name'] == 'alphabotizer':
            continue
        if 'text' in item:
            print '--- I found a tweet! ---'
            text = item['text']
            print text
            tweet_id = item['id']
            user = item['user']['screen_name']
            url = 'https://twitter.com/%s/status/%d' % (user, tweet_id)

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
            already_responded = [tweet_id] + already_responded[:-1]
            f = open('tweet_log', 'w')
            f.write('\n'.join(str(i) for i in already_responded))
            f.close()
    except Exception as oops:
        print oops
