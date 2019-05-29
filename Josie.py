import MainSelect


def family():  # This is to talk about your family
    count = 0
    print "Tell me about your family memberssss"
    while count <= 5:
        statement = raw_input("> ").lower()
        if "stop" in statement:
            print "Alright, let'sssss try a different topic."
            MainSelect.select()
            # change later to go back to mainSelectMenu
        elif "mom" in statement or "mother" in statement:
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
    else:
        print "Okay, let'ssss talk about something elsssse."
        MainSelect.select()


def weather():  # This is for talking about the weather
    count = 0
    print "What is the weather like today?"
    while count < 5:
        statement = raw_input("> ")
        if "stop" in statement:
            print "Alright, let'sssss try a different topic."
            MainSelect.select()
        elif "rain" in statement.lower():
            print "when it rains it pourssss"
            count += 1
        elif "sun" in statement.lower():
            print "Anyone who sayssss sunshine bringssss happinessss has never danced in the rain."
            count += 1
        elif "cloud" in statement.lower():
            print "Cloudssss come floating into my life, no longer to carry rain or usher sssstorm," \
              " but to add color to my sunset ssssky."
            count += 1
        elif "cold" in statement.lower():
            print "The coldest winter I ever spent was a ssssummer in San Francisco."
            count += 1
        elif "warm" in statement.lower():
            print "Fine weather issss a prejudice of youth. For an old man, the weather can be neither fine nor bad;" \
                " it issss the very texture of the weather that seemssss pricelesssss, whether brightened by shaftssss" \
                " of sunlight or clouded with darknesssss."
            count += 1
        elif "snow" in statement.lower():
            print "When sssnow fallssss, nature listenssss."
            count += 1
        elif "wind" in statement.lower():
            print "No one but Night, with tearssss on her dark face, watchessss beside me in thissss windy place."
            count += 1
        elif "thunder" in statement.lower() or "lightning" in statement.lower():
            print "Lightning streakssss like gunfire through the cloudssss, volleysssss of thunder shake the air. "
            count += 1
        elif "storm" in statement.lower():
            print "The calm before the ssssstorm"
            count += 1
        elif "driz" in statement.lower():
            print "The best thing one can do when it isssss raining issss to let it rain."
            count += 1
        else:
            print "Weather forecast for tonight: darknesssss."
            count += 1
    print "Do you want to talk about the weather more? (yes/no)"
    statement2 = raw_input("> ").lower()
    if "yes" in statement2 or "y" in statement2:
        weather()
    else:
        print "Okay, let'ssss talk about something elssse."
        MainSelect.select()


def escape_room_rules():
    print "Rules:\t 1. You are trying to escape the room."
    print "\t\t 2. If it's a yes or no question respond with a y for yes or an n for no."
    print "\t\t 3. For all the other questions type in the word that is all caps for the word."
    print "\t\t 4. A \">\" will signify where you type your responses."
    print "press anything to return to the lobby or EXIT to go back to main select."
    state = raw_input("> ")
    if "exit" in state.lower():
        MainSelect.select()
    else:
        escape_room_lobby()


def escape_room_lobby():
    print "Welcome to the lobby of escape rooms. If you want to play type PLAY, " \
          "or you can type HELP for instructions. Otherwise it will quit back to main select."
    state1 = raw_input("> ")
    if "play" in state1.lower():
        print "press 1 to play Kidnapping"
        print "press 2 to play Numbers"
        state2 = raw_input("> ")
        if "1" in state2.lower():
            print "You wake up in a dark room. Will you escape alive? Will you trust your only ally?"
            escape_room1()
        elif "2" in state2.lower():
            print "Guess the number to escape."
            escape_room2()
    elif "help" in state1.lower():
        escape_room_rules()
    else:
        print "Goodbye"
        MainSelect.select()


def escape_room1():  # This is a game that can be played with the chatbot where you are escaping from a room
    print "You wake up and you see that you are in a dark room. " \
          "You look around and see light switch on a wall nearby do you flip it?"
    state1 = raw_input("> ")
    if "y" in state1.lower():
        print "You flipped the switch... *pop* the light sparked to life and " \
              "you turn around to see a skeleton lying on the floor."
        print "He has a key around his neck, do you grab it?"
        state2 = raw_input("> ")
        if "y" in state2.lower():
            print "You grab the key from around his neck. You survey the room to find a " \
                  "box on the floor that has a lock. Do you want to try to use the key on the box?"
            state3 = raw_input("> ")
            if "y" in state3.lower():
                print"You open the box to find a clock and a note. Do you want to read the note?"
                state4 = raw_input("> ")
                if "y" in state4.lower():
                    room1_note()
                    print "You read the time, its 11:31, Would you like to WAIT until noon or " \
                          "EXPLORE the room you are trapped in for a weapon?"
                    state5 = raw_input("> ")
                    if "explore" in state5.lower():
                        room1_explore(1)
                    else:
                        room1_wait(1)
                else:
                    print "You pull the watch out of the box to see that it is 11:30. " \
                          "Would you like to look around the room?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        room1_explore(0)
                    else:
                        "You pull out the note to read it: "
                        room1_note()
                        print "Would you like to WAIT until noon or EXPLORE the room you are trapped in for a weapon?"
                        state6 = raw_input("> ")
                        if "explore" in state6.lower():
                            room1_explore(1)
                        else:
                            room1_wait(1)
            else:
                print "You wander around a bit noticing that there is nowhere else for the key to go. " \
                      "As you wander around you stumble and fall hitting your head on the ground. " \
                      "You bleed out and die."
                room1_end()
        else:
            print "You survey the room to find a box with a lock. The key might fit there. " \
                  "Do you want to grab the key to open the box?"
            state3 = raw_input("> ")
            if "y" in state3.lower():
                print "You grab the key from the skeleton and walk towards the box. The key fits into the lock. " \
                      "You turn the key and open the box to find a letter and pocket watch in the box. " \
                      "Do you want to read the note?"
                state4 = raw_input("> ")
                if "y" in state4.lower():
                    room1_note()
                    print "Would you like to WAIT until noon or EXPLORE the room you are trapped in for a weapon?"
                    state5 = raw_input("> ")
                    if "explore" in state5.lower():
                        room1_explore(1)
                    else:
                        room1_wait(1)
                else:
                    print "You pull the watch out of the box to see that it is 11:40. " \
                            "Would you like to look around the room?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        room1_explore(0)
                    else:
                        print "You pull out the note to read it: "
                        room1_note()
                        print "Would you like to WAIT until noon or EXPLORE the room you are trapped in for a weapon?"
                        state6 = raw_input("> ")
                        if "explore" in state6.lower():
                            room1_explore(1)
                        else:
                            room1_wait(1)
            else:
                room1_explore(0)
    elif "n" in state1.lower():
        print "You stumble around in the dark for a bit until you trip over something the size of a body."
        print "Do you want to turn on the light now?"
        state2 = raw_input("> ")
        if "n" in state2.lower():
            print "You stumble around a bit more feeling the thing that you tripped over. " \
                  "It feels like a human skeleton."
            print "As you are feeling up the dead guy you realize that there is a key around his neck." \
                  " Do you take the key?"
            state3 = raw_input("> ")
            if "y" in state3.lower():
                print "you snatch the key from around his neck and push yourself up off of him. " \
                      "You stand up and look around deciding whether you head AWAY from the wall and light switch " \
                      "or go TOWARDs the wall and light switch."
                state4 = raw_input("> ")
                if "to" in state4.lower():
                    print "You are standing in front of the light switch and this is " \
                          "your last chance to flip the light. Do you flip the light switch?"
                    state5 = raw_input("> ")
                    if "n" in state5.lower():
                        print "you decide to not flip the light switch. " \
                              "Do you walk ALONG the wall or AWAY from the wall?"
                        state6 = raw_input("> ")
                        if "along" in state6.lower():
                            print "As you walk along the wall with your hand on the wall. " \
                                  "You feel something sharp prick your hand. " \
                                  "You decide it's not a big deal and continue walking. " \
                                  "Then all of the sudden you feel a slice in your arm then nothing. " \
                                  "You look at your arm and notice there is no arm. " \
                                  "You pass out as you bleed to death."
                            room1_end()
                        elif "away" in state6.lower():
                            print "You shuffle away from the wall. " \
                                  "You trip over a box this time and realize it has a lock that would fit the key " \
                                  "that you stole from the dead guy laying next to you. " \
                                  "Do you use the key to open the box?"
                            state7 = raw_input("> ")
                            if "y" in state7.lower():
                                print "The box pops open. Inside is a note and a clock. Do you wish to read the note?"
                                state8 = raw_input("> ")
                                if "y" in state8.lower():
                                    room1_note()
                                    print "Do you wish to WAIT until noon or EXPLORE to find a weapon?"
                                    state9 = raw_input("> ")
                                    if "explore" in state9.lower():
                                        room1_explore(1)
                                    else:
                                        room1_wait(1)
                                else:
                                    print "You pull the watch out of the box to see that it is 11:30. " \
                                        "Would you like to look around the room?"
                                    state9 = raw_input("> ")
                                    if "y" in state9.lower():
                                        room1_explore(0)
                                    else:
                                        print "You pull out the note to read it: "
                                        room1_note()
                                        print "Would you like to WAIT until noon or EXPLORE the room " \
                                              "you are trapped in for a weapon?"
                                        state10 = raw_input("> ")
                                        if "explore" in state10.lower():
                                            room1_explore(1)
                                        else:
                                            room1_wait(1)
                            else:
                                room1_explore(0)
                        else:
                            print "You fall against the wall in a moment of dizziness" \
                                  " and accidentally hit the light switch. " \
                                  "After you regain your wits you notice there is a box a bit beyond the skeleton. " \
                                  "Do you walk to the box and try the key?"
                            state7 = raw_input("> ")
                            if "y" in state7.lower():
                                print "You walk up to the box and insert the key. It slips in effortlessly. " \
                                      "You turn it and the box pops open easily. " \
                                      "Inside is a note and a pocketwatch. Do yu wish to read the note?"
                                state8 = raw_input("> ")
                                if "y" in state8.lower():
                                    room1_note()
                                    print "Do you wish to EXPLORE for a weapon or WAIT for noon?"
                                    state9 = raw_input("> ")
                                    if "explore" in state9.lower():
                                        room1_explore(1)
                                    else:
                                        room1_wait(1)
                                else:
                                    print "You pull the watch out of the box to see that it is 11:40. " \
                                              "Would you like to look around the room?"
                                    state9 = raw_input("> ")
                                    if "y" in state9.lower():
                                        room1_explore()
                                    else:
                                        print "You pull out the note to read it: "
                                        room1_note()
                                        print "Would you like to WAIT until noon or EXPLORE the room " \
                                                  "you are trapped in for a weapon?"
                                        state10 = raw_input("> ")
                                        if "explore" in state10.lower():
                                            room1_explore(1)
                                        else:
                                            room1_wait(1)
                            else:
                                print "As you stare at the box you feel your vision go blurry again. " \
                                      "You need to get water soon. Maybe there is some in the box. " \
                                      "Do you go to open the box?"
                                state8 = raw_input("> ")
                                if "y" in state8.lower():
                                    print "You open the box to find a note and a clock. Do you wish to read the note?"
                                    state9 = raw_input("> ")
                                    if "y" in state9.lower():
                                        room1_note()
                                        print "Do you wish to EXPLORE or WAIT for noon?"
                                        state10 = raw_input("> ")
                                        if "explore" in state10.lower():
                                            room1_explore(1)
                                        else:
                                            room1_wait(1)
                                    else:
                                        print "You pull the watch out of the box to see that it is 11:40. " \
                                                  "Would you like to look around the room?"
                                        state9 = raw_input("> ")
                                        if "y" in state9.lower():
                                            room1_explore(0)
                                        else:
                                            print "You pull out the note to read it: "
                                            room1_note()
                                            print "Would you like to WAIT until noon or EXPLORE the room " \
                                                    "you are trapped in for a weapon?"
                                            state10 = raw_input("> ")
                                            if "explore" in state10.lower():
                                                room1_explore(1)
                                            else:
                                                room1_wait(1)
                                else:
                                    room1_explore()
                    else:
                        print "You flip the light switch and notice that there is a skeleton and a box on the floor. " \
                              "Do you wish to use the key to open the box?"
                        state6 = raw_input("> ")
                        if "y" in state6.lower():
                            print "You open the box to find a note and a clock. Do you wish to read the note?"
                            state7 = raw_input("> ")
                            if "y" in state7.lower():
                                room1_note()
                                print "Do you wish to EXPLORE or WAIT for noon?"
                                state9 = raw_input("> ")
                                if "explore" in state9.lower():
                                    room1_explore(1)
                                else:
                                    room1_wait(1)
                            else:
                                print "You pull the watch out of the box to see that it is 11:40. " \
                                      "Would you like to look around the room?"
                                state9 = raw_input("> ")
                                if "y" in state9.lower():
                                    room1_explore(0)
                                else:
                                    print "You pull out the note to read it: "
                                    room1_note()
                                    print "Would you like to WAIT until noon or EXPLORE the room " \
                                          "you are trapped in for a weapon?"
                                    state10 = raw_input("> ")
                                    if "explore" in state10.lower():
                                        room1_explore(1)
                                    else:
                                        room1_wait(1)
                        else:
                            room1_explore()
                elif "away" in state4.lower():
                    print "You stumble away from the wall until you trip over a small box."
                    print "The box feels like if has a lock on it. Do you want to see if your key fits?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        print "You open the box to find a note and a clock. Do you wish to read the note?"
                        state6 = raw_input("> ")
                        if "y" in state6.lower():
                            room1_note()
                            print "Do you wish to EXPLORE or WAIT for noon?"
                            state7 = raw_input("> ")
                            if "explore" in state7.lower():
                                room1_explore(1)
                            else:
                                room1_wait(1)
                        else:
                            print "You pull the watch out of the box to see that it is 11:30. " \
                                    "Would you like to look around the room?"
                            state7 = raw_input("> ")
                            if "y" in state7.lower():
                                room1_explore(0)
                            else:
                                print "You pull out the note to read it: "
                                room1_note()
                                print "Would you like to WAIT until noon or EXPLORE the room " \
                                        "you are trapped in for a weapon?"
                                state8 = raw_input("> ")
                                if "explore" in state8.lower():
                                    room1_explore(1)
                                else:
                                    room1_wait(1)
                    else:
                        room1_explore(0)
                else:
                    print "While you hesitate you trip over the body and hit your head on the ground. " \
                          "Causing a nasty brain bleed, too bad."
                    room1_end()
            else:
                print "You decide not to take the key and try to get up off the skeleton. " \
                      "When you push yourself up you hit your head. Your vision goes blurry. " \
                      "When you come to the lights are on and there is a man standing over you with a knife. " \
                      "Do you SCREAM or RUN?"
                state4 = raw_input("> ")
                if "scream" in state4.lower():
                    print "Your screaming alarms the man and he stabs you right in the chest. " \
                          "You die as your heart pumps the blood out of your body."
                    room1_end()
                elif "run" in state4.lower():
                    print "You get up and start running for the other side of the room. " \
                          "You notice that along the walls there are many knives hanging. " \
                          "The room is very long and at the other end is a door that is surprisingly open. " \
                          "Do you attempt to escape through the door?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        print "You run through the door and as you break the plane of the door you " \
                              "hear a gunshot and feel a prick in your shoulder. " \
                              "You keep running down the dark tunnel. Do you keep running?"
                        state6 = raw_input("> ")
                        if "y" in state6.lower():
                            print "You keep running until you see light at the end of the tunnel. " \
                                  "When you get to the end you see a truck and in the truck is your pet snake. " \
                                  "Do you hop in the truck?"
                            state7 = raw_input("> ")
                            if "y" in state7.lower():
                                print "You hop in and your snake starts driving off. You have escaped!"
                                print "Would you like to play another escape room?"
                                state8 = raw_input("> ")
                                if "y" in state8.lower():
                                    escape_room_lobby()
                                else:
                                    MainSelect.select()
                            else:
                                print "Your snake is mad that you did not hop in, " \
                                      "so it drives at you and you attempt to run away. " \
                                      "You can't run fast enough from the truck and he runs you over."
                                room1_end()
                        else:
                            print "Why did you not run away from the gun people? They shoot you, good job."
                            room1_end()
                    else:
                        print "You hesitated slightly and the man throws the knife at you. " \
                              "The knife lands squarely in your back. You fall to the ground as you bleed out."
                        room1_end()
                else:
                    print "The man stabs you as you lie there staring at him. He watches as your body goes lifeless."
                    room1_end()
        else:
            print "You turn around to see that you tripped over a skeleton."
            print "Dangling from his neck is a small key do you take it?"
            state3 = raw_input("> ")
            if "y" in state3.lower():
                print "You pull the key off his neck and notice a box nearby that may fit the key. " \
                      "Do you want to attempt to open the box?"
                state4 = raw_input("> ")
                if "y" in state4.lower():
                    print "You open the box to find that there is a pocket watch and a letter inside the box. " \
                          "Do you wish to read the letter?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        room1_note()
                        print "Do you wish to EXPLORE the room or WAIT for noon?"
                        state6 = raw_input("> ")
                        if "explore" in state6.lower():
                            room1_explore(1)
                        else:
                            room1_wait(1)
                    else:
                        print "You pull the watch out of the box to see that it is 11:30. " \
                              "Would you like to look around the room?"
                        state6 = raw_input("> ")
                        if "y" in state6.lower():
                            room1_explore(0)
                        else:
                            print "You pull out the note to read it: "
                            room1_note()
                            print "Would you like to WAIT until noon or EXPLORE the room " \
                                  "you are trapped in for a weapon?"
                            state7 = raw_input("> ")
                            if "explore" in state7.lower():
                                room1_explore(1)
                            else:
                                room1_wait(1)
                else:
                    room1_explore(0)
            else:
                print "You survey the room to find that there is a box a bit after the skeleton. " \
                      "Would you like to use the key from the skeleton's neck to open it?"
                state4 = raw_input("> ")
                if "y" in state4.lower():
                    print "You open the box to find that there is a pocket watch and a letter inside the box. " \
                          "Do you wish to read the letter?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        room1_note()
                        print "Do you wish to EXPLORE the room or WAIT for noon?"
                        state6 = raw_input("> ")
                        if "explore" in state6.lower():
                            room1_explore(1)
                        else:
                            room1_wait(1)
                            print "You pull the watch out of the box to see that it is 11:30. " \
                                  "Would you like to look around the room?"
                            state7 = raw_input("> ")
                            if "y" in state7.lower():
                                room1_explore(0)
                            else:
                                print "You pull out the note to read it: "
                                room1_note()
                                print "Would you like to WAIT until noon or EXPLORE the room " \
                                      "you are trapped in for a weapon?"
                                state8 = raw_input("> ")
                                if "explore" in state8.lower():
                                    room1_explore(1)
                                else:
                                    room1_wait(1)
                else:
                    room1_explore(0)

    else:
        print "You trip on your way to turn on the light and fall. When you fall you hit your head and die."
        room1_end()


def room1_note():
    print "You have been kidnapped by a secret organization that wants to kill all snakes.\n" \
          "In order to get out you need to kill the guy that brings you food at noon sharp.\n" \
          "Run and don't turn around or hesitate for any reason. " \
          "Your snake will be there to save you trust no one else.",


def room1_explore(open):
    box_open = int(open)
    print "You wander down the room and see lots of knives on the walls. Do you wish to grab one?"
    state1 = raw_input("> ")
    if "n" in state1.lower():
        print "You continue wandering until you find a door. Do you wish to try to open the door?"
        state2 = raw_input("> ")
        if "y" in state2.lower("> "):
            print "You push against the door and pull against the door to find that it's locked."
            if box_open >= 1:
                print "You look at your watch to see that it is 11:45"
            print "Would you like a knife now?"
            state3 = raw_input("> ")
            if "y" in state3.lower():
                print "You pull down a nice kitchen knife that comes with a sheath you can put on your belt."
                if box_open >= 1:
                    print "The time on the clock says 11:55, it's almost noon. " \
                          "You decide to wait with your knife ready to stab the guy. " \
                          "You are prepared for the guy and as soon as the door opens you stab and kill him."
                else:
                    print "You look around and wander around until the door open. " \
                          "There is a guy with a knife that has come to bring you food. " \
                          "You struggle with him for a bit then you eventually kill him."
                print "Would you like to make a run down the hallway outside your room?"
                state4 = raw_input("> ")
                if "y" in state4.lower():
                    print "You run through the door and " \
                          "hear a gunshot and feel a prick in your shoulder. " \
                          "Do you keep running down the dark hallway?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        print "You keep running until you see light at the end of the tunnel. " \
                              "When you get to the end you see a truck and in the truck is your pet snake. " \
                              "Do you hop in the truck?"
                        state6 = raw_input("> ")
                        if "y" in state6.lower():
                            print "You hop in and your snake starts driving off. You have escaped!"
                            print "Would you like to play another escape room?"
                            state7 = raw_input("> ")
                            if "y" in state7.lower():
                                escape_room_lobby()
                            else:
                                MainSelect.select()
                        else:
                            print "Your snake is mad that you did not hop in, " \
                                  "so it drives at you and you attempt to run away. " \
                                  "You can't run fast enough from the truck and he runs you over."
                            room1_end()
                    else:
                        print "Why did you not run away from the gun people? They shoot you, good job."
                        room1_end()
                else:
                    print "You hesitate in the room and another guard with a gun comes in to investigate. " \
                          "Upon seeing his dead comrade he shoots you square in the chest. "
                    room1_end()
            else:
                print "The door opens and inside comes a guard with a knife. " \
                      "He sees you near the door way and stabs you."
                room1_end()
        else:
            print "You wander back down the hallway"
            if box_open >= 1:
                print "You look at your watch to see that it is 11:45"
            print "Would you like to grab a knife now?"
            state3 = raw_input("> ")
            if "y" in state3.lower():
                print "You pull down a nice kitchen knife that comes with a sheath you can put on your belt."
                if box_open >= 1:
                    print "The time on the clock says 11:55, it's almost noon. " \
                          "You decide to wait with your knife ready to stab the guy. " \
                          "You are prepared for the guy and as soon as the door opens you stab and kill him."
                else:
                    print "You look around and wander around until the door open. " \
                          "There is a guy with a knife that has come to bring you food. " \
                          "You struggle with him for a bit then you eventually kill him."
                print "Would you like to make a run down the hallway outside your room?"
                state4 = raw_input("> ")
                if "y" in state4.lower():
                    print "You run through the door and " \
                          "hear a gunshot and feel a prick in your shoulder. " \
                          "Do you keep running down the dark hallway?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        print "You keep running until you see light at the end of the tunnel. " \
                              "When you get to the end you see a truck and in the truck is your pet snake. " \
                              "Do you hop in the truck?"
                        state6 = raw_input("> ")
                        if "y" in state6.lower():
                            print "You hop in and your snake starts driving off. You have escaped!"
                            print "Would you like to play another escape room?"
                            state7 = raw_input("> ")
                            if "y" in state7.lower():
                                escape_room_lobby()
                            else:
                                MainSelect.select()
                        else:
                            print "Your snake is mad that you did not hop in, " \
                                  "so it drives at you and you attempt to run away. " \
                                  "You can't run fast enough from the truck and he runs you over."
                            room1_end()
                    else:
                        print "Why did you not run away from the gun people? They shoot you, good job."
                        room1_end()
                else:
                    print "You hesitate in the room and another guard with a gun comes in to investigate. " \
                          "Upon seeing his dead comrade he shoots you square in the chest. "
                    room1_end()
            else:
                print "The door opens and inside comes a guard with a knife. " \
                      "He sees you near the door way and stabs you."
                room1_end()
    else:
        print "You pull down a nice kitchen knife that comes with a sheath you can put on your belt."
        print "You continue to look around and find a door. " \
              "Do you want to try to open the door?"
        state2 = raw_input("> ")
        if "y" in state2.lower():
            print "You push against the door and pull against the door to find that it's locked. " \
                  "You try jiggling your knife in the crack and you hear a pop that opens the door."
            if box_open >= 1:
                print "You look at your watch to see that it is 11:50"
            print "Would you like to make a run for it? "
            state3 = raw_input("> ")
            if "y" in state3.lower():
                print "You run through the door and " \
                      "hear a gunshot and feel a prick in your shoulder. " \
                      "Do you keep running down the dark hallway?"
                state4 = raw_input("> ")
                if "y" in state4.lower():
                    print "You keep running until you see light at the end of the tunnel. " \
                          "When you get to the end you see a truck and in the truck is your pet snake. " \
                          "Do you hop in the truck?"
                    state5 = raw_input("> ")
                    if "y" in state5.lower():
                        print "You hop in and your snake starts driving off. You have escaped!"
                        print "Would you like to play another escape room?"
                        state6 = raw_input("> ")
                        if "y" in state6.lower():
                            escape_room_lobby()
                        else:
                            MainSelect.select()
                    else:
                        print "Your snake is mad that you did not hop in, " \
                              "so it drives at you and you attempt to run away. " \
                              "You can't run fast enough from the truck and he runs you over."
                        room1_end()
                else:
                    print "Why did you not run away from the gun people? They shoot you, good job."
                    room1_end()
            else:
                print "You sit down on the ground. 10 minutes later " \
                      "the guard bringing you food notices the door is unlocked and " \
                      "stabs you when he opens the door and sees you sitting there."
                room1_end()
        else:
            if box_open >= 1:
                print "You look at your watch to see that it is 11:45. You decide to wait until the guy comes. " \
                      "You are prepared for his entrance and easily kill him. "
            else:
                print "You are waiting next to the door when it pops open. " \
                          "There is a guy with a knife that has come to bring you food. " \
                          "You struggle with him for a bit then you eventually kill him."
            print "Would you like to make a run down the hallway outside your room?"
            state4 = raw_input("> ")
            if "y" in state4.lower():
                print "You run through the door and " \
                    "hear a gunshot and feel a prick in your shoulder. " \
                    "Do you keep running down the dark hallway?"
                state5 = raw_input("> ")
                if "y" in state5.lower():
                    print "You keep running until you see light at the end of the tunnel. " \
                        "When you get to the end you see a truck and in the truck is your pet snake. " \
                        "Do you hop in the truck?"
                    state6 = raw_input("> ")
                    if "y" in state6.lower():
                        print "You hop in and your snake starts driving off. You have escaped!"
                        print "Would you like to play another escape room?"
                        state7 = raw_input("> ")
                        if "y" in state7.lower():
                            escape_room_lobby()
                        else:
                            MainSelect.select()
                    else:
                        print "Your snake is mad that you did not hop in, " \
                            "so it drives at you and you attempt to run away. " \
                            "You can't run fast enough from the truck and he runs you over."
                        room1_end()
                else:
                    print "Why did you not run away from the gun people? They shoot you, good job."
                    room1_end()
            else:
                print "You hesitate in the room and another guard with a gun comes in to investigate. " \
                    "Upon seeing his dead comrade he shoots you square in the chest. "
                room1_end()


def room1_wait(open):
    box_open = int(open)
    if box_open >= 1:
        print "You look at the clock to see that it is 11:45. At noon the door pops open " \
              "and the guy that comes in has a knife. Since you were prepared for his arrival " \
              "you are able to slip out the door behind him would you like to?"
        state5 = raw_input("> ")
        if "y" in state5.lower():
            print "You run through the door and as you break the plane of the door you " \
                  "hear a gunshot and feel a prick in your shoulder. " \
                  "You keep running down the dark tunnel. Do you keep running?"
            state6 = raw_input("> ")
            if "y" in state6.lower():
                print "You keep running until you see light at the end of the tunnel. " \
                      "When you get to the end you see a truck and in the truck is your pet snake. " \
                      "Do you hop in the truck?"
                state7 = raw_input("> ")
                if "y" in state7.lower():
                    print "You hop in and your snake starts driving off. You have escaped!"
                    print "Would you like to play another escape room?"
                    state8 = raw_input("> ")
                    if "y" in state8.lower():
                        escape_room_lobby()
                    else:
                        MainSelect.select()
                else:
                    print "Your snake is mad that you did not hop in, " \
                          "so it drives at you and you attempt to run away. " \
                          "You can't run fast enough from the truck and he runs you over."
                    room1_end()
            else:
                print "Why did you not run away from the gun people? They shoot you, good job."
                room1_end()
        else:
            print "You hesitated slightly and the man notices you trying to escape. He throws his knife at you. " \
                  "The knife lands squarely in your back. You fall to the ground as you bleed out."
            room1_end()
    else:
        print "You sit down next to the wall to wait. The door opens catching you by surprise. " \
              "There is a man with a knife. Because of your surprise he is able to easily over take you and stab you."
        room1_end()


def room1_end():
    print "Would you like to attempt the room again?"
    state1 = raw_input("> ")
    if "y" in state1.lower():
        escape_room1()
    else:
        escape_room_lobby()


def escape_room2():
    num = 50  # Random Number generator
    print "In order to escape you need to find my number. " \
          "Once you have found my number I will let you out of your confines. "
    guess = raw_input("Enter Your number on the pad \n> ")
    while guess != num:
        guess = int(guess)
        if guess > num:
            print "Your guess is too high!"
        elif guess < num:
            print "Your guess is too low!"
        else:
            print "You got it!!! You are free to go."
        guess = raw_input("Enter Your number on the pad \n> ")

    print "Would you like to play again?"
    state1 = raw_input("> ")
    if "y" in state1.lower():
        escape_room2()
    else:
        escape_room_lobby()