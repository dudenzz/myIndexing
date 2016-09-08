__author__ = 'Asus'

from scipy.spatial.distance import cosine
from math import log
from math import e


def highest(word, text, vsm):
    max = 0
    wret = ''
    for w in text.split():
        try:
            a = 1-cosine(vsm.word_vectors[vsm.dictionary[w]],vsm.word_vectors[vsm.dictionary[word]])
            if a>max:
                max = a
                wret = w
        except:
            b = 0
    return [max,wret]

wiki_lnt = 3977901

def IDF(frequencies, word):
    return log(wiki_lnt/float(frequencies[word]))


def compare(wnText,wikiText,avgWnLnt,freq,vsm,k1,b):
    sum = 0;
    lnt = len(wikiText.split())
    for w in wikiText.split():
        sum += float(IDF(freq,w))*((highest(w,wnText,vsm)[0]*(k1+1))/(highest(w,wnText,vsm)[0]+k1*(1-b+b*lnt/avgWnLnt)))
    return sum