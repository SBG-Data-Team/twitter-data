from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
import sys
import datetime


access_token = '547497746-pXPwQ0L3owjlkhdWIhAroISkiZl0rGcQfwbyISZE'
access_token_secret='5RZ4psKEx1CeRSJITBAdcAutQEAaoedzKoc3upFeW3lee'
consumer_key='87B5BQ6SqzTjHOBp1M9yKXytT'
consumer_secret='Hf7NEek1tHCz3nQEuIsvsVhZ80R5LoHBBE3IK8btCJFK6GExxZ'

# start_date = datetime.datetime(2017, 1, 1, 0, 0, 0)
# end_date = datetime.datetime(2019, 8, 14, 0, 0, 0)

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    tracklist = ['@StanbicBankGH','#BlueMonday', '#DoYourThing','#BlueCare','stanbic bank']
    # sys.stdout = tweet_data
    stream.filter(track=tracklist)

    

   # with open('stanbic_dataset.csv', 'w') as csvfile:
        #linewriter = csv.writer(tweet_data)
        #linewriter.writerows(tweet_data)


