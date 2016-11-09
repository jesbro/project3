# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.


import requests_oauthlib
import tweepy
import json

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
	params = {'q': '10th Planet', 'count' : 2})

rj = r.json()
# print (pretty(rj))
print (rj['statuses'][0]['text'])
print (rj['statuses'][1]['text'])
# for tweet in rj:
# 	print (tweet['statuses'])#['statuses'][0]['text'])

# print("Average subjectivity is")
# print("Average polarity is")
