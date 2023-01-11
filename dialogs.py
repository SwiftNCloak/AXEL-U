responses = []
while True:
    print("DATA GATHERING STARTED | Dialog method")
    response = input("Please enter your response (or 'q' to quit): ")
    if response == 'q':
        break
    responses.append(response)

with open('C:/Users/Mark James/Desktop/COMSCI LABS/artificial-intelligence-lab/chatbot-1/AXEL-U/chatbot.txt', 'a') as f:
    for response in responses:
        f.write('\n\n' + response)
print("AXEL-U dialogs are now placed in chatbot.txt")