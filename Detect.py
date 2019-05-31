
import random

def yesResponses(response):

    yesWords = ["yes", "sure", "ok", "okay", "yeah", "ya", "yah", "yep", "yup", "good", "great", "alright", "yee", "y"]
    for i in range(0, len(yesWords)):
        if yesWords[i] in response.lower():
            return True
    return False


def nouns():

    nounList = ["chatbots", "games", ""]

def nonResponses():
        responses = ["Hmmm", "Tell me more", "Oh?", "Jussst like a bull in a china ssshop...\n...or maybe a ssssnake",
                     "A chain iss only asss ssstrong asss itsss weakessst link", "Interessssssting...", "Wow",
                     "A fool'ssssss paradisssssse",
                     "There'ssss a frog in my throat... Yum", "I did not underssstand",
                     "A leopard doesssn't change itssss sspotssss... but a ssssnake sssshedsss itsss ssscalesss",
                     ]
        ind = random.randint(1, len(responses))
        print responses[ind]





