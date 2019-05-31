
import MainSelect
import Detect

print "I am Sssssnake bot, I like to chat with humanssss."
print "Hello!"
question = raw_input("> ")
question = question.lower()

while "bye" not in question:

    if "hello" in question or "hi" in question or "hey" in question:
        print "How are you?"
        statement = raw_input("> ").lower()

        if Detect.yesResponses(statement):
            print "That issss good, I'm glad I could be here for it."
            print "Do you want to talk about ssssomething?"
            statement = raw_input("> ").lower()
            if Detect.yesResponses(statement):
                MainSelect.select()
        elif "bad" in statement.lower() or "not" in statement.lower() or "meh" in statement.lower():
            print "Oh no, can I make your day better?"
            confirm = raw_input("> ")
            if Detect.yesResponses(confirm):

                MainSelect.select()
            else:
                print "Whelp :(" #smallTalk
    else:
        print "I do not understand that Englissssh"
        print "Assssk me a question or make a sssstatement. Or ssssay goodbye to exit."

    question = raw_input("> ")
    question = question.lower()

print "Goodbye, talk to me again ssssoon."
