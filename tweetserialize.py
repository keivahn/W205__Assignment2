# Alex Smith
# MIDS - W205

import json # import json module

class TweetSerialize:
    # class to write the tweets from Twitter to a file

    # basic assumptions
    # TWEETS_PER_FILE = 20      # use if we want to chunk the json files
    count = 0
    out = None
    first = False
    current_tweet_count = 0


    def start(self, query, date):
        # bring the program to life

        # increment the self counter by 1
        self.count = self.count + 1

        # create a new file based on the count name
        file_name = "tweets_" + str(query) +"_" + str(date) + ".json"

        # open the file in self.out
        self.out = open(file_name,"w")

        # write a new line, set first to true, and set count to 0
        self.out.write("[\n")
        self.first = True
        self.current_tweet_count = 0

    def end(self):
        # end the program

        # confirm that the program has actually begun, add 2 blank lines to end
        # and close the file
        if self.out is not None:
            self.out.write("\n]\n")
            self.out.close()

        # get out of the file
        self.out = None

    def write(self,tweet):
        # write the tweets to our file

        # if this is not the first tweet, write a new line with a comma seperator
        if not self.first:
            self.out.write(",\n")

        # set the first indicator back to False
        self.first = False

        # write the tweet to the file as a json and increment the tweet count
        self.out.write(json.dumps(tweet._json).encode('utf8'))
        self.current_tweet_count = self.current_tweet_count + 1

        # use only if we want to chunk the json files
        """
        # close and reopen the file if we've reached the hardcoded limit of tweets
        if self.current_tweet_count == self.TWEETS_PER_FILE:
            self.current_tweet_count = 0
            self.end()
            self.start()
        """
