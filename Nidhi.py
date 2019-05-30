
import MainSelect

def hobbies(): #gives responses to different hobby types, including sports and the arts
    count = 0
    print "What are your hobbiesssss? Sportsss? Perhapssss the artsss?"
    while count <= 5:
        statement = raw_input("> ").lower()
        if "stop" in statement:
            print "Alright, let'sssss try a different topic."
            MainSelect.select()
        elif "soccer" in statement:
            print "Goooooooooooooaaaaaaalllll!!!"
            count += 1
        elif "football" in statement:
            print "The grind never sssstopsssss."
            count += 1
        elif "volleyball" in statement:
            print "Ssssssspike it."
            count += 1
        elif "baseball" in statement:
            print "Keep your eyesssss on the ball."
            count += 1
        elif "tennis" in statement:
            print "Game, ssssset, match!"
            count += 1
        elif "basketball" in statement:
            print "KOBE."
            count += 1
        elif "cricket" in statement:
            print "The key will be early wicketsssss."
            count += 1
        elif "golf" in statement:
            print "Hole in one."
            count += 1
        elif "swimming" in statement:
            print "Jussssst like a fissssssh."
            count += 1
        elif "draw" in statement or "drawing" in statement:
            print "The firsssst writing of the human being wasssss drawing, not writing."
            count += 1
        elif "dance" in statement or "dancing" in statement:
            print "Dance isssss the hidden language of the sssssoul."
            count += 1
        elif "read" in statement or "reading" in statement:
            print "A reader livesssss a thousand livesssss before he diessss. The man who never readsssss livesssss only one."
            count += 1
        elif "game" in statement:
            print "Life isssss a game."
            count += 1
        elif "music" in statement:
            print "That'sssss groovy. Musssssic is the key to the ssssoul."
            count += 1
        elif "sleep" in statement or "sleeping" in statement:
            print "Have fun exploring the cavernsssss of your pillowsssss."
            count += 1
        elif "writing" in statement or "write" in statement:
            print "There isssss no greater agony than bearing an untold sssssstory inside you."
            count += 1
        elif "photography" in statement or "photo" in statement:
            print "A picture issss worth a thoussssand wordssss."
        else:
            print "That'ssssss interesting... Sssoundssss fun!"
            count += 1
        if count < 5:
            print "What other hobbiessss do you enjoy?"
    print "Do you want to talk about your hobbiessss more? (yes/no)" #asks if user wants to continue talking about hobbies after 5 sentences
    statement2 = raw_input("> ").lower()
    if "yes" in statement2 or "y" in statement2:
        hobbies()
    else:
        print "Okay, let'ssss talk about something elsssse."

def animals(): #gives responses about different animals that the user talks about
    count = 0
    print "What are your favorite animals?"
    while count < 5:
        statement = raw_input("> ").lower()
        if "stop" in statement:
            print "Alright, let'sssss try a different topic."
            MainSelect.select()
        elif "snake" in statement:
            print "The besssst animal!"
            count += 1
        elif "dog" in statement:
            print "Dog is man'ssss besssst friend."
            count += 1
        elif "cat" in statement:
            print "What greater gift than the love of a cat."
            count += 1
        elif "rabbit" in statement or "bunny" in statement:
            print "What'sss up, doc?"
            count += 1
        elif "hamster" in statement or "guinea pig" in statement:
            print "Mmmmmm dinner."
            count += 1
        elif "fish" in statement:
            print "'I know the human being and fisssssh can co-exist peacefully.' - George W. Busssssh"
            count += 1
        elif "bird" in statement:
            print "Polly want a cracker?"
            count += 1
        elif "turtles" in statement:
            print "Sssslow and sssssteady winssss the race."
            count += 1
        elif "whale" in statement:
            print "The giantsssss of the water."
            count += 1
        elif "shark" in statement:
            print "Sssssharks aren't the monstersssss we make them out to be."
            count += 1
        elif "monkey" in statement or "chimp" in statement or "orangutan" in statement or "baboon" in statement or "gorrillas" in statement or "howler" in statement or "gibbons" in statement or "capuchin" in statement:
            print "People go to the zoo and they like the lion because it's ssscary," \
            " and the bear becausssse it's intensssse, but the monkey makessss people laugh."
            count += 1
        elif "elephant" in statement:
            print "The wisssessst of animalssss."
            count += 1
        elif "dolphin" in statement:
            print "If I had to come back in life, I'd come back assss a dolphin... " \
                  "they're alwayssss smiling; they're alwaysssss playing."
            count += 1
        elif "tiger" in statement or "panther" in statement or "lion" in statement or "jaguar" in statement or "leopard" in statement or "cheetah" in statement or "cougar" in statement or "puma" in statement:
            print "Big catsssss are just small catsssss with bigger teeth and clawsssss."
            count += 1
        elif "horse" in statement:
            print "The wind of heaven is that which blowsssss between a horsssse's earssss."
            count += 1
        else:
            print "Fasssssscinating. Beautiful creaturessss everywhere on thissss earth!"
            count += 1
        if count < 5:
            print "What other animalssss do you like?"

    print "Do you want to talk about animals more? (yes/no)" #asks if user wants to continue talking about animals after 5 sentences
    statement2 = raw_input("> ").lower()
    if "yes" in statement2 or "y" in statement2:
        pets()
    else:
        print "Okay, let'ssss talk about something elsssse."
        MainSelect.select()

def snakefacts(): #user puts in a number from 1-20 and Snakebot gives out a snake fact
    count = 0
    print "Give me an integer from 1 - 20 and I'll give you a sssssnake fact."
    while count < 5:
        statement = raw_input("> ").lower()
        if "stop" in statement:
            print "Alright, let'sssss try a different topic."
            MainSelect.select()
        statement = int(statement)
        if statement == 20:
            print "Ssssnakes range in ssssize from the tiny, 10 cm-long thread ssssnake, " \
            "to the reticulated python of up to 6.95 meterssss (22.8 ft) in length."
            count += 1
        elif 19 == statement:
            print "There's an isssland in Brazil where civilianssss are forbidden to go: " \
                  "it hassss up to 5 snakessss per ssssquare meter."
            count += 1
        elif 18 == statement:
            print "Sssssnakessss can have two headssss and fight each other for food."
            count += 1
        elif 17 == statement:
            print "The top ten deadliesssst ssssnakessss can be found in Australia."
            count += 1
        elif 16 == statement:
            print "Ssssnakessss can open their mouth up to 150 degreessss."
            count += 1
        elif 15 == statement:
            print "The Titanoboa lived 60 million yearssss ago and issss the largessst, " \
            "longesssst, and heaviesssst ssssnake ever discovered."
            count += 1
        elif 14 == statement:
            print "Ssssnakessss don't have eyelidssss."
            count += 1
        elif 13 == statement:
            print "Ssssnakessss usssse their tonguessss to ssssmell."
            count += 1
        elif 12 == statement:
            print "51% of Americanssss fear snakessss, most than any other thing in the world."
            count += 1
        elif 11 == statement:
            print "There has never been sssssnakessss in Ireland becausssse being cold-blooded, " \
                  "sssssnake couldn't ssssurvive the frozen ground during the ice age in the passsst."
            count += 1
        elif 10 == statement:
            print "More than 20 ssssnake familiessss are currently recognized, " \
                  "comprissssing about 500 genera and about 3,400 ssssspeciessss."
            count += 1
        elif 9 == statement:
            print "Military commandossss in Lebanon eat live ssssnakessss, " \
                  "a tradition to dissssplay their sssstrength and daring."
            count += 1
        elif 8 == statement:
            print "Ssssnakessss can ssssensssse other animalssss approaching by detecting faint vibrationssss " \
                  "in the air and on the ground."
            count += 1
        elif 7 == statement:
            print "Ssssome ssssnakessss ssssurvive for up to two yearssss without a meal."
            count += 1
        elif 6 == statement:
            print "The vertebral column of ssssnakessss consistssss of anywhere between 200 to 400 vertebrae."
            count += 1
        elif 5 == statement:
            print "Ophidiophobia issss the abnormal fear of ssssnakessss."
            count += 1
        elif 4 == statement:
            print "'King' in a ssssnake'sss name sssssignifiessss that it preys on other ssssnakessss."
            count += 1
        elif 3 == statement:
            print "The decapitated head of a dead ssssnake can still bite, even hourssss after death." \
                  " These typessss of bitessss usually contain huge amountssss of venom."
            count += 1
        elif 2 == statement:
            print "The top 5 mosssst venomous ssssnakessss in the world are the inland taipan, the eassstern brown ssssnake, " \
                  "the coasssstal taipan, the tiger ssssnake, and the black tiger ssssnake."
            count += 1
        elif 1 == statement:
            print "Ssssome ssssnakessss have over 200 teeth."
            count += 1
        else:
            print "Thosssse who do not read instructionssss do not receive sssssnake facts."
        if count < 5:
            print "Put in another integer from 1 - 20 for another ssssplendid sssssnake fact."
    print "Do you want to talk about ssssnakes more? (yes/no)" #asks if user wants to continue talking about snake facts after 5 sentences
    statement2 = raw_input("> ").lower()
    if "yes" in statement2 or "y" in statement2:
        snakefacts()
    else:
        print "Okay, let'ssss talk about something elsssse."
        MainSelect.select()
