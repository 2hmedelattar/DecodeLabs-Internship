from datetime import datetime


def greet():
    print("Hello! I'm your assistant, how can I help you?")

def get_input():
    while True:
        message = input("Enter your message: ").lower().strip()
        if message == "":
            print("Not clear to me")
            continue
        break

    return message

def build_lookup():
    intents = {
        "greetings": {"hi", "hello", "welcome"},
        "exiting":   {"quit", "exit", "bye", "good bye", "goodbye"},
        "time":      {"what is the time now", "time", "time now"}
    }

    lookup = {}
    for intent_name, keywords in intents.items():
        for word in keywords:
            lookup[word] = intent_name
    return lookup

def get_response(intent):

    if intent == "greetings":
        response = "Hi! How can I help?"

        return response

    elif intent == "time":
        now = datetime.now()
        response =  f"It's {now.strftime('%I:%M %p')}"

        return response
    
    elif intent == "exiting":         
        return "Goodbye! Have a great day!"
    
    else:
        response = "Sorry, I don't have any answer"

        return response

def run_chatbot():
    greet()
    lookup = build_lookup()

    while True:
        message = get_input()
        intent = lookup.get(message)  

        response = get_response(intent)
        print(response)

        if intent == "exiting":
            break
        
run_chatbot()