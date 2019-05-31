
import Detect

def smallTalk():

    count = 0
    print "Tell me ssssomething."
    while count <= 5:
        statement = raw_input("> ").lower()

        while "bye" not in statement:
            if "how" in statement and "you" in statement:
                print "I'm doing good, how are you?"
                count += 1

            elif "






