print "Ask me a question or make a ssssssstatement."
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
            print "That issssss good, I'm glad I could be here for it"
        elif "bad" in statement.lower():
            print "Oh no, can I make your day better?"
            confirm = raw_input("> ")
            if "yes" in confirm.lower():
                print "Tell me about your family memberssssssss"
                family = raw_input("> ")
                if "mom" or "mother" in family.lower():
                    print ""


    print "Ask me a question or make a ssssssstatement."
    question = raw_input("> ")
    question = question.lower()

print "Goodbye, talk to me again sssssssssoon."