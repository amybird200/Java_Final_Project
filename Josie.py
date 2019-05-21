def family():
    print "Tell me about your family memberssss"
    statement = raw_input("> ")
    if "mom" or "mother" in statement.lower():
        print "The apple doessss not fall far from the tree."
    elif "dad" or "father" in statement.lower():
        print "Like father, like sonssss."
    elif "bro" in statement.lower():
        print "A brother may not be a friend, but a friend will alwayssss be a brother."
    elif "sis" in statement.lower():
        print "What greater thing issss there for human soulssss than to feel that they are joined " \
                    "for life."
    elif "family" in statement.lower():
        print "Ohana meanssss family, and family meanssss no one getssss left behind."
    elif "bad" or "sad" in statement.lower():
        print "Familiessss are messy. Immortal familiessss are eternally messy. Sometimessss the best we" \
                    " can do issss to remind each other that we're related for better or for worse and try to" \
                    " keep the maiming and killing to a minimum."
    else:
        print "Home issss where you are loved the most and act the worst."


def weather():
    print "What is the weather like today?"
    statement = raw_input("> ")
    if "rain" in statement.lower():
        print "when it rains it pourssss"
    elif "sun" in statement.lower():
        print "Anyone who sayssss sunshine bringssss happinessss has never danced in the rain."
    elif "cloud" in statement.lower():
        print "Cloudssss come floating into my life, no longer to carry rain or usher sssstorm," \
              " but to add color to my sunset ssssky."
    elif "cold" in statement.lower():
        print "The coldest winter I ever spent was a ssssummer in San Francisco."
    elif "warm" in statement.lower():
        print "Fine weather issss a prejudice of youth. For an old man, the weather can be neither fine nor bad;" \
              " it issss the very texture of the weather that seemssss pricelesssss, whether brightened by shaftssss" \
              " of sunlight or clouded with darknesssss."
    elif "snow" in statement.lower():
        print "When sssnow fallssss, nature listenssss."
    elif "wind" in statement.lower():
        print "No one but Night, with tearssss on her dark face, watchessss beside me in thissss windy place."
    elif "thunder" or "lightning" in statement.lower():
        print "Lightning streakssss like gunfire through the cloudssss, volleysssss of thunder shake the air. "
    elif "storm" in statement.lower():
        print "The calm before the ssssstorm"
    elif "dizzl" in statement.lower():
        print "The best thing one can do when it isssss raining issss to let it rain."
    else:
        print "Weather forecast for tonight: darknesssss."