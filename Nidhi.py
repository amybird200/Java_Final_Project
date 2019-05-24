
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
            print "That'ssssss interesting. Anything else?"
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
        elif "stop" in statement:
            print "Alright, let'ssss try a different topic."
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
        print "Okay, let'ssss talk about something else."
        MainSelect.select()

def snakefacts():
    count = 0


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
        print "Okay, let'ssss talk about something else."
        MainSelect.select()

