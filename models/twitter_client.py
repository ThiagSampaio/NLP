import tweepy
from tweepy import OAuthHandler
import json


class TwitterClient(object):
    def __init__(self):
        # tokens
        # TODO: Colocar em variável de ambiente (os.environ.get('TWITTER_CONSUMER_KEY'), etc)
        consumer_key = 'wF27dQviNlbJrkS4pS5c07ClP'
        consumer_secret = 'kjQDLQIoDCbOYYOcPGnHKiEJAjUQjTRgCfSLfanUBWWABCjrXq'
        access_token = '1378491084800729094-7moBwIU09BE92u3nx7xZHPQec5Lyd1'
        access_token_secret = 'yZyWBa6NQH16q6UvcrVbNYZAy1GtQuZ2Z48xZswQCqycv'

        # tentativa de autenticação
        try:
            # create OAuthHandler object
            auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(auth)
        except:
            print("Error: Authentication Failed")

    def on_status(self, status):

        """
        Função para pegar o tweet por inteiro -  feita em 13/07/2021
        """

        if hasattr(status, "retweeted_status"):  # Checando se é um  Retweet
            try:
                return status.retweeted_status.extended_tweet["full_text"]
            except AttributeError:
                return status.retweeted_status.full_text
        else:
            try:
                return status.extended_tweet["full_text"]
            except AttributeError:
                return status.full_text

    def get_tweets(self, query, count=10):
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count, result_type="mixed", tweet_mode='extended')

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # saving text of tweet
                parsed_tweet = {}

                parsed_tweet['text'] = self.on_status(tweet)
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

    # Futuro/ análise de  top trends
    def get_trends(self):

        try:
            BRAZIL_WOE_ID = 23424768

            brasil_trends = self.api.trends_place(BRAZIL_WOE_ID)

            trends = json.loads(json.dumps(brasil_trends, indent=1))

            return trends

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
