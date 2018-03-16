"""
tweets a sonnet everyday
"""
import tweepy
from credentials import *
from time import sleep

sonnetsPath = 'sonnets.txt'
sleepTime = 24*1000

def authenticate():
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)

    return api

def loadSonnets(sonnetsPath):
    sonnetsFile = open(sonnetsPath,'r')
    sonnets = sonnetsFile.readlines()
    sonnetsFile.close()

    return sonnets

def tweet(api,line):
    try:
        api.update(line)
        sleep(20)
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(5)

def loop():
    lineCount = 0
    sonnets = loadSonnets(sonnetsPath)
    api = authenticate()

    for line in sonnets:
        if lineCount > 14:
            sleep(sleepTime)
            lineCount = 0

        if line == "End of Project Gutenberg's Shakespeare's Sonnets, by William Shakespeare\n":
            print('ended')
            return

        if line[0] != '#' and line[0]!='\n':
            print(line)
            tweet(api)
            lineCount +=1

if __name__ == '__main__':
    loop()
