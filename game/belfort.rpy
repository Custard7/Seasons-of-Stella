label belfort:

    #variables
    $ dominance = 0;
    $ favorability_taiga = 100;

    #story

    centered "==Summer=="
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
        "I sure hope so! I'm very excited to be working with you!":
            $ dominance -= 10
            $ favorability_taiga += 100
        "More prepared than you are":
            $ dominance += 75
            $ favorability_taiga -= 20
        "I have no idea what I'm doing here":
            $ dominance -= 50

    #Boss is going to prep Stella on what it means to work for morgan stanley
    # Directly copied from here http://www.morganstanley.com/people-opportunities/students-graduates/programs/institutional-securities/investment-banking/summer-analyst-north-america/

    # Wealth Management, Stella Belfort, Storgan manley, Goldman Sachs, High Frequency Trading, 
    # Subprime Mortgage Loans, Trading Floor, Michael Moore, Koch Brothers, Warren Buffet, Ponzi Schemes,
    # Real Estate, Ivy League Recruits, Internships, Bitcoin, Non-Disclosure Agreements, Entrepreneurship, 
    # Winklevoss Twins, Facebook IPO, Cocaine, Party Culture, Wolf on Wallstreet, The Big Short, Shorting, Alan Greenspan,
    # Economics, Supply and Demand, International Trade, Guest Speakers, inflation, Hedge Funds, Thai from Fox Island, 
    # Financial Advisors, Leadership
    # 