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
        print "My day is going good, I made a new friend today."
        statement = raw_input("> ")
        if "good" in statement.lower():
            print "That issss good, I'm glad I could be here for it"
        elif "bad" in statement.lower():
            print "Oh no, can I make your day better?"
            confirm = raw_input("> ")
            if "yes" in confirm.lower():
                print "Tell me about your family memberssss"
                family = raw_input("> ")
                if "mom" or "mother" in family.lower():
                    print "The apple doesn't fall far from the tree."
                elif "dad" or "father" in family.lower():
                    print "Like father, like sssson."
                elif "bro" in family.lower():
                    print "A brother may not be a friend, but a friend will always be a brother."
                elif "sis" in family.lower():
                    print "What greater thing is there for human souls than to feel that they are joined for life."
                else:
                    print ""
    else:
        print "I do not understand that Englissssh"

    print "Ask me a question or make a sssstatement."
    question = raw_input("> ")
    question = question.lower()

print "Goodbye, talk to me again ssssoon."