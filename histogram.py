# Alex Smith
# MIDS - W205

import json     # import json module
import nltk     # import natural language toolkit module to analyze words in tweets

class Histogram:
    # create class to create historgram of words in tweets

    def create(self,dictionary,query1,query2):
        # method to create find the word counts

        # create 3 lists that we will append all tweets to
        list_query1 = []
        list_query2 = []
        list_both_q = []

        # loop through every tweet that we have stored
        for tweet_id in dictionary:

            # if the tweet text contains query1 but not query2, append to list
            if query1 in dictionary[tweet_id] and query2 not in dictionary[tweet_id]:
                list_query1.append(dictionary[tweet_id])

            # if the tweet text contains query2 but not query1, append to list
            if query2 in dictionary[tweet_id] and query1 not in dictionary[tweet_id]:
                list_query2.append(dictionary[tweet_id])

            # if the tweet text contains both query1 and query2, append to list
            if query1 in dictionary[tweet_id] and query2 in dictionary[tweet_id]:
                list_both_q.append(dictionary[tweet_id])

        # combine each list into a single string for tokenization
        space = " "
        str_query1 = " ".join(list_query1)
        str_query2 = " ".join(list_query2)
        str_both_q = " ".join(list_both_q)

        # convert all into unicode and ignore those symbols that we
        # cannot convert
        str_query1 = unicode(str_query1,errors="ignore")
        str_query2 = unicode(str_query2,errors="ignore")
        str_both_q = unicode(str_both_q,errors="ignore")

        # tokenize the string for counting
        token_query1 = nltk.word_tokenize(str_query1)
        token_query2 = nltk.word_tokenize(str_query2)
        token_both_q = nltk.word_tokenize(str_both_q)

        # create a frequency distribution for each tokenized string
        dist_query1 = nltk.FreqDist(token_query1)
        dist_query2 = nltk.FreqDist(token_query2)
        dist_both_q = nltk.FreqDist(token_both_q)

        # create a csv file for each query
        file_query1 = query1 + ".csv"
        file_query2 = query2 + ".csv"
        file_both_q = query1 + "_&_" + query2 + ".csv"

        # treat the frequency distribution as a dictionary and loop over
        # it, writing to the appropriate file
        file_query1=open(file_query1,"w")
        for word in dist_query1:
            file_query1.write(word + ", " + str(dist_query1[word]) + "\n")
        file_query1.close()

        file_query2=open(file_query2,"w")
        for word in dist_query2:
            file_query2.write(word + ", " + str(dist_query2[word]) + "\n")
        file_query2.close()

        file_both_q=open(file_both_q,"w")
        for word in dist_both_q:
            file_both_q.write(word + ", " + str(dist_both_q[word]) + "\n")
        file_both_q.close()
