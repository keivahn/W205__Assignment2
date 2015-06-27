# Alex Smith
# MIDS - W205

import tweepy           # module to help with acquiring data from twitter
import signal           # module to get a async signals from the system
import threading        # locking module to prevent corrupted data
import tweetserialize   # import the function to write the tweets
import threading        # locking module that prevents half written tweets
import datetime         # import the datetime module to separate json files by date
import time             # import time module to help tweepy sleep

# sleep time; the time the application should rest if it encounters an error
# before continuing on, in seconds
SLEEP_TIME = 1000

class TweetAcquire:
    # class to download the tweets based on the specified parameters

    def __init__(self):

        # initialize the lock to prevent half written tweets
        self._lock = threading.RLock()

        # credentials to access twitter account
        consumer_key = "vnfX5Viy6T6Ziaus9U1cZru8J"
        consumer_secret = "ranzXYfdjDxxp6GWRtgJjvxLZyNmvr9f92URim0MgvYpBkYd0U"
        access_token = "101096469-YXAbVs6UmQEV0UtRejz8KKFeqa9gbrhxqHw8aqVC"
        access_token_secret = "5Lm7jDp47LntYMhBQik6O6A7TZ0LXIpoOmZuN3UNNy0iu"

        # apply credentials using tweepy module
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # use the tweepy api to limit the rate of downloads and not
        # be banned
        self.api = tweepy.API(auth_handler = auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

        # call a function to define tasks in the case of user interrupt
        signal.signal(signal.SIGINT, self.interrupt)

    def interrupt(self,signum,frame):
        # interrupt the function, but first finish getting the last tweet

        # use the threading module to finish gathering the last tweet
        print "Please wait, application is gathering last tweet and closing..."
        with self._lock:
            self.serializer.end()

        # exit with code 1 to indicate abnormal exit
        exit(1)

    def search(self, query, begin, end):
        # search for a certain term q

        # run a separate search through Tweepy for each day for
        # the query specified. create a serializer and create the
        # json to which it will write
        current = begin
        current_range = current + datetime.timedelta(days = 1)
        while current <= end:
            self.serializer = tweetserialize.TweetSerialize()
            self.serializer.start(query, current)

            # search the cursor for the search term q within the date range and write the
            # appropriate tweet using serializer's write function
            # use the lock function to ensure the complete tweet is written
            try:
                for tweet in tweepy.Cursor(self.api.search,q=query, since = current, until = current_range).items():
                    with self._lock:
                        self.serializer.write(tweet)

            # when there is an error sleep for 1000 seconds, necessary because
            # sometimes Twitter shuts off the connection
            except BaseException as e:
                print 'Error, program failed: '+ str(e)
                time.sleep(SLEEP_TIME)

            # end the serializer to close and save the file
            # increment current to the next date
            self.serializer.end()
            current = current + datetime.timedelta(days = 1)
            current_range = current + datetime.timedelta(days = 1)
