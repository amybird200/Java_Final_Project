import Nidhi
import Josie
import Ravisha



def select():
    print "Would you like to talk about your family?"
    confirm = raw_input("> ")
    if "yes" in confirm.lower() or "y" in confirm.lower():
        Josie.family()
    print "Would you like to talk about the weather?"
    confirm = raw_input("> ")
    if "yes" in confirm.lower() or "y" in confirm.lower():
        Josie.weather()
    print "Would you like to talk about your hobbies?"
    confirm = raw_input("> ")
    if "yes" in confirm.lower() or "y" in confirm.lower():
        Nidhi.hobbies()
    print "Would you like to talk about your pets?"
    confirm = raw_input("> ")
    if "yes" in confirm.lower() or "y" in confirm.lower():
        Nidhi.pets()
    print "Would you like to hear snake facts?"
    confirm = raw_input("> ")
    if "yes" in confirm.lower() or "y" in confirm.lower():
        Nidhi.snakefacts()
    print "Would you like to play Escape Room?"
    confirm = raw_input("> ")
    if "yes" in confirm.lower() or "y" in confirm.lower():
        Josie.escape_room_lobby()
    else:
        Ravisha.smallTalk()


