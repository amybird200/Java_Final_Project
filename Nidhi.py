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
    elif "draw" or "drawing" in statement.lower():
        print "The firsssst writing of the human being wasssss drawing, not writing."
