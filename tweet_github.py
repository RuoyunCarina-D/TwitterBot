import tweepy

#connect with Twitter API
keys = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': ''
}

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# set a target word or phrase
# double quotes inside single qutes to search for that exact phrase
query = '"winter is cold"' 

# get the tweets
tweet_list = api.search(
    q = query, # phrase to search
    count = 20, # number of tweets to return
    lang = 'en' # language to search (optional)                   
)

#retweet the 20 tweets including target phrase with massage 'cold winter'
for tweet in tweet_list:
    screen_name = tweet.user.screen_name

    message = '@{username} {message}'.format(
        username = screen_name,
        message = 'cold winter'
    )
    
    try:
        api.update_status(
            status = message,
            in_reply_to_status_id = tweet.id
        )
        print message
    except tweepy.TweepError as e:
        print e.message

# when we want to each more keywords/prase in one time #

query_list=(
    ('"what you want to search"', 'what you want to reweet', 'maybe add a image.png'),
    ('"yolo"', 'nice try!','maybe add a image.png')
)          

''' 
I am still working on the following, sorry:
for q in query_list:
    query = q[0]

    tweet_list = api.search(q=query, count=20, lang="en")

    tweets_answered = 0

    for tweet in tweet_list:
        screen_name = tweet.user.screen_name

        # ??? avoid retweets
        if (
            hasattr(tweet, 'retweeted_status') or
            'RT @' in tweet.text or
            api.me().screen_name == screen_name
        ):
            print "this is a retweet, let's try with the next one"

        else:
            message = ".@{username} {message}".format(
                username=screen_name,
                message=alot[1]
            )
            image_path = "media/{image_name}".format(image_name=alot[2])

            # if the tweet is a duplicate an exception is raised
            try:
                # follow the user
                api.create_friendship(screen_name)

                api.update_with_media(
                    filename=image_path,
                    status=message,
                    in_reply_to_status_id=tweet.id
                )

                tweets_answered += 1
                print '{tweets_answered} {query}'.format(
                    tweets_answered=tweets_answered,
                    query=query
                )

                print message

                if tweets_answered >= 2:
                    break

            except tweepy.TweepError as e:
                print e.message[0]['code']
                print e.args[0][0]['code']
'''
