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
    p "No."
    "I'm shocked. I've never been turned down by a boy, let alone . . . "
    "Pucas"
    "He runs a hand through his hair, blushing."
    p "I'm sorry, I just don't like eating lunch. Dinner's fine though."
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
            $ pucas_points += 20
            "I reach down to my foot, pull off my shoe, and give it a sloppy lick."
            p "Oh you like to lick shoes? Me too!"
            "He whips off his shoe, and with a big"
            "*SLURP*"
            "Licks the bottom of his shoe."
            "We both replace our shoes."
            p "Tacos sound good. Taco Bell at 5."
    jump Pucas_goodbye

label Pucas_goodbye:

    "We slip into silence again."
    "He's starting to sweat. A steady drip goes down his forehead, slipping into the corner of his eye."
    "He flinches from the sting."
    s "Well, I'll see you later, Pucas!"
    "I'm excited for my date tonight. I'ts been a long time since I've actually gone out with anyone."
    "Pucas and I go way back."
    "Even in middle school, there was something between us."
    "I remember one time, I was on the playground, by myself. I'd forgotten my lunch, so I went out earlier than all my friends.
    Grumbling tummy, light-headed, I was pretty miserable. It was not unusual for me to forget my lunch, but that day was different, somehow. 

    I felt as if I'd let myself, my family, my ancestors down. It was sort of a low point."

    "I saw a small woodchip in the dirt. It was a little scuffed up, splintery."
    "It reminded me of myself."
    "Pucas approached me with a box of Fig Newtons. He offered me a handful, but I was too embarrassed.
    He set them on the woodchips beneath, and walked away."
    "Little did he know, that was the exact moment I fell in love with him."
    "Pucas."
    jump ganja

label ganja:
    
    "I jump back to attention."
    "Last thing I remember, Maddie Velvet was heading my way."
    "I turn around, quickly, and see-"
    star "Stella! Want some green ganja?"    
    "It's Starbuck. Pretentious and giggly, as usual."
    "She's wearing stilts underneath her gown. Apparently those are in vogue now."
    "Her bedazzled eyepatch scatters light like a discoball."
    s "Green ganja? Why would I want that?"
    star "Heehee! You'll be nervous, silly. You've got to speak in front of the WHOLE SCHOOL!"
    "She reaches into her pocket, pulls out a brownie, and shoves the whole thing in her mouth."
    s "Was that just-"
    star "Yeah. Totes. Want one?"
    "Starbuck reaches into her pocket."
    "She pulls out a brownie with pink sprinkles and buttercream icing. It's mouthwatering . . ."
    
    menu:
        "Should I take the pot brownie?"
    
        "Do it!":
            $ nicaragua_points += 10
            star "Nice dude. Here you go."
            "She tosses me the brownie."
            "I unwrap it, give it a good once over."
            "*munch*"
            s "MMf . . . Thib ib dewishus . . . huh?"
            "DAMN. That's a good brownie. But it's not . . . special."
            star "Oh, you thought THAT was the green ganja?"
            "She gazes for a second, then-"
            star "Bahahahahaha! Stella, that's one of my mom's brownies. That's nothing like green ganja."
    
        "I'll pass.":
            $ nicaragua_points -= 10
            "Starbuck frowns at me."
            star "But I thought you loved my mom's cooking!"
            "I freeze. I DO love her mom's cooking."
            s "I didn't know your mom made it! I thought it was special, like . . . "
            "I look at her knowingly"
            s "Green ganja?"
            star "Seriously?"
            "She scoffs."
            star "That's nothing like green ganja!"


label post_brownie: 
    s "It's not my fault I'm not hip on what kids are dropping these days!"
    star "You want green ganja? Here."
    "She hops off her stilts, reaches down into her shoe."
    "She's holding a small silver case. On the top of the case, engraved, are strange, runic symbols."
    "Out of the edges of the case, a verdant glow pulsates."
    star "Now this is green ganja. You want a hit?"
    "Starbuck extends the case, then clicks it open."
    "The glow pulsates with more frequency, the case gives off a high-pitched whine."

    menu:
        "Look inside?"
        
        "Just a peek . . .":
            $ nicaragua_points += 25
            "I peer over the edge of the case."
            "Inside, emitting rays of blinding neon, is a rare creature."
            "A cosmic shrimp."
            "Its long, curved body wraps around itself indefinitely, an ocean-born Ouroboros."
            "An enigmatic perfume wafts from the case, a bouquet of exotic spice and freshly hewn stone."
            "I gaze into the eyes."
            "The eyes."
            "A chasmous, neverending maelstrom of antediluvian power looms beneath surface of these inky black bulbs."
            shrimp "Forgive"
            "What is this voice?"
            shrimp "Exists no other lung save for the one through which thee breatheth."
            "A high-pitched whine rises above the chatter."
            s "Get out."
            shrimp "As once was I, thou hast been burdened with terrible purpose."
            "Terrible purpose?"
            s "Aghh!"
            "A grinding within my skull grows."
            "It's a slow, dizzying grinding, individual nodules of brain tissue being smashed on the inside of my skull by a mortar and pestle."
            "I can't move."
            "I can't think."
            "Help me."
            "It hurts."
            "You think this is a game?"
            "No. This was your choice."
            "You did this to me."
            "YOU SUBJECTED ME TO THIS!"
            "I WAS SUPPOSED TO BE SOMEONE!"
            "GO SOMEWHERE!"
            "NOT SUCCUMB TO THE FEELING THAT MY CRANIAL TISSUE, THE VERY FIBER OF MY SENTIENCE, IS BEING SPLINTERED INTO AN UNRECOGNIZABLE, PALLID MUCILAGE."
            "DEATH IS NO RELEASE. DEATH IS PHILOSOPHICAL AGONY. YOU WILL NEVER, EVER, EVER-"
            scene black
            with Dissolve
            jump stanley
    
        "I'll pass":
           $ nicaragua_points -= 10
           star "Really? What a nerd."
           s "Excuse me?"
           star "Yeah, you nerd. NERD. NERDY NERD."
           s "You don't have to be so pretentious"
           star "What do you mean {i}pretentious{/i}?"
           "She asked for it"
           "I walk up to Starbuck, nose to nose. Stare her down in the eye."
           s "Underneath that eyepatch, you're nothing more than a smelly, fuzzy-"
           "WHIIIRRRRR"
           "Starbuck's arms detach at the shoulder, revealing a web of wires and hydraulic pumps."
           "The arms crawl to the side of her head, latching on at the ear."
           star "YOU HAVE NO POTENTIAL. RESCINDING OFFER, REVERTING MEMORY FILES. GOODBYE, STELLA BELFORT."
           "The robotic voice reverberates with a tinny echo."
           "Suddenly, a cloud of fuschia gas emits from Starbuck's empty shoulder sockets."
           s "What the hell is happening? What are you, you freak?"
           "The world seems strange, a little dim."
           "Starbuck strides through the panicking crowd, spraying gas along her path"
           s "What have you . . . what have you done?"
           "My vision is fading fast."
           "What is Starbuck?"
           "Why was she here?"
           "Why did that bitch say I have no potential?"
           "*HHHSSSSSSSSSSSSSSS*"
           scene black
           with Dissolve
           jump stanley

label stanley: