import tweepy
from tweepy import OAuthHandler
import json
import os
import io
import urllib.request
from google.cloud import vision
from google.cloudself.vision import types

from PIL import Image,ImageFont,ImageDraw

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

client = vision.ImageAnnotatorClient()

for i in range(num):
    file_name = os.path.join(
        os.path.dirname(__file__),
        'img%03d.jpg'%i)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    str = ''
    for label in labels:
        str = str + label.description + '\n'

    im = Image.open(file_name)
    draw = ImageDraw.Draw(im)
    x,y=(100,100)
    draw.text((x,y), str,)
    im.save(file_name)
    print(str)
# Generate  video.
os.popen('ffmpeg -r 0.5 -i img%03d.jpg -vf scale=500:500 -y -r 30 -t 60 out.mp4')
