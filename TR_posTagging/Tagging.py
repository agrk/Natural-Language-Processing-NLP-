# -*- coding: utf-8 -*-
"""
@author: Asile
"""

#import corpus from kaggle

import nltk 
from nltk.corpus import stopwords 

text = open("150.txt","r", encoding = 'utf-8')   # We defined our corpus about intermitten fasting
corpus=text.read()


#%% 

import re
import nltk as nlp
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
from nltk.tag import pos_tag
from nltk import FreqDist
from nltk.corpus import treebank


# description_list = []
first_tagged_token = []
second_tagged_token = []


tagged1=[]
tagged2=[]

#%%

# Cleaning processing

corpus = re.sub("^[a-zA-Z0-9ğüşöçİĞÜŞÖÇ]+$",' ',corpus)
corpus = re.sub(r'[^\w]', ' ', corpus)
corpus = corpus.lower()
corpus = nltk.word_tokenize(corpus) 
corpus = [ word for word in corpus if not word in set(stopwords.words('turkish'))]

#%%

print(nltk.help.upenn_tagset('JJ'))

print(nltk.help.upenn_tagset('VB.*'),"\n")


#%%

tagged1=pos_tag(corpus)

print(tagged1)

#%%

tagged2=pos_tag(corpus, tagset='universal')
print(tagged2)


#%%


tag_count = nltk.FreqDist(tag for (word, tag) in tagged1)
print(tag_count.most_common())


#%%

tag = {}
print(tag)

tag['beslenme'] = 'ADJ'
print(tag)

tag['aralıklı'] = 'ADV'
tag['yapmanız'] = 'VERB'
tag['kilo'] = 'NOUN'
print(tag)



#%%

def n_gram(corpus,n):
    
    n_grams = ngrams(corpus,n)
        
    ngramsFrequency = Counter(n_grams)
     
    valuesOfngrams = list(ngramsFrequency.values())
    ngramlist = list(ngramsFrequency)
    for i in range(0,len(ngramlist)):
        if valuesOfngrams[i] >= n:
            second_tagged_token.append( nltk.pos_tag(ngramlist[i]))
            print(ngramlist[i], "  ", valuesOfngrams[i], " ")

#%%

bigram = n_gram(corpus,2)


           
#%%

trigrams = n_gram(corpus,3)


#%%









