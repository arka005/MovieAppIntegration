##http://www.unc.edu/~ncaren/haphazard/sentiment.py
#Setting up Twitter API
import sys
import urllib
import json
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
import string
from collections import Counter
consumer_key='MIhCVhaCeOmvpUVolppG97P8n',
consumer_secret='GXFHOrbvUAzUiYucrJNtVx0caEihQT0pxBxZXqgoeVa4iH1SyY',
access_token='3471712154-ny0pLe4TUT7pMpEkMPFnwKtMZW1mz2G8zYfbRix',
access_token_secret='4BZzGLq9AljkkXBQtiSG2fav0842MuK8RtYXcJy4taqc4'
positive_words=['awesome','good','nice','super','fun']
negative_words=['awfu','lame','horrible','bad']
emotional_words=negative_words+positive_words
##print (emotional_words)

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
##tweet = "RT @marcobonzanini: just an example! :D http://example.com #NLP"
##print(preprocess(tweet))


##This is for the language encoding otherwise it vl throw encoding error
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
 ##To Remove the Stop Words From the Text
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
    #terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
##print(stop)
from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['#garam']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'MIhCVhaCeOmvpUVolppG97P8n',
        consumer_secret = 'GXFHOrbvUAzUiYucrJNtVx0caEihQT0pxBxZXqgoeVa4iH1SyY',
        access_token = 'ny0pLe4TUT7pMpEkMPFnwKtMZW1mz2G8zYfbRix',
        access_token_secret = '4BZzGLq9AljkkXBQtiSG2fav0842MuK8RtYXcJy4taqc4'
     )
    count_all = Counter()

        ##tweet['user']['screen_name'].translate(non_bmp_map), @%s tweeted: %s'
     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        ##print( '%s' % (  tweet['text'].translate(non_bmp_map) ) )
        #words= tweet['text'].translate(non_bmp_map).split(' ')
        #word_count=len(words)
        ##tweet = json.loads(tweet['text'].translate(non_bmp_map)) # load it as Python dict
        ##print(tweet) # pretty-print
        ##terms_stop = [term for term in tweet['text'].translate(non_bmp_map) if term not in stop]
       # word=word_tokenize(tweet['text'].translate(non_bmp_map))
        ##terms_all = [term for term in preprocess(tweet['text'])]
        terms_only = [term for term in preprocess(tweet['text'].translate(non_bmp_map))]
              ##if term not in stop and
              ##not term.startswith(('#', '@'))]
        ##print(terms_only)
        #terms_stop = [term for term in preprocess(tweet['text'].translate(non_bmp_map)) if term not in stop]
        # Count terms only once, equivalent to Document Frequency
        terms_single = set(terms_only)
        # Count hashtags only
        #terms_hash = [term for term in preprocess(tweet['text'].translate(non_bmp_map)) 
              #if term.startswith('#')]
            # Count terms only (no hashtags, no mentions)
        terms_only = [term for term in preprocess(tweet['text'].translate(non_bmp_map)) 
              if term not in stop and
              not term.startswith(('#', '@'))] 
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if 
              # we pass a list of inputs
        count_all.update(terms_only)
    print(count_all.most_common())      
        ##print(terms_only)
        ##print(len(words))
       ## print (words)
        #for word in words:
          #  if word.lower() in positive_words:
                ##print (word)
             #   positive_counter=positive_counter+1
                ##print (positive_counter)
           # elif word.lower() in negative_words:
              #  print(word)
               # negative_counter=negative_counter+1
                
    #positive_counts.append(positive_counter/word_count)
    #negative_counts.append(negative_counter/word_count)

    #print(len(positive_counts))
   # print(len(negative_counts))
    
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

