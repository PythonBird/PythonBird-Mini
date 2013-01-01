#!/usr/bin/env python

'''
author: Diego Pignattini
last update: December the 31th 2012 
version: 0.1
'''

import tweepy
from auth import startAuth

#Authorize this application
api = startAuth()

#Get yourself's object
myself = api.me()

#Sends a tweet
def tweet():
        while True:
                print "Compose new Tweet..."
                tweet = raw_input()
                if tweet == 'exit' or tweet == 'Exit':
                        break
                while len(tweet) > 140:
                    print ("The tweet must be less or equal to 140 characters")
                    tweet = raw_input("Insert your tweet: ")
                api.update_status(tweet)


def begin():
        print ''
        print ('==============================================================')
        print ('WELCOME TO PYTHONBIRD MINI, A (MINI) PYTHON-SHELL TWITTER TOOL')
        print ('==============================================================')
        print ''
        print 'Hello', myself.screen_name
        print ('______________________________________________')
        tweet()

        
if __name__=="__main__":
        begin()
