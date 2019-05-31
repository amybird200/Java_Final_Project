
import Detect
import MainSelect

def smallTalk():

    count = 0
    print "Tell me ssssomething."
    while count <= 5:
        statement = raw_input("> ").lower()

        if "stop" in statement or "bye" in statement:
            print "Letssss talk about ssssomething elsssssse."
            MainSelect.select()
        elif "ok" in statement:
            Detect.convoStarters()
        elif "how" in statement and "you" in statement:
            print "I'm doing good, how are you?"
            count += 1
        elif "good" in statement:
            print "I am glad."
            count += 1
        elif "bad" in statement:
            print "Aww. :( Why isssss that?"
            count += 1
        elif "what" in statement and "name" in statement:
            print "Can't you read!!! my name is Ssssssnakebot. \tWhat'ssss your name??"
            count += 1
        else:
            Detect.nonResponses()









