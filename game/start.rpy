# The game starts here.
label start:

    $ pucas_points = 0
    $ alpha_phi_points = 0
    $ nicaragua_points = 0
    $ belfort_points = 0
    
    "9:52 Class of 2014 Sentinel Graduation"

    s "I am the Big Stella!"

    s "Get ready for an adventure!" 
    
    s "Is it time for me to pupate?"

    #Dissolve to black
    #Chapter 1

    "I look around the hall, at the hundreds of students just like me. Waiting in anticipation from the sweet, hot release of graduation"
    "Finally, I'm ready. Ready to leave this life of being a big fish in a small pond"
    "High school was filled with drama..."
    "Across the crowded hall, an icy pair of peepers catches my eyes"
    "Of course it's Maddie Velvet, the girl who's been out to get me since I beat her in the 3rd grade grill-off."
    "She begins to stalk towards me, a predator in action."
    "This has been a long time coming. And you know, I might deserve it. Because-"
    
    p "Hey Stella!"
    
    "I whip around, surprised, upon hearing my name"
    "It's none other than Pucas P. Potato"
    "His long, fluffy blonde hair flows elegantly as he speaks. He's tall, handsome, with a rugged, masculine exterior"
    "The last time I'd talked to Pucas, we'd . . . "
    "Well, let's just say we didn't talk."
    "I'm too nervous to say anything other than-"
    s "Pucas. Hi, um. Congrats!"
    p "Congrats to me? No way, it's all on you! You're the one giving a big speech"
    "He pats me on the back. Is he patronizing me?"
    s "No, not at all. It's not that big of a deal"
    "I remember Maddie was on her way over."
    "Behind me, I see her, pacing, waiting for Pucas to leave."
    "I'm safe for now."
    p "Maddie is giving a speech too, I heard. You two have always been so impressive."
    s "Oh, you're embarassing me!"
    "He jumps backwards, a furrow of concern in his brow."
    p "I'm . . . I'm so sorry. I didn't mean to bother you."

    menu:
         "What should I do?"

         "Ask him out.":
            $ pucas_points += 10
            s "Do you want to go get lunch with me?"
            p "No."
            "I'm shocked. I've never been turned down by a boy, let alone . . . "
            "Pucas"
            "He runs a hand through his hair, blushing."
            p "I'm sorry, I just don't like eating lunch. Dinner's fine though."
            jump Pucas_continue
         "Ride him like a pony.":
            $ pucas_points -= 50
            s "I'm going to ride you like a pony"
            "That happened."
            "Afterwards, Pucas just kept staring at me. It was strange, sort of mystifying. It was as if his eyes were large black holes."
            "Inside those black holes was the old Pucas."
            "Stuck."
            "Alone."
            pause
            "He never talked again."
            jump ganja

label Pucas_continue:
    "I chuckle to myself. Typical Pucas."
    s "Great! We'll get tacos at Taco Bell at 5?"
    p "Tacos . . . "
    "He squints at me, scrutinizing my decision."
    "Does he not like tacos? Why won't he stop staring at me?"
    menu:
        "What should I do?"
    
        "Give him the ol' winkeroo":
            $ pucas_points -= 10
            "I wink at him."
            "He immediately breaks eye contact."
            p "Uh . . . Yeah, that works"

    
        "Lick my shoe":
            $ pucas_points += 10
            "I reach down to my foot, pull off my shoe, and give it a sloppy lick."
            p "Oh you like to lick shoes? Me too!"
            "He whips off his shoe, and with a big"
            "*SLURP*"
            "Licks the bottom of his shoe."
            "We both replace our shoes."
            p "Tacos sound good. Taco Bell at 5."
label Pucas_goodbye:

    "We slip into silence again."
    "He's starting to sweat. A steady drip goes down his forehead, slipping into the corner of his eye."
    "He flinches from the sting."
    s "Well, I'll see you later tonight, Pucas!"
    "I'm excited for my date later tonight. I'ts been a long time since I've actually gone on a date with anyone."
    "Pucas and I go way back."
    "Even in middle school, there was something between us."
    "I remember one time, I was on the playground, by myself. I'd forgotten my lunch, so I went out earlier than all my friends.
    Grumbling tummy, light-headed, I was pretty miserable. It was no unusual for me to forget my lunch, but that day was different, somehow. 

    I felt as if I'd let myself, my family, my ancestors down. It was sort of a low point."

    "I saw a small woodchip in the dirt. It was a little scuffed up, splintery."
    "It reminded me of myself."
    ""
label ganja:
    
    ""
    ""

