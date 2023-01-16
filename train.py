import nltk
from nltk.util import ngrams
from nltk.lm import MLE

# Initialize an empty list to store the user inputs
user_inputs = []

# Chatbot loop
while True:
    # Get user input
    user_input = input("You: ")
    if user_input == 'exit':
        break
    # Append user input to the list
    user_inputs.append(user_input)
    # Tokenize the user inputs
    tokens = nltk.word_tokenize(" ".join(user_inputs))
    # Create a list of trigrams
    trigrams = list(ngrams(tokens, 3))
    # Create a language model using Maximum Likelihood Estimation
    lm = MLE(3)
    # Train the language model on the trigrams
    lm.fit(trigrams)
    # Use the trained model to generate a response
    response = lm.generate(30)
    print("Chatbot: " + " ".join(response))
