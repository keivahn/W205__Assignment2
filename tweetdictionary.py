# Alex Smith
# MIDS - W205

import datetime         # import datetime to handle iterating through file dates
import json             # import the json module because the tweet files are jsons
import pickle           # import the python pickle module to export the dictionary

class TweetDictionary:
    # class to create a dictionary of all tweets with id's

    def create(self,query1,query2,begin,end,file):

        # create a new dictionary to store our tweets and tweet id's in
        tweetdict = {}

        # set the current file to begin so that we can loop through the
        # first query
        current = begin

        # open the file as readable and create a new dictionary to store all
        # of the text from the tweets. loop through all the files for a given
        # query
        while current <= end:
            file_name = "tweets_" + query1 + "_" + str(current) + ".json"
            file = open(file_name,"r")
            json_file = json.load(file)

            # pull each tweet and write it's contents to the dictionary
            # we choose to encode its contents as unicode to deal with characters from
            # other languages and the problems that creates for our dictionaries
            for tweet in json_file:
                tweet_id = tweet["id"]
                tweet_text = str(tweet["text"].encode('utf-8'))
                tweetdict[tweet_id] = tweet_text

            current = current + datetime.timedelta(days=1)


        # repeat the same process for the second query
        current = begin
        while current <= end:
            file_name = "tweets_" + query2 + "_" + str(current) + ".json"
            file = open(file_name,"r")
            json_file = json.load(file)

            for tweet in json_file:
                tweet_id = tweet["id"]
                tweet_text = str(tweet["text"].encode('utf-8'))
                tweetdict[tweet_id] = tweet_text

            current = current + datetime.timedelta(days=1)

        # save the tweet dictionary as an output for later use
        pickle.dump(tweetdict,open(file, "wb"))

        # return the dictionary to the calling program
        return tweetdict
