print "Ask me a question: ",
question = raw_input()
question = question.lower()
print "your question: %s" % question

if "hello" in question:
    print "Hello to you too"

if "fuck" in question:
    print "That's not nice"
