import tweepy
from tweepy import OAuthHandler
import json
import os
import io
import urllib.request
import mysql3
import mongoDB3
from google.cloud import vision
from PIL import Image,ImageFont,ImageDraw

def twi():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    #authorize twitter, initialize tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    count = 20
    tweets = api.user_timeline(screen_name='kriswu',
                               count=20, include_rts=False,
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

        # The ImageAnnotatorClient class within the google.cloud.vision library for accessing the Vision API.
    client = vision.ImageAnnotatorClient()

    mysql3.create()
    mongoDB3.clear_base()
    for i in range(num):
        file_name = os.path.join(
            os.path.dirname(__file__),
            'img%03d.jpg'%i)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        str = ''
        newtag = ''
        for label in labels:
            str = str + label.description + '\n' #tag
            newtag = newtag + label.description + ','
        print(newtag)

        im = Image.open(file_name)

        ttfront= ImageFont.truetype("/Users/shiluwu/Documents/EC601/miniproject1/twitter/abcd.ttf", 20)
        draw = ImageDraw.Draw(im)
        x,y=(100,100)
        draw.text((x,y), str, fill=(255,97,0), font=ttfront)
        im.save(file_name)
        #print(str)
        print(len(media))
        #print('len media num fl')
        print(num)
        fl = ''
        fl = fl + file_name
        mysql3.mysql(count,num,fl,newtag)
        mongoDB3.mongoDb(count,num,fl,newtag)




if __name__ == '__main__':
    twi()

    os.popen('ffmpeg -r 0.5 -i img%03d.jpg -vf scale=500:500 -y -r 30 -t 60 out.mp4')

