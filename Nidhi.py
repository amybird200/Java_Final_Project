def hobbies():
    print "Do you have any hobbiesssss? Sportsss? Maybe the artsss?"
    statement = raw_input("> ")
    if "sports" in statement.lower():
        if "soccer" in statement.lower():
            print "Goooooooooooooaaaaaaalllll!!!"
        elif "football" in statement.lower():
            print "The grind never sssstopsssss."
        elif "volleyball" in statement.lower():
            print "Ssssssspike it."
        elif "baseball" in statement.lower():
            print "Keep your eyesssss on the ball."
        elif "tennis" in statement.lower():
            print "Game, ssssset, match!"
        elif "basketball" in statement.lower():
            print "KOBE."
        elif "cricket" in statement.lower():
            print "The key will be early wicketsssss."
        elif "golf" in statement.lower():
            print "Hole in one."
        elif "swimming" in statement.lower():
            print "Jussssst like a fissssssh."
    elif "draw" or "drawing" in statement.lower():
        print "The firsssst writing of the human being wasssss drawing, not writing."
    elif "dance" or "dancing" in statement.lower():
        print "Dance isssss the hidden language of the sssssoul."
    elif "read" or "reading" in statement.lower():
        print "A reader livesssss a thousand livesssss before he diessss. The man who never readsssss livesssss only one."
    elif "game" in statement.lower():
        print "Life isssss more fun if you play gamesssss."
    elif "music" in statement.lower():
        print "That'sssss groovy. Musssssic is the key to the ssssoul."
    elif "sleep" or "sleeping" in statement.lower():
        print "Have fun exploring the cavernsssss of your pillowsssss."
    elif "writing" or "write" in statement.lower():
        print "There isssss no greater agony than bearing an untold sssssstory inside you."
    else:
        print "That'sssss boring."