def family():
    print "Tell me about your family memberssss"
    statement = raw_input("> ")
    if "mom" or "mother" in statement.lower():
        print "The apple doessss not fall far from the tree."
    elif "dad" or "father" in statement.lower():
        print "Like father, like sonssss."
    elif "bro" in statement.lower():
        print "A brother may not be a friend, but a friend will alwayssss be a brother."
    elif "sis" in statement.lower():
        print "What greater thing issss there for human soulssss than to feel that they are joined " \
                    "for life."
    elif "family" in statement.lower():
        print "Ohana meanssss family, and family meanssss no one getssss left behind."
    elif "bad" or "sad" in statement.lower():
        print "Familiessss are messy. Immortal familiessss are eternally messy. Sometimessss the best we" \
                    " can do issss to remind each other that we're related for better or for worse and try to" \
                    " keep the maiming and killing to a minimum."
    else:
        print "Home issss where you are loved the most and act the worst."