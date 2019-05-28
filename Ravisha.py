
import random

def smallTalk():
    count = 0
    print "How wassssss your day?"
    while count <= 5:
        statement = raw_input("> ").lower()

        if "good" in statement:
            print "Exsssssscelent... What did you do"


def nonResponses():

    responses = ["Hmmm", "Tell me more", "Oh?", "Jussst like a bull in a china ssshop...\n...or maybe a ssssnake",
                 "A chain iss only asss ssstrong asss itsss weakessst link", "Interessssssting...", "Wow", "A fool'ssssss paradisssssse",
                 "There'ssss a frog in my throat... Yum", "I did not underssstand", "A leopard doesssn't change itssss sspotssss... but a ssssnake sssshedsss itsss ssscalesss",
                 ]
    ind = random.randint(1, len(responses))
    print responses[ind]



