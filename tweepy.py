import tweepy
from tweepy import OAuthHandler
import json
import os
import urllib.request

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='KrisWu',
                           count=10, include_rts=False,
                           exclude_replies=True)
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

num=0
for media_file in media_files:
    save_name = 'img%03d.jpg'%num
    urllib.request.urlretrieve(media_file,save_name)
    num = num + 1

os.popen('ffmpeg -r 0.5 -i img%03d.jpg -vf scale=500:500 -y -r 30 -t 60 out.mp4')
