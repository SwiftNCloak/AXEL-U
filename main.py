from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import nltk
import numpy as np
import random
import string

import pyttsx3
engine = pyttsx3.init()

# Don't forget to comment each line in order to not forget everything.

f = open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/chatbot.txt','r',errors = 'ignore')

raw=f.read()
raw=raw.lower()

verLetter = 'A-'
verNum = '006'

responses = []

# nltk.download('punkt') # first time
# nltk.download('wordnet') # first time
# nltk.download('omw-1.4') # first time

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey", "hey there")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "hey there", "well, hello there"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I apologize... I do not understand what you said. Could you repeat that for me?"
        engine.say(robo_response)
        engine.runAndWait()
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        engine.say(robo_response)
        engine.runAndWait()
        return robo_response

flag=True
print("AXEL-U: My name is " + verLetter + verNum + ". Type 'bye' for the chat to stop. I am still not as advanced as what I am supposed to be, but I'll be learning to improve myself more... I am improving to become better.")

while(flag==True):
    user_response = input("> ")
    user_response=user_response.lower()

    responses.append(user_response)
    with open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/inputs.txt', 'a') as f:
        f.write('\n' + user_response)
            
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' or user_response=='thank u'):
            flag=False
            print("AXEL-U: No problem.")
        else:
            if(greeting(user_response)!=None):
                print("AXEL-U: "+greeting(user_response))
            else:
                print("AXEL-U: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("AXEL-U: Bye! Thank you for talking!")
        engine.say("Bye! Thank you for talking!")
        engine.runAndWait()