﻿label start:
    scene bg city
    with fade

    """In a city name \"Duri\".
    
    Arrived a distinguish gentlemen, going to his friend's house."""

    show Dan at center
    with easeinleft

    dan.character Happy Talk "*phew* I finally arrived!~"
    dan.character Talk "It is indeed a beautiful city. "
    dan.character -Talk "Man... "
    extend "He's indeed lucky to live in this city."

    dan.character Talk "I kinda want to do a little walk in this place, "
    extend "but I need to go to my friend's house."

    dan.character -Talk "What should I do?"

    menu:
        "Do a little walk":
            call dan_goes_walk
            return
        "Go visit my friend's house":
            dan.character @ Talk "Yeah, I shouldn't make him wait now."

            hide Dan
            with easeoutright

            jump dan_goes_friends_house
            return
        
    return

label dan_goes_walk:
    dan.character Talk "A little walk around would not be a problem."

    hide Dan
    with easeoutright

    "and Dan decided to do a little walk for a bit."

    scene bg city
    with fade

    show Dan at center:
        xzoom -1.0
    with easeinright

    dan.character @ Talk "Wow~"
    dan.character @ Talk "So many good places in here.~"
    dan.character "Alright, "
    extend "It's time to go to his house now."
    dan.character "He's probably waiting for me right now."

    hide Dan
    with easeoutleft

    jump dan_goes_friends_house
    return


label dan_goes_friends_house:
    scene bg city
    with fade
    """Dan finally arrived at his friend's house"""
    return

