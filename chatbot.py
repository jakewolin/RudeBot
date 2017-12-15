# PyChat 2K17

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        word = word.lower()
        
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Why don't you stop talking to me?",
                 "Shut up you dumb dumb.",
                 "Absolutely annoying.",
                 "Go back to watching YouTube videos.",
                 "What's the best college in America?"]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    questioning_words = ["why", "who", "what", "when", "where"]
    college_words = ["Harvard", "Yale", "Princeton", "Stanford"]
    
    if has_keyword(statement, questioning_words):
        response = "Stop asking dumb questions!!!!!"
    elif has_keyword(statement, college_words):
        response = "Well you're not getting in so might as well give up now."
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("""Hello. I'm  ____ ____ ____ ____ ____ ____ ____ 
           ||R |||u |||d |||e |||B |||o |||t ||
           ||__|||__|||__|||__|||__|||__|||__||
           |/__\|/__\|/__\|/__\|/__\|/__\|/__\|.""")
    print("What's your darn name?")
    name=input()
    print ("How's your crummy life " + name +"? ")
    

    while talking:
        statement = input(name + ": ")

        if statement == "Goodbye" + ():
            talking = False
        else:
            response = get_response(statement)
            print("RudeBot:" + response)

    print("Goodbye. It was terrible talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to annoyingly chat again?")

end()
