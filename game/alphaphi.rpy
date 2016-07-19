label alphaphi:
    #Define Variables Here
    $ maddie_points = -10
    $ anti_frat = False
    $ anti_nerd = False


    centered "Fall"
    "Eyes wide, I step off the 747 and into the sweet, sticky, September, New-Haven air."
    "To my right, an old couple argues with a gate agent."
    "To my left, a moose gallivants across the tarmac."
    k "*hu-ugh*"
    "What a whimsical place."
    "A bright-green town car waits for me at the passenger pick-up zone."
    "Emblazoned on the side is a magical symbol."
    "The block 'Y'."
    "Yale University, here I come."

    "We pull up in front of a lively campus, hundreds of excited freshmen milling about the quad."
    "*SKRRRRR*"
    "I jump out of the car, dump my rucksack in my new dorm room and rush out to make new friends."
    "I wonder who my roommate will be!"
    "All around me, clubs and societies woo new students."
    cdog "Welcome, pledges!"
    durks "Do you want to party hard?"
    cdog "Do you want to pull?"
    durks "Do you want to be the smartest man on campus?"
    cdog "Do you want to be part of the freshest fraternity around?"
    durks "Come on down to the Sigma Chi house this Thursday for a recruitment kickback!"
    cdog "The drinks will be flowing."
    durks "And the ratio will be high."

    menu:
        "Talk to the frat bros.":
            s "Aren't you being a little sexist?"
            durks "I think you mean {i}sex-iest{/i}!"
            cdog "ha {i}HA{/i}!"
            "They high-five."
            s "I'm serious. Women shouldn't be demeaned."
            cdog "You know what, you've got a point, and I like your spunk."
            "I narrow my eyes. Is he man-splaining?"
            durks "I don't think we've met! I'm Durkee, but they call me The Durks."
            durks "This is my pledge brother Chance, he goes by C-Dawg."
            durks "We're the social chairs of the Sigma Chi fraternity here!"
            s "Nice to meet you guys. I'm Stella. Stella Belfort."
            s "I've never met real frat bros before."
            cdog "WHOA WHOA WHOA WHOA."
            durks "We prefer to be known as 'Fraternity Brothers.'"
            cdog "Frat-bros has kind of a bad connotation, if you know what I mean."
            durks "It was great to meet you though, Belfort!"
            cdog "Take one of our networking-cards, hit us up anytime!"
            durks "See you around, Stel-Bel!"
            $ inventory['Frat Networking Card'] = 1
            "C-Dawg and The Durks turn back to the swarms of freshmen to continue recruiting."
            "They hardly let me get a word in edgewise."
            "Seemed nice enough, though."
            jump club_intros
        
        "Flip off the frat bros.":
            s "Fuck you, you sexist pigs!"
            durks "Ouch."
            durks "Brother, my feelings are a little hurt."
            cdog "It'll be OK brother, just ignore her."
            "They give each-other a long, passionate embrace."
            $ anti_frat = True
            "I walk away feeling conflicted."
            "Was I being rude?"
            "I'm pretty sure they're the douche-bags in this situation."
            jump club_intros

        "Walk by the frat bros.":
            "I'm really not in the mood for an argument on social issues right now."
            "I walk on by as the frat bros continue their loud calls."
            "I'm sure I'll meet those two again later."
            jump club_intros

label club_intros:
    "I spot Maddie mingling around a sorority table."
    "I'll investigate once she leaves."
    "I walk among the throngs of club tables, searching for something that piques my interest."
    "*J. Cole Appreciation Club*"
    "*Wealth Management Club*"
    "*Kubb Club*"
    "*{i}Kubb: The Viking Game{/i}*"
    "Those all sound lame."
    "A sign catches the corner of my eye."
    "*Astronomy Club*"
    s "I love astrology!"
    lassi "Actually, this is astronomy club. The study of celestial bodies."
    lassi "Astrology isn't real."
    chi "Though there are some amazing constellations named for the star signs!"
    chi "My personal favorite is Libra!"
    mat "But none can compare to the Andromeda super-cluster!"
    chi "Are you interested in joining our humble club?"
    
    menu:
        "Should I join astronomy club?"
        "Yeah!":
            s "Yeah!"
            s "My name's Stella, nice to meet you!"
            lassi "Stella means star in Latin!!"
            lassi "I'm Lassi, pronounced 'law-see.'"
            chi "I'm Chi, pronounced like my favorite Greek letter!"
            mat "And I'm MatTt B., but you can call me MatTt."
            lassi "Here's a flier for out meetings!"
            $ inventory['Astronomy Club Flier'] = 1
            chi "Next week we're organizing a field trip to the new telescope installation on campus!"
            mat "I hope we see you in the library for our first meeting!"
            s "For sure! See you around guys!"
            jump aphi_intro

        "Ew.":
            s "Um, no thanks."
            lassi "...oh...ok... sorry to bother you..."
            $ anti_nerd = True
            "Honestly, they seem a little too nerdy for me."
            "I came here to be a champion, not to look at stars."
            jump aphi_intro

label aphi_intro:
    "I can see that Maddie's left the sorority recruitment table."
    "Slowly, I jaunt over to check out what she was up to."
    stormy "Hi There!"
    "A bright, jovial voice interrupts my internal monologue."
    stormy "I'm Stormee, president of Alpha Phi sorority here at Yale! Who are you?"
    s "I'm Stella, I'm a freshman from Montana."
    stormy "No way! I was just talking to a girl from Montana, do you two know each other?"
    s "..."
    s "...yes."
    stormy "hahaha cool!"
    "An elderly Galapagos tortoise plods by her feet."
    s "Who's that?"
    stormy "Oh, that's Keith! He's our house pet!"
    k "*hu-ugh*"
    stormy "Do you want to know more about joining a sorority?"
    if anti_nerd == True and anti_frat == True:
        "I should probably join at least one club here..."



    return