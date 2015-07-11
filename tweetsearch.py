# Alex Smith
# MIDS - W205
# This program searches for tweets within a given date range
# for all tweets containing two queries.

import sys                  # import the system module, read command line arguments
import urllib               # import module to interact with web
import datetime             # import module to manipulate date and time formats
import tweetacquire         # import tweetacquire class to search for tweets
import tweetdictionary      # import tweetdictionary class to create a dictionary of our tweets
import tweetcount           # import tweetcount class to count the instances of each query
import histogram            # import histogram class to create plot of word counts
import tweetS3              # import tweetS3 class to send output to AWS S3

# get today's date and set range of 1 week for pulling relevant tweets
TODAYS_DATE = datetime.date.today()
ACCEPTABLE_RANGE = datetime.timedelta(days=6)
START = TODAYS_DATE - ACCEPTABLE_RANGE
END = TODAYS_DATE

# define two hashtags (queries) that we want to find
QUERY1 = "#NBAFinals2015"
QUERY2 = "#Warriors"

# name the output file for storing our tweets and later retrieval
OUTPUT_FILE = "tweet_output.p"

if __name__ == "__main__":
    # check to see if this function is the main function being called

    # call our acquire function and use it to search the queries
    acquire = tweetacquire.TweetAcquire()
    query1 = urllib.quote_plus(QUERY1)
    query2 = urllib.quote_plus(QUERY2)
    begin = START
    end = END
    acquire.search(query1,begin,end)
    acquire.search(query2,begin,end)

    # create a dictionary to store all our tweets by tweet id
    mytweetdictionary = tweetdictionary.TweetDictionary().create(query1,query2,begin,end,OUTPUT_FILE)

    # call our count function on our dictionary to count the number
    # of instances of each query alone and the number of instances of
    # both queries together; we use non-urllib queries because when we are
    # searching the original text
    tweetcount.TweetCount().count(mytweetdictionary,QUERY1,QUERY2)

    # create a histogram of words, write each word and its frequency
    # to a csv file; creates 3 csv files, one for tweets with only the
    # first query, one for tweets with only the second query, and one
    # for tweets with both queries
    histogram.Histogram().create(mytweetdictionary,QUERY1,QUERY2)

    # send tweet output to Amazon S3 for others to use
    tweetS3.TweetS3().upload(OUTPUT_FILE)
