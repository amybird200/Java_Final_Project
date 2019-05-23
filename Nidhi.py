def hobbies():
    count = 0
    print "What are your hobbiesssss? Sportsss? Perhapssss the artsss?"
    statement = raw_input("> ").lower()
    while count < 5:
        if "soccer" in statement:
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
            print "That'ssssss interesting. Anything else?"
            count += 1
    print "Do you want to talk about your hobbiessss more?"
    statement2 = raw_input("> ").lower
    if "yes" or "y" in statement2:
        hobbies()

def pets():
    count = 0
    print "Do you own any petssss?"
    statement = raw_input("> ").lower()
    while count < 5:
        if "snake" in statement:
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
    print "Do you want to talk about your petsssss more?"
    statement2 = raw_input("> ").lower
    if "yes" or "y" in statement2:
        pets()



