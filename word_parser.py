from math import log
import string
import re

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).

words = open("words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

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
    
    def has_digit(s):
        return bool(re.search(r'\d', s))

    phrases = s.split(',')

    new_phrases = []

    for phrase in phrases:

        # Remove other punctuation
        phrase = phrase.translate({ord(i):None for i in string.punctuation})

        # Avoid including numbers when separating
        if has_digit(phrase):
            new_phrase_list = re.findall(r'\d+|\D+', phrase)
            new_phrase_list = [infer_spaces(word.replace(' ','').lower()) if not has_digit(word)
                                else word for word in new_phrase_list]
            new_phrases.append(' '.join(new_phrase_list))

        else:
            phrase = phrase.replace(' ','').lower()
            phrase = infer_spaces(phrase)
            new_phrases.append(phrase)


    s = ', '.join(new_phrases)

    return s