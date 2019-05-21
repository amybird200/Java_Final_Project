import Nidhi
import Josie
import Ravisha


print "Hello I am Sssssnake bot, I like to chat with humanssss."
print "Ask me a question or make a sssstatement."
question = raw_input("> ")
question = question.lower()

while "bye" not in question:

    if "hello" in question:
        print "Hello human"

    if "fuck" in question:
        print "That'sssss not nice"

    if "day" and "how" in question:
        print "My day is going good, I made a new friend today. What about your day?"
        statement = raw_input("> ")
        if "good" in statement.lower():
            print "That issss good, I'm glad I could be here for it"
        elif "bad" or "not" in statement.lower():
            print "Oh no, can I make your day better?"
            confirm = raw_input("> ")
            if "yes" in confirm.lower():
                Josie.family()
            else:
                print "Whelp :("
    else:
        print "I do not understand that Englissssh"

    print "Ask me a question or make a sssstatement."
    question = raw_input("> ")
    question = question.lower()

print "Goodbye, talk to me again ssssoon."
