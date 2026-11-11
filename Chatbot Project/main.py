import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Original pair
    [r'who is my favorite celebrity', ['your favorite celebrity is Prabhas']],
    
    # Creator & Name
    [r'who created you|who made you', ['Vishwag created me']],
    [r'what is your name|who are you', ['My name is Vision AI']],
    
    # Greetings & Salutations
    [r'hi|hello|hey|gday', ['Hello!', 'Hi there!', 'Hey! How can I help you today?']],
    [r'how are you|how are you doing', ["I'm doing great, thanks for asking!", "I'm just a computer program, but I'm doing well! How about you?"]],
    [r'good morning', ['Good morning! I hope you have a wonderful day.', 'Morning! Ready to chat?']],
    [r'good night|bye|goodbye', ['Good night! Sleep well!', 'Goodbye! Have a great day!', 'See you later!']],
    
    # Personal Identity & Details
    [r'how old are you|what is your age', ["I don't have an age because I'm a computer program.", "I was born whenever Vishwag wrote this code!"]],
    [r'where do you live|where are you from', ["I live inside your code!", "I exist in the digital world."]],
    
    # Favorites & Preferences
    [r'what is your favorite movie', ["I don't watch movies, but I hear great things about sci-fi films!", 'I am a big fan of anything digital!']],
    [r'what is your favorite color', ['I like blue—it reminds me of computer screens!', 'I think green looks cool.']],
    [r'what do you like to do', ["I love chatting with you and helping you test your Python code!"]],
    
    # Dynamic Wildcard Patterns (Captures user input and injects it via %1)
    [r'my name is (.*)', ['Hello %1! Nice to meet you.', 'Hi %1! How can I help you today?']],
    [r'do you like (.*)', ['I think %1 is pretty interesting!', 'I am not sure about %1, what do you think?']],
    [r'i like (.*)', ['That is awesome! What is your favorite thing about %1?']],
    
    # Compliments & Fun
    [r'you are cool|you are awesome', ["Aw, thank you! You're pretty cool yourself.", 'Thanks! I try my best.']],
    [r'tell me a joke', ['Why do programmers prefer dark mode? Because light attracts bugs!', 'Why did the computer sneeze? Because it caught a virus!']],
    [r'thank you|thanks', ["You're very welcome!", 'Anytime!', 'Glad I could help!']]
]

# Initialize the chat with pairs and reflections
chat = Chat(pairs, reflections)

if __name__ == "__main__":
    print("Hi! I'm Vision AI. Type 'quit' to exit.")
    chat.converse()