# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

"""
References:
lecture code/Colleen's github code
"""


import requests_oauthlib
import tweepy
import json
from textblob import TextBlob

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

#keeping my creds off github
f = open("twitterOauth.txt")

ckey, csecret, atoken, atsecret = f.readlines()

ckey = ckey.strip()
csecret = csecret.strip()
atoken = atoken.strip()
atsecret = atsecret.strip()

f.close()

oauth = requests_oauthlib.OAuth1Session(ckey,
                        client_secret=csecret,
                        resource_owner_key=atoken,
                        resource_owner_secret=atsecret)

#connecting to Twitter
r = oauth.get("https://api.twitter.com/1.1/search/tweets.json", 
	params = {'q': 'election', 'count' : 5})

rj = r.json()
polarity = 0.0
subj = 0.0

for val in range(len(rj['statuses'])):
	tweet = rj['statuses'][val]['text']
	print ('\n', tweet.encode("ascii", "ignore").decode("utf-8"))

	analysis = TextBlob(tweet)

	polarity += analysis.polarity
	subj += analysis.subjectivity

polarity /= len(rj['statuses'])
subj /= len(rj['statuses'])


print("\nAverage subjectivity is", round(subj, 4))
print("Average polarity is", round(polarity, 4))
