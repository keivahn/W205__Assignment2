# Alex Smith
# MIDS - W205

import json                 # import the json module because the tweets are jsons
import datetime             # import datetime to handle iterating through file dates


class TweetCount:
    # count the number of a query

    # initialize the count to 0
    count1 = 0      # count for query1
    count2 = 0      # count for query2
    count3 = 0      # count for both queries

    def count(self,dictionary,query1,query2):

        # iterate over the dictionary, incrementing the counters based
        # on the below specified conditions
        for tweet_id in dictionary:

            # if the tweet text contains query1 but not query2, increment count1
            if query1 in dictionary[tweet_id] and query2 not in dictionary[tweet_id]:
                self.count1 = self.count1 + 1

            # if the tweet text contains query2 but not query1, increment count2
            if query2 in dictionary[tweet_id] and query1 not in dictionary[tweet_id]:
                self.count2 = self.count2 + 1

            # if the tweet text contains both query1 and query2, increment count3
            if query1 in dictionary[tweet_id] and query2 in dictionary[tweet_id]:
                self.count3 = self.count3 + 1

        # print the counts for reference in our readme
        print str(query1) + " only: " + str(self.count1)
        print str(query2) + " only: " + str(self.count2)
        print str(query1) + " & " + str(query2) + ": " + str(self.count3)
