from math import log
import string
import re
from itertools import tee
from collections import Counter
import pandas as pd

# Cost dictionary using Zipf's law and cost = -math.log(probability).

words = open("words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

# From Generic Human / StackOverflow
def infer_spaces(s):
    #Infer the location of spaces in a string without spaces.

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

def separate_merged_words(s):
    
    # Remove other punctuation
    s = s.translate({ord(i):None for i in string.punctuation})
    # Remove digits
    s = s.translate({ord(i):None for i in string.digits})
    # Remove spaces and lower
    s = s.replace(' ','').lower()
    # Infer spaces on merged text
    s = infer_spaces(s)

    return s

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def most_common_pairs_df(iterable):

    pairs = Counter([pair for sublist in iterable
         if type(sublist) == str
         for pair in pairwise(sublist.split())])

    most_common_pairs = pairs.most_common()

    df = pd.DataFrame(most_common_pairs, columns = ['pair', 'count'])

    return df