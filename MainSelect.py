import Nidhi
import Josie
import Ravisha
import Detect

def select():
    print "Would you like to talk about your family?"
    confirm = raw_input("> ")

    if Detect.yesResponses(confirm):
        Josie.family()
    print "Would you like to talk about the weather?"
    confirm = raw_input("> ")
    if Detect.yesResponses(confirm):
        Josie.weather()
    print "Would you like to talk about your hobbies?"
    confirm = raw_input("> ")
    if Detect.yesResponses(confirm):
        Nidhi.hobbies()
    print "Would you like to talk about animals?"
    confirm = raw_input("> ")
    if Detect.yesResponses(confirm):
        Nidhi.animals()
    print "Would you like to hear snake facts?"
    confirm = raw_input("> ")
    if Detect.yesResponses(confirm):
        Nidhi.snakefacts()
    print "Would you like to play Escape Room?"
    confirm = raw_input("> ")
    if Detect.yesResponses(confirm):
        Josie.escape_room_lobby()
    else:
        Ravisha.smallTalk()


