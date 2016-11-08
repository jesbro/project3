# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

'''
References:
https://dev.twitter.com/oauth/overview/single-user
'''

import requests_oauthlib
import tweepy

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


#connecting to Twitter
auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,atsecret)

api = tweepy.API(auth)

#posts status
api.update_with_media(r"C:\Users\Jess\Desktop\SI206\Pro3\project3\media\loco.jpg", "#UMSI206 #Proj3")
