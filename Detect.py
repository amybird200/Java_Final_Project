
def yesResponses(response):

    yesWords = ["yes", "sure", "ok", "okay", "yeah", "ya", "yah", "yep", "yup", "good", "great", "alright", "yee", "y"]
    for i in range(0, len(yesWords)):
        if yesWords[i] in response.lower():
            return True
    return False


def nouns():

    nounList = ["chatbots", "games", ""]


