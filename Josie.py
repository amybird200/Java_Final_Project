def family():  # This is to talk about your family
    count = 0
    print "Tell me about your family memberssss"
    while count <= 5:
        statement = raw_input("> ").lower()
        if "mom" in statement or "mother" in statement:
            print "The apple doessss not fall far from the tree."
            count += 1
        elif "dad" in statement or "father" in statement:
            print "Like father, like sonssss."
            count += 1
        elif "bro" in statement:
            print "A brother may not be a friend, but a friend will alwayssss be a brother."
            count += 1
        elif "sis" in statement:
            print "What greater thing issss there for human soulssss than to feel that they are joined " \
                    "for life."
            count += 1
        elif "family" in statement:
            print "Ohana meanssss family, and family meanssss no one getssss left behind."
            count += 1
        elif "bad" in statement or "sad" in statement:
            print "Familiessss are messy. Immortal familiessss are eternally messy. Sometimessss the best we" \
                    " can do issss to remind each other that we're related for better or for worse and try to" \
                    " keep the maiming and killing to a minimum."
            count += 1
        else:
            print "Home issss where you are loved the most and act the worst."
            count += 1
    print "Do you want to talk about your family more?"
    statement2 = raw_input("> ").lower
    if "yes" or "y" in statement2:
        family()


def weather():  # This is for talking about the weather
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


def escape_room_rules():
    print "Rules:\t 1. You are trying to escape the room."
    print "\t\t 2. If it's a yes or no question respond with yes or no"
    print "\t\t 3. For all the "


def escape_room():  # This is a game that can be played with the chatbot where you are escaping from a room
    print "You wake up and you see that you are in a dark room. " \
          "You look around and see light switch on a wall nearby do you flip it?"
    state1 = raw_input("> ")
    if "yes" or "y" in state1.lower():
        print "You flipped the switch... *pop* the light sparked to life and " \
              "you turn around to see a skeleton lying on the floor."
        print "He has a key around his neck, do you grab it?"
        state2 = raw_input("> ")
        if "y" or "yes" in state2.lower():
            print "You grab the key from around his neck. You survey the room to find a " \
                  "box on the floor that has a lock. Do you want to try to use the key on the box?"
            state3 = raw_input("> ")
            if "y" or "yes" in state3.lower():
                print""
            else:
                print""
    elif "no" or "n" in state1.lower():
        print "You stumble around in the dark for a bit until you trip over something the size of a body."
        print "Do you want to turn on the light now?"
        state2 = raw_input("> ")
        if "no" or "n" in state2.lower():
            print "You stumble around a bit more feeling the thing that you tripped over. " \
                  "It feels like a human skeleton."
            print "As you are feeling up the dead guy you realize that there is a key around his neck." \
                  " Do you take the key?"
            state3 = raw_input("> ")
            if "yes" or "y" in state3.lower():
                print "you snatch the key from around his neck and push yourself up off of him. " \
                      "You stand up and look around deciding whether you head AWAY from the wall and light switch " \
                      "or go TOWARDs the wall and light switch."
                state4 = raw_input("> ")
                if "to" in state4.lower():
                    print "You are standing in front of the light switch and this is " \
                          "your last chance to flip the light. Do you flip the light switch?"
                    state5 = raw_input("> ")
                    if "no" or "n" in state5.lower():
                        print "you decide to not flip the light switch. " \
                              "Do you walk ALONG the wall or AWAY from the wall?"
                else:
                    print "You stumble away from the wall until you trip over a small box."
                    print "The box feels like if has a lock on it. Do you want to see if your key fits?"
        else:
            print "You turn around to see that you tripped over a skeleton"
            print "Dangling from his neck is a small key do you take it?"
    else:
        print "You trip on your way to turn on the light and fall. When you fall you hit your head and die."
        print "Would you like to try again?"
        state2 = raw_input("> ")
        if "yes" or "y" in state2.lower():
            escape_room()