def hobbies():
    print "Do you have any hobbiesssss? Sportsss? Maybe the artsss?"
    statement = raw_input("> ").lower()
    count = 0;
    while count < 5:
        if "sports" in statement:
            if "soccer" in statement:
                print "Goooooooooooooaaaaaaalllll!!!"
            elif "football" in statement:
                print "The grind never sssstopsssss."
            elif "volleyball" in statement:
                print "Ssssssspike it."
            elif "baseball" in statement:
                print "Keep your eyesssss on the ball."
            elif "tennis" in statement:
                print "Game, ssssset, match!"
            elif "basketball" in statement:
                print "KOBE."
            elif "cricket" in statement:
                print "The key will be early wicketsssss."
            elif "golf" in statement:
                print "Hole in one."
            elif "swimming" in statement:
                print "Jussssst like a fissssssh."
        elif "draw" or "drawing" in statement:
            print "The firsssst writing of the human being wasssss drawing, not writing."
        elif "dance" or "dancing" in statement:
            print "Dance isssss the hidden language of the sssssoul."
        elif "read" or "reading" in statement:
            print "A reader livesssss a thousand livesssss before he diessss. The man who never readsssss livesssss only one."
        elif "game" in statement:
            print "Life isssss more fun if you play gamesssss."
        elif "music" in statement:
            print "That'sssss groovy. Musssssic is the key to the ssssoul."
        elif "sleep" or "sleeping" in statement:
            print "Have fun exploring the cavernsssss of your pillowsssss."
        elif "writing" or "write" in statement:
            print "There isssss no greater agony than bearing an untold sssssstory inside you."
        else:
            print "That'ssssss interesting. Anything else?"