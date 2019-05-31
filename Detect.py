
import random

def yesResponses(response):

    yesWords = ["yes", "sure", "ok", "okay", "yeah", "ya", "yah", "yep", "yup", "good", "great", "alright", "yee"]
    for i in range(0, len(yesWords)):
        if yesWords[i] in response.lower():
            return True
    return False


def convoStarters():
    questions = ["How are you?", "What did you do today?", "Tell me sssomething about you.", "How wassss your day?", "What are you doing?"]
    print questions[random.randint(1, len(questions))]

def nonResponses():
        responses = ["Hmmm", "Tell me more", "Oh?", "Jussst like a bull in a china ssshop...\n...or maybe a ssssnake",
                     "A chain iss only asss ssstrong asss itsss weakessst link", "Interessssssting...", "Wow",
                     "A fool'ssssss paradisssssse",
                     "There'ssss a frog in my throat... Yum", "I did not underssstand",
                     "A leopard doesssn't change itssss sspotssss... but a ssssnake sssshedsss itsss ssscalesss", "That'ssss a you problem...", "Ssssoundsss rough.",
                     "Perhapsssss...", "Are you ssssure?"
                     ]
        ind = random.randint(1, len(responses))
        print responses[ind]





