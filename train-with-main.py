from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import nltk
import numpy as np
import random
import string

from nltk.util import ngrams
from nltk import word_tokenize
from nltk.lm import MLE
from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline

verLetter = 'U-'
verNum = 'EXPERIMENT'

with open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/chatbot.txt', "r") as file:
    contents = file.read()

flag=True
print("AXEL-U: My name is " + verLetter + verNum + ". Type 'bye' for the chat to stop. I am still not as advanced as what I am supposed to be, but I'll be learning to improve myself more..")

while(flag==True):
    paddedLine = [list(pad_both_ends(word_tokenize(contents), n=3))]

    train, vocab = padded_everygram_pipeline(3, paddedLine)

    lm = MLE(3)

    clean_text = contents.replace('<s>','').replace('</s>','')
    token =  ['<s>'] + nltk.word_tokenize(clean_text) + ['</s>'] + nltk.word_tokenize(clean_text)
    lm.fit(train, vocab)

    generated_sentence = lm.generate(20)
    # If sentence input is short, then response is short

    user_response = input("> ")
    user_response=user_response.lower()
    print(" ".join(generated_sentence) + '\n----------------------')