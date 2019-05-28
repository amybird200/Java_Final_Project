
import MainSelect

def hobbies():
    count = 0
    print "What are your hobbiesssss? Sportsss? Perhapssss the artsss?"
    while count <= 5:
        statement = raw_input("> ").lower()
        if "stop" in statement:
            print "Alright, let'sssss try a different topic."
            MainSelect.select()
            # change later to go back to mainSelectMenu
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
            print "That'ssssss interesting. Anything elsssse?"
            count += 1
    print "Do you want to talk about your hobbiessss more? (yes/no)"
    statement2 = raw_input("> ").lower()
    if "yes" in statement2 or "y" in statement2:
        hobbies()
    else:
        print "Okay, let'ssss talk about something else."

def pets():
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
        elif "whales" in statement:
            print "The giants of the water."
        else:
            print "Fasssssscinating. I hope it doessssn't bite!"
            count += 1
        print "What other animals do you like?"
    print "Do you want to talk about your petsssss more? (yes/no)"
    statement2 = raw_input("> ").lower()
    if "yes" in statement2 or "y" in statement2:
        pets()
    else:
        print "Okay, let'ssss talk about something elsssse."
        MainSelect.select()

def snakefacts():
    count = 0
    print "Give me a number from 1 - 20 and I'll give you a snake fact."
    while count < 5:
        statement = raw_input("> ").lower()
        if "stop" in statement:
            print "Alright, let'sssss try a different topic."
            MainSelect.select()
        statement = int(statement)
        if statement == 20:
            print "Snakes range in size from the tiny, 10 cm-long thread snake, " \
            "to the reticulated python of up to 6.95 meters (22.8 ft) in length."
            count += 1
        elif 19 == statement:
            print "There's an Island in Brazil where civilians are forbidden to go: it has up to 5 snakes per square meter."
            count += 1
        elif 18 == statement:
            print "Snakes can have two heads and fight each other for food."
            count += 1
        elif 17 == statement:
            print "The top ten deadliest snakes can be found in Australia."
            count += 1
        elif 16 == statement:
            print "Snakes can open their mouth up to 150 degrees."
            count += 1
        elif 15 == statement:
            print "The Titanoboa lived 60 million years ago and is the largest, " \
            "longest, and heaviest snake ever discovered."
            count += 1
        elif 14 == statement:
            print "Snakes don't have eyelids."
            count += 1
        elif 13 == statement:
            print "Snakes use their tongues to smell."
            count += 1
        elif 12 == statement:
            print "51% of Americans fear snakes, most than any other thing in the world."
            count += 1
        elif 11 == statement:
            print "There has never been snakes in Ireland because being cold-blooded, " \
                  "snake couldn't survive the frozen ground during the ice age in the past."
            count += 1
        elif 10 == statement:
            print "More than 20 snake families are currently recognized, " \
                  "comprising about 500 genera and about 3,400 species."
            count += 1
        elif 9 == statement:
            print "Military commandos in Lebanon eat live snakes, a tradition to display their strength and daring."
            count += 1
        elif 8 == statement:
            print "Snakes can sense other animals approaching by detecting faint vibrations " \
                  "in the air and on the ground."
            count += 1
        elif 7 == statement:
            print "Some snakes survive for up to two years without a meal."
            count += 1
        elif 6 == statement:
            print "The vertebral column of snakes consists of anywhere between 200 to 400 vertebrae."
            count += 1
        elif 5 == statement:
            print "Ophidiophobia is the abnormal fear of snakes."
            count += 1
        elif 4 == statement:
            print "'King' in a snake's name signifies that it preys on other snakes."
            count += 1
        elif 3 == statement:
            print "The decapitated head of a dead snake can still bite, even hours after death." \
                  " These types of bites usually contain huge amounts of venom."
            count += 1
        elif 2 == statement:
            print "The top 5 most venomous snakes in the world are the inland taipan, the eastern brown snake, " \
                  "the coastal taipan, the tiger snake, and the black tiger snake."
            count += 1
        elif 1 == statement:
            print "Some snakes have over 200 teeth."
            count += 1
        else:
            print "Thosssse who do not read instructions do not receive sssssnake facts."
    print "Do you want to talk about ssssnakes more? (yes/no)"
    statement2 = raw_input("> ").lower()
    if "yes" in statement2 or "y" in statement2:
        snakefacts()
    else:
        print "Okay, let'ssss talk about something elsssse."
        MainSelect.select()
