import time 
import tweepy
import os
import random

dirname = os.path.dirname(os.path.abspath(__file__))
# read files and parse into lists
drakequotesfile = open(os.path.join(dirname, 'drake_quotes.txt'), "r+")
drakequotesdata = drakequotesfile.read()
drakequotes = drakequotesdata.split("\n")
wisquotesfile = open(os.path.join(dirname, 'quotes.txt'), "r+")
wisquotesdata = wisquotesfile.read()
wisquotes = wisquotesdata.split("\r\n\r\n")
officequotesfile = open(os.path.join(dirname, 'office_quotes.txt'), "r+")
officequotesdata = officequotesfile.read()
officequotes = officequotesdata.split("\n \n")

#duplicate each list because one will be getting editted with each tweet
wisquotes_dup = wisquotes
drakequotes_dup = drakequotes
officequotes_dup = officequotes

# Consumer Key (API Key)
cons_key = 
# Consumer Secret (API Secret)
cons_secret = 
# Access Token
access_token = 
# Access Token Secret
access_token_secret = 

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
    
# Enter user name here
user = api.get_user('<your_username>')
#print user.screen_name
#print user.followers_count
#for friend in user.friends():
   #print friend.screen_name

onehalfhours = 60*60*1.5
twohours = 60*60*2
sevenhours = 7*60*60
while True:
    year, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')
    if hour > 3 and hour < 7:
        time.sleep(300)
        continue
        
    i = random.randint(1,3)
    
    if i % 3 == 0:
        if len(wisquotes) == 0:
            wisquotes = os.path.join(dirname, 'quotes.txt').split("\r\n\r\n")
            print "~~~~~~ ALL WISDOM QUOTES TWEETED ~~~~~~"
        quote = wisquotes.pop(random.randint(0, len(wisquotes) - 1))
        #wisquotesdata.replace(quote, "")
        #wisquotesfile.write(wisquotesdata)
          
    elif i % 3 == 1:
        if len(officequotes) == 0:
            officequotes = open(officequotesfile, "r").read().split("\n\n")
            print "~~~~~~ ALL OFFICE QUOTES TWEETED ~~~~~~"
        quote = officequotes.pop(random.randint(0, len(officequotes) - 1))
        #officequotesdata.replace(quote, "")
        #officequotesfile.write(officequotesdata)
        
    else:
        if len(drakequotes) == 0:
            drakequotes = open(drakequotesfile, "r").read().split("\n")
            print "~~~~~~ ALL DRAKE QUOTES TWEETED ~~~~~~"
        quote = drakequotes.pop(random.randint(0, len(drakequotes) - 1))
        #drakequotesdata.replace(quote, "")
        #drakequotesfile.write(drakequotesdata)
            
    if len(quote) <= 140:
        try:
            print
            api.update_status(quote)
        except Exception, e:
            pass
        print "tweet posted at ", str(year), str(month), str(day), str(hour) + ":" + str(minute)
        print quote
        time_til_next_tweet = random.randint(twohours, sevenhours)
        print "Posting next tweet in " + str(time_til_next_tweet/60) + " minutes"
        time.sleep(time_til_next_tweet)