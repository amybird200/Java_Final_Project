

print "Ask me a question or make a statement."
question = raw_input("> ")
question = question.lower()
print "your question: %s" % question

while "bye" not in question:

    if "hello" in question:
        print "Hello to you too"

    if "fuck" in question:
        print "That's not nice"

    print "Ask me a question or make a statement."
    question = raw_input("> ")
    question = question.lower()
    print "your question: %s" % question

print "Goodbye, talk to me again soon."