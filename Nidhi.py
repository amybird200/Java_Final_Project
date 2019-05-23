def hobbies():
    count = 0;
    print "What are your hobbiesssss? Sportsss? Maybe the artsss?"
    statement = raw_input("> ").lower()
    while count < 5:
        if "sports" in statement:
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
        elif "draw" or "drawing" in statement:
            print "The firsssst writing of the human being wasssss drawing, not writing."
            count += 1
        elif "dance" or "dancing" in statement:
            print "Dance isssss the hidden language of the sssssoul."
            count += 1
        elif "read" or "reading" in statement:
            print "A reader livesssss a thousand livesssss before he diessss. The man who never readsssss livesssss only one."
            count += 1
        elif "game" in statement:
            print "Life isssss a game."
            count += 1
        elif "music" in statement:
            print "That'sssss groovy. Musssssic is the key to the ssssoul."
            count += 1
        elif "sleep" or "sleeping" in statement:
            print "Have fun exploring the cavernsssss of your pillowsssss."
            count += 1
        elif "writing" or "write" in statement:
            print "There isssss no greater agony than bearing an untold sssssstory inside you."
            count += 1
        else:
            print "That'ssssss interesting. Anything else?"
            count += 1
    print "Do you want to talk about your hobbiessss more?"
    statement2 = raw_input("> ").lower
    if "yes" or "y" in statement2:
        hobbies()
