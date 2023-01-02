from . import tweets
import time


def starting_file():
    tweets.electronics()
    #API can fetch 900 tweets in 15 minutes so giving some time to start the process for next tweet
    time.sleep(5*60)
    tweets.shoes()
    #API can fetch 900 tweets in 15 minutes so giving some time to start the process for next tweet
    time.sleep(5*60)
    tweets.fashion()
    #API can fetch 900 tweets in 15 minutes so giving some time to start the process for next tweet
    time.sleep(5*60)
    tweets.phones()

