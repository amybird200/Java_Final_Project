
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
    print "Do you own any petssss?"
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
        else:
            print "Fasssssscinating. I hope it doessssn't bite!"
            count += 1
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
        statement = int(statement)
        if "20" == statement:
            print "Snakes range in size from the tiny, 10 cm-long thread snake, " \
            "to the reticulated python of up to 6.95 meters (22.8 ft) in length."
        if 19 == statement:
            print "There's an Island in Brazil where civilians are forbidden to go: it has up to 5 snakes per square meter."
        if 18 == statement:
            print "Snakes can have two heads and fight each other for food."
        if 17 == statement:
            print "The top ten deadliest snakes can be found in Australia."
        if 16 == statement:
            print "Snakes can open their mouth up to 150 degrees."
        if 15 == statement:
            print "The Titanoboa lived 60 million years ago and is the largest, "
            "longest, and heaviest snake ever discovered."
        if 14 == statement:
            print "Snakes don't have eyelids."
        if 13 == statement:
            print "Snakes use their tongues to smell."
        if 12 == statement:
            print "51% of Americans fear snakes, most than any other thing in the world."
        if 11 == statement:
            print "There has never been snakes in Ireland because being cold-blooded, " \
                  "snake couldn't survive the frozen ground during the ice age in the past."
        if 10 == statement:
            print "More than 20 snake families are currently recognized, " \
                  "comprising about 500 genera and about 3,400 species."
