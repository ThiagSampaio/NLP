import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import string
from nomes_brasileiros import get_lista_nomes

lista_names = get_lista_nomes()


def dict_to_list(d):
    lista_tweets = []
    print(d)
    for item in d:
        lista_tweets.append(item["text"])
    return lista_tweets


def process_tweet(tweet):
    """Função de processamento de um tweet.
    Input:
        tweet: a string contendo o tweet
    Output:
        tweets_clean: uma lista de palavras contendo o tweet processado

    """
    # pegando lista de palavras stopwords
    stopwords_portuguese = stopwords.words('portuguese')

    # remove tickers do mercado de ações como $ GE
    tweet = re.sub(r'\$\w*', '', tweet)

    # remove o texto retweetado no estilo antigo "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)

    # remove hyperlinks
    tweet = re.sub(r'https?://.*[\r\n]*', '', tweet)

    # remove hashtags
    tweet = re.sub(r'#', '', tweet)

    # remove os @
    tweet = re.sub(r'@', '', tweet)

    # remove os emojis
    '''
    padrao_emoji = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # dingbats
                                u"\u3030"
                            "]+", flags=re.UNICODE)
    tweet = re.sub(padrao_emoji, '', tweet)
    '''
    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []

    for word in tweet_tokens:
        if (
                word not in stopwords_portuguese and  # remove stopwords
                word not in string.punctuation and  # remove pontuação
                word not in lista_names  # remove nomes
        ):
            tweets_clean.append(word)

    return tweets_clean
