from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'KltIbyzbglQIbh3trg3ZnA4Ab'
consumer_secret = 'CnEDNnt0Yer9gbguJa4uLgx0sLhCJh3DvQqLVS5sSNbn2zZ9bJ'

access_token = '1274209966052663296-qTmEljT8NYQUSiOs3WGnSLDxjS8UDh'
access_token_secret = 'T0k0Qs8uNO4OMAhqpcl689gAVsJ6ehsYKVowBBBpjctMt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()