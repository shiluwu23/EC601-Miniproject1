import tweepy
from tweepy import OAuthHandler
import json
import os

consumer_key = 'Dg0ZvE3Ygu0sI9gQXBSCrPEdA'
consumer_secret = 'j17lBGBXtvUStt8kaCWBD0hbvUfndiey023v3lApTPq3nRaB4A'
access_token = '1040342641249013760-qSLxHrQjoff84GZOOjHgcNMlOgedzC'
access_secret = 'BhxGNaAfOfOhooT16UpB7nXmkuuVILt37KVeGi828PDp7'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='KrisWu',
                           count=200, include_rts=False,
                           exclude_replies=True)
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

import wget

for media_file in media_files:
        wget.download(media_file)

os.popen('ffmpeg -r 0.5 -i img%03d.jpg -vf scale=500:500 -y -r 30 -t 60 out.mp4')
