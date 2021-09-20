from modelo_matematico import predict_tweet
from processamento import dict_to_list, process_tweet


class TermoBusca:
    def __init__(self, twitter_client, freqs, theta):
        self.twitter_client = twitter_client
        self.freqs = freqs
        self.theta = theta

    def make_list_positives_and_negatives_regression(self, termo):
        tweets = self.twitter_client.get_tweets(query=termo, count=50)
        tweets = dict_to_list(tweets)

        lista_positiva_regression = []
        lista_negativa_regression = []

        for i in tweets:
            tweet_tratado = process_tweet(i)
            tweet_str = ' '.join([str(item) for item in tweet_tratado])
            y_hat = predict_tweet(tweet_str, self.freqs, self.theta)
            if y_hat >= 0.75:
                lista_positiva_regression.append(i)
                '''
                pontos_pos = y_hat
                if pontos_pos >= pontos_pos_corte:
                    tweet_legal = str(i)
                    pontos_pos_corte = pontos_pos
                '''
            else:
                if y_hat <= 50:
                    lista_negativa_regression.append(i)
                '''
                if y_hat < pontos_neg:
                    tweet_chato = str(i)
                    pontos_neg = y_hat
                '''
        return lista_positiva_regression, lista_negativa_regression
