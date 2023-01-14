import discord

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

import nltk
import numpy as np
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

g = open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/chatbot.txt','r',errors = 'ignore')

raw=g.read()
raw=raw.lower()

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
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    responses.append(message.content)
    with open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/inputs.txt', 'a') as f:
        f.write('\n' + message.content)
                
    if(message.content =='thanks' or message.content =='thank you' or message.content =='thank u'):
        flag=False
        await message.channel.send("No problem.")
    else:
        if(greeting(message.content)!=None):
            await message.channel.send(greeting(message.content))
        else:
            await message.channel.send(response(message.content))
            sent_tokens.remove(message.content)

@client.event
async def on_ready():
    print('AXEL-U is now activated')

    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'#chat-system'
    ))

client.run('MTA2Mzc0MTYxNDU4NzEzODA4OQ.GCDoRh.WVAXw9ecI82GE25f7SBuga06zvlAhd7sc-R938')