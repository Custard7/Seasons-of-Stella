label alphaphi:
    #Define Variables Here
    $ maddie_points = -10
    $ anti_frat = False
    $ anti_nerd = False

    show bg black
    centered "Fall"
    show bg airport
    "Eyes wide, I step off the 747 and into the sweet, sticky, September, New-Haven air."
    "To my right, an old couple argues with a gate agent."
    "To my left, a moose gallivants across the tarmac."
    k "*hu-ugh*"
    "What a whimsical place."
    "A bright-green town car waits for me at the passenger pick-up zone."
    "Emblazoned on the side is a magical symbol."
    "The block 'Y'."
    "Yale University, here I come."

    show bg quad_busy
    "We pull up in front of a lively campus, hundreds of excited freshmen milling about the quad."
    "*SKRRRRR*"
    "I jump out of the car, dump my rucksack in my new dorm room and rush out to make new friends."
    "I wonder who my roommate will be!"
    "All around me, clubs and societies woo new students."
    show bg quad_closeup
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
            show bg quad_busy
            "I'm really not in the mood for an argument on social issues right now."
            "I walk on by as the frat bros continue their loud calls."
            "I'm sure I'll meet those two again later."
            jump club_intros

label club_intros:
    show bg quad_busy
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
    show bg quad_closeup
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
    show bg quad_busy
    "I can see that Maddie's left the sorority recruitment table."
    "Slowly, I jaunt over to check out what she was up to."
    show bg quad_closeup
    stormee "Hi There!"
    "A bright, jovial voice interrupts my internal monologue."
    stormee "I'm Stormee, president of Alpha Phi sorority here at Yale! Who are you?"
    s "I'm Stella, I'm a freshman from Montana."
    stormee "No way! I was just talking to a girl from Montana, do you two know each other?"
    s "..."
    s "...yes."
    stormee "hahaha cool!"
    "An elderly Galapagos tortoise plods by her feet."
    s "Who's that?"
    stormee "Oh, that's Keith! He's our house pet!"
    k "*hu-ugh*"
    stormee "Do you want to know more about joining a sorority?"
    if anti_nerd == True and anti_frat == True:
        "I should probably join at least one club here..."
        jump Aphi_choice
    else:
        jump Aphi_choice

label Aphi_choice:
    menu:
        "Should I tell Stormee I'm Interested in Greek life?"
        "Um, obvi.":
            s "I'm totes interested."
            stormee "haha sweet!"
            stormee "Come to the Alpha Phi house this Thursday!"
            stormee "All the actives will judge you to see if you're cool enough to deserve a bid."
            "All this jargon had my head spinning, but I was excited by the chance to climb the social ladder."
            s "I'll be there."
            s "And I'll be the best new member you've ever had."
            stormee "haha, we call them pledges, silly."
            stormee "Here's your entry card!"
            "Stormee hands me an ecru card embossed with Greek letters."
            $ inventory['Alpha Phi Entry Card'] = 1
            stormee "Come ready to be hazed!"
            jump club_outro

        "Not really.":
            s "No, not really."
            stormee "haha no worries!"
            stormee "We can all be in a bit of a whirlwind sometimes."
            stormee "Talk to us later if something changes."
            jump club_outro

label club_outro:
    show bg quad_busy
    "The welcoming events are wrapping up, I should probably head back to my dorm."
    show bg stairwell
    "I can't believe that they assigned me a six-floor walk-up."
    s "*pant*"
    tiger "Stella? Stella Belfort?"
    s "Tiger?! Wow, there sure are a lot of folks from Montana at this school."
    tiger "I'm in the Sigma Chi fraternity here! My sister Nimo is gonna join Alpha Phi. We're pretty big deals."
    tiger "You look pretty spent from these stair-climb-burpee-box-jump-arnold-tuck-curl-presses."
    tiger "Want a bite of my x1-rejuvination-power-protein-bar?"
    tiger "It's sponsored by Michael Jordan."
    s "...sure Tiger, thanks."
    tiger "See you around Stella! And remember, we're always looking for greek-life members to come join us down on Wall Street!"
    if anti_frat == True:
        s "Actually, frats are archaic institutionalized racism that promote socio-economic stratification while refusing to acknowledge the crisis of confidence present in lower-class America thanks to de jure tracking in our public school system as was upheld in {i}Cantwell v. North Dakota Board of Regents.{/i}"
        tiger "What Do You Mean?"
        tiger "ohh-oh."
    else:
        s "I'll think about it!"
        tiger "I can take you places you've never been before."

    s "..."
    s "So I'm gonna go to my dorm now."
    "I leave Tiger behind in the stairwell and walk into my dorm room."
    show bg dorm_room
    "It's a converted double."
    "Built as a bathroom but converted into a double."
    "On the top-bunk/washbasin sits a kind-looking girl."
    s "Hey I'm Stella, I think we're roommates"
    connie "Hey Stella, I'm ConTessa, but I go by Connie."
    connie "I'm in charge of the campus-wide 'Save The Juncos' initiative."
    if anti_nerd == True:
        s "That sounds really stupid."
        s "Juncos are like fat chickadees."
        s "They're the last things that need saving."
        s "You're just wasting your time."
        connie "Oh."
        connie "I didn't know you felt that way."
        connie "I'm gonna shower and go to bed."
        connie "Good night Stella."
        "Connie left the room, leaving me to reflect on my savage take-down of her bird club."
        "Someone needed to tell her the harsh truth of this world."
        "I didn't come here to make friends."
        "I came here to..."
        "I mean... I did come here to make friends."
        "But not friends like {i}her{/i}."
        jump ch1_conclusion
    else:
        s "That sounds interesting."
        s "I'd love to get to know you a bit better."
        s "Maybe I'll come to one of your club meetings sometime."
        connie "Sounds great, thanks Stella!"
        connie "I'm going to head to bed, but I'm excited to live with you!"
        jump ch1_conclusion

label ch1_conclusion:
    show bg black
    "After a shower, I slip into bed and turn off the lights."
    "What a day."
    "Tomorrow, I start classes, but I'm most excited to see where this wild train of characters takes me."
    s "*zzzzZZZZZ*"

    #Choices for next chapter
    if 'Alpha Phi Entry Card' in inventory:
        jump alphaphi_pledge
    
    elif anti_frat == True and anti_nerd == True:
        jump nofriends_pt1

    else:
        jump nerd_pt1


    return