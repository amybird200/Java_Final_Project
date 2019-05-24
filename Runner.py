
import MainSelect

print "Hello I am Sssssnake bot, I like to chat with humanssss."
print "Assssk me a question or make a sssstatement."
question = raw_input("> ")
question = question.lower()

while "bye" not in question:

    if "hello" in question or "hi" in question or "hey" in question:
        print "Hello human"

    elif "fuck" in question:
        print "That'sssss not nice"

    elif "day" and "how" in question:
        print "My day issss going good, I made a new friend today. What about your day?"
        statement = raw_input("> ")
        if "good" in statement.lower():
            print "That issss good, I'm glad I could be here for it"
        elif "bad" in statement.lower() or "not" in statement.lower() or "meh" in statement.lower():
            print "Oh no, can I make your day better?"
            confirm = raw_input("> ")
            if "yes" in confirm.lower() or "y" in confirm.lower():
                MainSelect.select()
            else:
                print "Whelp :("
    else:
        print "I do not understand that Englissssh"
        print "Assssk me a question or make a sssstatement. Or ssssay goodbye to exit."

    question = raw_input("> ")
    question = question.lower()

print "Goodbye, talk to me again ssssoon."
