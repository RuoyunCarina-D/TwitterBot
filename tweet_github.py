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
    ('"yolo"', 'nice try!')
)          
