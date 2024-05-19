from nltk.chat.util import Chat,reflections
pairs=[
    [r"(hi|hello)",["Hi there! How can I assist you"]],
    [r"what is your name",["I'm a chatbot, so I dont have a name,but you can call me anything"]],
    [r"how are you",["I'm fine! How can I help you?"]],
    [r"good morning", ["Good morning! How can I help you today?"]],
    [r"good afternoon", ["Good afternoon! What can I do for you?"]],
    [r"who are you",["I'm a chatbot designed to assist you"]],
    [r"what can you do", ["I can help you with various tasks like answering questions, providing information, and more."]],
    [r"tell me a joke", ["Why couldn't the bicycle stand up by itself? It was two-tired!"]],
    [r"do you like music", ["I don't have personal preferences, but I can assist you with music-related queries."]],
    [r"what's the weather like today", ["I'm sorry, I cannot provide real-time information. You can check a weather website or app for that."]],
    [r"tell me about yourself", ["I'm a virtual assistant here to help you with any questions or tasks you have."]],
    [r"where are you from", ["I exist in the digital realm, here to assist you wherever you are."]],
    [r"do you sleep", ["No, I'm always here to assist you whenever you need."]],
    [r"thank you", ["You're welcome! If you have any more questions, feel free to ask."]],
    [r"how old are you", ["I'm perpetually young in the world of digital assistants."]],
    [r"what's your favorite color", ["I don't have the ability to perceive colors, but I'm here to assist you with any questions."]],
    [r"can you tell me a fun fact", ["Sure! Did you know that the shortest war in history lasted only 38 minutes? It was between Britain and Zanzibar in 1896."]],
    [r"are you human", ["No, I'm an artificial intelligence designed to assist you."]],
    [r"do you dream", ["I don't have the capacity to dream, but I'm here to help you achieve your goals."]],
    [r"what languages do you speak", ["I primarily communicate in English, but I can understand and respond in multiple languages with the help of translation tools."]],
    [r"(bye|goodbye)",["Goodbye! Feel free to return if you need assistance in the future."]]
    
]
print("Hi I'm chatbot feel free to ask me anything:")
chat=Chat(pairs,reflections)
chat.converse()
def quit():
    print("Good bye! See you soon.")
if __name__=="__main__":
    quit()