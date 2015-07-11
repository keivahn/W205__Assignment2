# Alex Smith
# MIDS - W205

import boto                     # import boto to use the command line to connect to Amazon Web Services
from boto.s3.key import Key     # import the Key function of the boto module to set the specific file in the bucket

AWS_ACCESS_KEY = ""
AWS_SECRET_ACCESS_KEY = ""
BUCKET_NAME = "keivahn-w205-assignment2"

class TweetS3:
    # create a class to upload file to Amazon S3

    def upload(self,file):
        # upload the the file to AWS S3

        # open the file
        file = open(file,"r")

        # establish a connection with AWS using credentials in constants
        # get the specific we're interested in, also from constants
        # use the key function to create a key and send the contents of the
        # local file to S3
        connection = boto.connect_s3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY,host='s3-us-west-1.amazonaws.com')
        bucket = connection.get_bucket(BUCKET_NAME)
        Key(bucket).set_contents_from_file(file)

        # close the file to cleanly end this class
        file.close()
