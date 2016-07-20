label belfort:

    #variables
    $ dominance = 0;
    $ favorability_taiga = 100;
    $ dominated_tiger = False

    #story

    centered "Summer"
    "24 personal essays, 14 on-line leadership seminars, several phone calls, 18 networking trips, 3.4 friends lost, and a butt-load of coffee later . . ."
    "This is it."
    "The silver crested letters stand nobly, bathing in an aura of prestige"
    "STORGAN MANLY"
    "Floating, the metallic lettering extrudes itself outwards from a glossy ocean of reflective calmness"
    "Each oceanic tile of the towering skyscraper proudly asserts itself in a faceless mesh of stability and class"
    "Lurking beneath this opaque and brilliant blue: the Kraken of capitalism"
    "Its dastardly tentacles silently take root in the soil beneath"
    "Slowly but confidently they feast on precious morsels: average American families"
    "Millions of suction cups gently envelop homeowners, small businesses, and local banks as they coax them with wealth and grandeur"
    "Waiting."
    "Waiting for the great beast beneath the waters in front of me to flex its muscles of power"
    "Sucking."
    "Sucking."
    "Sucking. All breath, all life."
    "How exciting!"
    "Rushed with the spirit of Captain Jack Sparrow, I stand on the edge of an abyss before this mighty power!"
    "I lean forward, preparing myself to be swallowed by this immense, alluring being"
    tiger "The Big Stella!"
    "I stumble"
    "Such sudden exclamation topples me backwards to reality"
    "My miraculous vision burst!"
    "I realize my mouth is wet with salivation"
    s "Tiger! Hullo!"
    s "I was hoping I would find you here!"
    tiger "Ready for your first day of leadership and success?"
    menu:
        "Ready? Huh, on my birthing table I cut my own umbilical cord with a Visa™ Credit Card and exercised my first Stock Option Agreement":
            $ dominance += 100
            tiger "Platinum Visa™?"
            s "Stainless Steel Platinum™"
            tiger "That's a platinum birth Stella. You'll fit in here."
            tiger "I'll introduce you to your manager"
        "I sure hope so! I'm very excited to be working with you!":
            $ dominance -= 10
            $ favorability_taiga += 100
            tiger "Great, I'll introduce you to your manager!"
        "More prepared than you are":
            $ dominance += 75
            $ favorability_taiga -= 20
            tiger "HEHEHE"
            tiger ". . ."
        "I have no idea what I'm doing here":
            $ dominance -= 50
            $ favorability_taiga += 20
            tiger "Steve Jobs didn't know what he was doing either"
            tiger "Then he took a calligraphy class in college"
            tiger "Now he's the most ready person there is"
            tiger "He's the leader of leaders"
            tiger "I'll introduce you to your manager so that you can get started right away on this exciting journey towards knowledge and success."
            tiger "Stella Jobs, I like the ring of that"
    tiger "Walk with me"
    jump manager_meeting
    return

label fired:

    "I walk outside."
    "The grass is wet with mildew."
    "I feel milquetoast."
    "I managed wealth . . ."
    "But I couldn't manage myself."
    "==Game Over=="

    return

label manager_dominate_sequence:

    $ aggression = 1
    while aggression > 0:

        if aggression < 1:
            tiger_manager "NO, the pleasure is actually mine."
            menu:
                "No, the pleasure is truly mine":
                    $ aggression += 1
                    $ dominance += 20
                "Haha, but really, the pleasure is actually mine":
                    $ aggression += 1
                    $ dominance -= 10
                "NO.":
                    $ aggression += 2
                    $ dominance += 30
                "Okay, the pleasure is yours":
                    $ aggression -= 1
                    $ dominance -= 40
                "Okay, dammit, the pleasure is yours":
                    $ aggression += -1
                    $ dominance += 20
        elif aggression < 3:
            tiger_manager "Okay bud, the pleasure is objectively mine"
            menu:
                "Buddy boy, back off and let me take my pleasure":
                    $ aggression += 1
                    $ dominance += 40
                "May be, but subjectively, it's mine":
                    $ aggression += 1
                    $ dominance -= 10
                "Do you even know who my dad is? *Scoff*":
                    $ aggression += 2
                    $ dominance += 50
                "Okay, the pleasure is yours":
                    $ aggression = 0
                    $ dominance -= 40
                "Okay, dammit, the pleasure is yours":
                    $ aggression = 0
                    $ dominance += 20
        elif aggression < 4:
            tiger_manager "We'll settle this outside if we have to. It's mine."
            menu:
                "Okay, let's get dirty.":
                    $ aggression += 2
                    $ dominance += 50
                "Let's settle this inside":
                    $ aggression += 1
                    $ dominance -= 20
                "Okay, the pleasure is yours":
                    $ aggression = 0
                    $ dominance -= 40
                "Okay, dammit, the pleasure is yours":
                    $ aggression = 0
                    $ dominance += 20
        elif aggression >= 4:
            tiger_manager "That's it, you're fired!"
            menu:
                "Fire me. I dare you.":
                    jump fired
                "Fuck you, your family, your first born child, Storgan Manley, Derivatives, and your fluffy hair until you let me have the pleasure of meeting you!":
                    $ aggression = -1
                    $ dominance += 1000
                    tiger_mammal "Damn. You can have it."
                    "Power moves only. It's the only way to make it in this world"
                    "Dog eat dog. Tiger eat tiger"
                    s "I am the tiger now."
                    tiger_mammal "I like you"
                    $ favorability_taiga += 100
                    tiger_mammal "You're gonna go far here, kid"
                    tiger_mammal "I always like to test the new recruits. See if they are made of somethin'"
                    tiger_mammal "Sometimes you get the weaklings. The plastic knockoffs of real meat n' bone tigers"
                    tiger_mammal "Welcome to the jungle"
                    $ dominated_tiger = True
                "Okay, the pleasure is yours":
                    tiger_mammal "Oh, it's too late for that!"
                    jump fired
                "Okay, dammit, the pleasure is yours":
                    tiger_mammal "Oh, it's too late for that!"
                    jump fired
    return


label manager_meeting:

    #Scene in the waiting room of a fancy office

    "I wonder what's taking the manager so long to see me"
    "I emailed him this morning, he told me to meet here at 9:05 on the dot"
    "==9:21== the elegant clock above me reads"
    "I hope he didn't forget about me . . ."

    #Scene up inside Storgan Manley's Office
    tiger_manager "Hullo!"
    "A refined and young gentlemen emerges from the monolithic doors to my right"

    if dominance > 0:
        s "Pleasure to meet you Mr. Manley, my name is Stella."
        s "The Big Stella."
        tiger_manager "No, the pleasure is mine Ms. Stella."
        menu:
            "No, the pleasure really is mine, Mr. Manley":
                call manager_dominate_sequence
            "Yes, the pleasure is yours, Mr. Manley":
                tiger_manager "You've got a good head on your head, I like you"
                $ favorability_taiga += 40
    else:
        s "Mr. Manley! So good to meet you, I was worried . . ."
        tiger_manager "Worry not, child. You must have thought I forgot about you?"
        tiger_manager "That I don't have time for the petty scuttling of new recruits amidst my terribly busy schedule."
        tiger_manager "That I would prefer to spend my waking hours managing the world's wealth over holding your hand on your first day here."
        tiger_manager "But this is non-sense, I forget no one."

    if dominated_tiger:
        "Mr. Manley gestures me into his office, smiling as he waits for me to enter first"
    else:
        "Without gesture Mr. Manley walks into his office, leaving his door open"


    #Boss is going to prep Stella on what it means to work for morgan stanley
    # Directly copied from here http://www.morganstanley.com/people-opportunities/students-graduates/programs/institutional-securities/investment-banking/summer-analyst-north-america/

    # Wealth Management, Stella Belfort, Storgan manley, Goldman Sachs, High Frequency Trading, 
    # Subprime Mortgage Loans, Trading Floor, Michael Moore, Koch Brothers, Warren Buffet, Ponzi Schemes,
    # Real Estate, Ivy League Recruits, Internships, Bitcoin, Non-Disclosure Agreements, Entrepreneurship, 
    # Winklevoss Twins, Facebook IPO, Cocaine, Party Culture, Wolf on Wallstreet, The Big Short, Shorting, Alan Greenspan,
    # Economics, Supply and Demand, International Trade, Guest Speakers, inflation, Hedge Funds, Thai from Fox Island, 
    # Financial Advisors, Leadership
    # 