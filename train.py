import nltk
from nltk.util import ngrams
from nltk import word_tokenize
from nltk.lm import MLE
from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline

with open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/chatbot.txt', "r") as file:
    contents = file.read()

paddedLine = [list(pad_both_ends(word_tokenize(contents), n=2))]

train, vocab = padded_everygram_pipeline(2, paddedLine)

lm = MLE(2)

clean_text = contents.replace('<s>','').replace('</s>','')
token =  ['<s>'] + nltk.word_tokenize(clean_text) + ['</s>'] + nltk.word_tokenize(clean_text)
lm.fit(train, vocab)

generated_sentence = lm.generate(20)
while len(generated_sentence) <= 20:
    generated_sentence = lm.generate(20)

with open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/train-data.txt', 'a') as f:
        f.write(f'\n{generated_sentence}')

print(" ".join(generated_sentence))