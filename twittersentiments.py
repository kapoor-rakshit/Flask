#importing various modules
import requests
import sys
import datetime
import time
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
#from tweepy.streaming import StreamListener
import json
from flask import *

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results',methods=['post'])
def result():
	tweets=[]
	pos=[]
	neg=[]
	neut=[]
	#make ur app on twitter and get ur ckey,csecret,accesskey,accesstoken.
      #enter consumer key, consumer secret, access token, access secret.
	ckey="EKrGrMl9SbG0Qa3n1kvHxDwcp"
	csecret="FtQdtFA8exg2yw4ZnwqOu0iRF2ThAFXLCbs0pDIrSGmL9XnV80"
	atoken="851461746212487173-YBoswsGwa43pYWNJYG1h70zrEw6mZa0"
	asecret="7zWOG2clH5muUebUfJM3dpCLzaEy8pKIoLRhEeYYDXBbu"
	#to interact with sentiment analysis api

	auth = OAuthHandler(ckey,csecret)
	auth.set_access_token(atoken,asecret)
	api = tweepy.API(auth)

	url = 'http://text-processing.com/api/sentiment/'
	name=request.form['keyword']
	st = time.time()
	u=datetime.date.today()
	for tweet in tweepy.Cursor(api.search,q=name,since=u-datetime.timedelta(2),until=u,lang='en').items():
		s = tweet.text
		tweets.append(s)
		r = requests.post(url,{'text':s})
		js = json.loads(r.text[:])
		pos.append(str(js['probability']['pos']*100) + " %")
		neg.append(str(js['probability']['neg']*100) + " %")
		neut.append(str(js['probability']['neutral']*100) + " %")
		if time.time()-st>60:
			break
	if len(tweets)==0:
		tweets.append("Sorry! No results for this keyword...")
		pos.append(0)
		neg.append(0)
		neut.append(0)
	fdata=zip(tweets,pos,neg,neut)     
	return render_template('results.html',tweetdet=fdata)


if __name__=='__main__':
    app.debug=True
    app.run()
