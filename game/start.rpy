# The game starts here.
label start:

    $ pucas_points = 0
    $ alpha_phi_points = 0
    $ nicaragua_points = 0
    $ belfort_points = 0
    $ stanley_influence = False
    $ Pucas_flirt = False
    $ stella_saw_shrimp = False
    $ stella_saw_starbuck = False
    $ tiger_lick = False

    $ inventory = {};
    
    "9:52 Class of 2014 Sentinel Graduation"

    s "I am the Big Stella!"

    s "Get ready for an adventure!" 
    
    s "Is it time for me to pupate?"

    #Dissolve to black
    #Chapter 1

    "I look around the hall, at the hundreds of students just like me. Waiting in anticipation from the sweet, hot release of graduation."
    "Finally, I'm ready. Ready to leave this life of being a big fish in a small pond."
    "High school was filled with drama..."
    "Across the crowded hall, an icy pair of peepers catches my eyes."
    "Of course it's Maddie Velvet, the girl who's been out to get me since I beat her in the 3rd grade grill-off."
    "She begins to stalk towards me, a predator in action."
    "This has been a long time coming. And you know, I might deserve it. Because-"
    
    p "Hey Stella!"
    
    "I whip around, surprised, upon hearing my name."
    "It's none other than Pucas P. Potato."
    "His long, fluffy blonde hair flows elegantly as he speaks. He's tall, handsome, with a rugged, masculine exterior."
    "The last time I'd talked to Pucas, we'd . . . "
    "Well, let's just say we didn't talk."
    "I'm too nervous to say anything other than-"
    s "Pucas. Hi, um. Congrats!"
    p "Congrats to me? No way, it's all on you! You're the one giving a big speech."
    "He pats me on the back. Is he patronizing me?"
    s "No, not at all. It's not that big of a deal."
    "I remember Maddie was on her way over."
    "Behind me, I see her, pacing, waiting for Pucas to leave."
    "I'm safe for now."
    p "Maddie is giving a speech too, I heard. You two have always been so impressive."
    s "Oh, you're embarassing me!"
    "He jumps backwards, a furrow of concern in his brow."
    p "I'm . . . I'm  so sorry. I didn't mean to bother you."

    menu:
         "What should I do?"

         "Ask him out.":
            $ pucas_points += 10
            s "Do you want to go get lunch with me?"
            jump Pucas_continue

         "Ride him like a pony.":
            $ pucas_points -= 50
            s "I'm going to ride you like a pony."
            "That happened."
            "Pucas stares at me. It's strange, sort of mystifying. It's as if his eyes were large black holes."
            "Inside those black holes is the old Pucas."
            "Stuck."
            "Alone."
            pause
            "He may never talk again."
            $ Pucas_flirt = False
            jump ganja


label Pucas_continue:
    p "No."
    "I'm shocked. I've never been turned down by a boy, let alone . . . "
    "Pucas."
    "He runs a hand through his hair, blushing."
    p "I'm sorry, I just don't like eating lunch. Dinner's fine though."
    "I chuckle to myself. Typical Pucas."
    s "Great! We'll get tacos at Taco Bell at 5?"
    p "Tacos . . . "
    "He squints at me, scrutinizing my decision."
    "Does he not like tacos? Why won't he stop staring at me?"
    menu:
        "What should I do?"
    
        "Give him the ol' winkeroo.":
            $ pucas_points -= 10
            "I wink at him."
            "He immediately breaks eye contact."
            p "Uh . . . Yeah, that works."
            $ Pucas_flirt = False
    
        "Lick my shoe.":
            $ pucas_points += 40
            "I reach down to my foot, pull off my shoe, and give it a sloppy lick."
            p "Oh you like to lick shoes? Me too!"
            "He whips off his shoe, and with a big"
            "*SLURP*"
            "Licks the bottom of his shoe."
            "We both replace our shoes."
            p "Tacos sound good. Taco Bell at 5."
            $ Pucas_flirt = True
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
            "I look at her knowingly."
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

    $ stella_saw_shrimp = False;
    $ stella_saw_starbuck = False;

    menu:
        "Look inside?"
        
        "Just a peek . . .":
            $ nicaragua_points += 25
            $ stella_saw_shrimp = True
            "I peer over the edge of the case."
            "Inside, emitting rays of blinding neon, is a rare creature."
            "A cosmic shrimp."
            "Its long, curved body wraps around itself indefinitely, an ocean-born Ouroboros."
            "An enigmatic perfume wafts from the case, a bouquet of exotic spice and freshly hewn stone."
            "I gaze into the eyes."
            "The eyes."
            "A chasmous, neverending maelstrom of antediluvian power looms beneath surface of these inky black bulbs."
            shrimp "Forgive."
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
            #with Dissolve
            jump stanley
    
        "I'll pass.":
           $ nicaragua_points -= 20
           $ stella_saw_starbuck = True;

           star "Really? What a nerd."
           s "Excuse me?"
           star "Yeah, you nerd. NERD. NERDY NERD."
           s "You don't have to be so pretentious."
           star "What do you mean {i}pretentious{/i}?"
           "She asked for it."
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
           #with Dissolve
           jump stanley

label stanley:
    "I open my eyes and find myself passed out in a non-descript parking lot."
    "Still woozy, the birds tweeting nearby seem to spiral in circles around my head."
    "*tweet tweet*"
    "The air tinges my lungs as I attempt to breathe in this sticky, salty solution wafting around me."
    "My ears perk up to a combination of grunts and clinking metal."
    "*clink* *ungh* *clink*"
    "I look above at the building in front of me."
    "SWOLL INC., the sign reads."
    "SYNERGIZING GIBBOUS SOLUTIONS SINCE 1997"
    if stella_saw_starbuck == True:
       "Why do I have a lingering desire for a caramel macchiato?"
    else:
       "A tingling sensation shoots through the entirety of my being as if a microscopic sea crustacean were slowly gnawing on my nervous system."
    tiger "Dude, you look like you need some X1 Fiber Infused Kombucha."
    "I whip towards this gentle voice."
    s "Hey! Who are you? My day has been pretty tough."
    tiger "Elon Musk said, 'tough times don't last, but tough people do.'"
    "One of his hands reaches out with an overflowing bottle of Fiber-bucha."
    menu:
        "Aggressively guzzle the Fiber-bucha.":
            $ belfort_points += 25;
            "I immediately clamp my hands around the girthy container."
            "I raise up this chalice of health and fitness and roar to the Gods."
            "Like the glorious fountains of lore, I bathe myself in its golden, liquid delivery."
            "I relish the individual, living microbes as they lusciously spurt over me."
            "Kombuch-yeah."
            tiger "Woah. Dude."
            tiger "That was innovative."
            s "Call me Stella, the Big Stella."
            tiger "I'm Tiger, Tiger Mammal."

            label buzzwords:
                tiger "Innovation"
                tiger "Synergy"
                tiger "Local"
                tiger "Organic"
                tiger "Green Foods"
                tiger "Joe Biden"
                tiger "Benghazi"
                tiger "Collaboration"
                tiger "Right Brain Thinkers"
                tiger "Scalable Server Technology"
                tiger "The Green Cheddar"
                tiger "High Frequency Trading"
                tiger "Fracking"
                tiger "Wealth Management"
                tiger "Income Inequality"
                tiger "The Fiscal Cliff"
                tiger "Super PACs"
                tiger "Subprime Mortgage Loans"
                tiger "Derivatives"
                tiger "Subprime Mortgage Derivatives"
                tiger "Sustainable"
                tiger "Intuitive"
                tiger "Snappy"
                tiger "Viral"
                tiger "Synergy"
                tiger "Brain food"
                tiger "Globalization"
                tiger "Disruption"
                tiger "Entrepreneurship"
                tiger "Leadership"
                tiger "These are all words"
                tiger "Do they appeal to you?"
    
                menu: 
                    "Yes. They indeed appeal.":
                        $ belfort_points += 5
                    "Yes. Especially the wealth management one. Screwing over the average American family tickles me pink.":
                        $ belfort_points += 20
                    "No. They do not appeal to me.":
                        tiger "Did you hear me?"
                        $ belfort_points -= 15
                        jump buzzwords
                tiger "Here, take my card."
                "--TIGER MAMMAL: INNOVATIVE LEADER IN WEALTH MANAGEMENT--"
                "--STORGAN MANLY (406)-830-5053--"
                tiger "This world is full of these words."
                tiger "You could be a leader in this space."
                tiger "A leader."
                $ stanley_influence = True

        "Slap the Fiber-bucha into his face.":
            $ belfort_points -= 20;
            "Disgusted, I slap the Fiber-bucha into a miraculous array of bougie goodness across his face."
            s "Um. No thanks, Kombucha is part of the milk industry and the milk industry ruins children's lives by paying billions of dollars to make them love milk when really biologically milk was never made for children just for kittens but I'm not a kitten so I don't want your corporate milk industry derived sheep of a sellout komubcha."
            s "How about, Kombuch-NO."
            "Tiger Mammal looks at me, dripping with yogurt drank."
            tiger "I would be upset, but I will 'Turn the other cheek' as Michael Jacksón once said." 
            menu:
                "Lick the Fiber-bucha off of Tiger's Abercrombie abs.":
                    "I stick my tongue out"
                    tiger "*sticks his tongue out*"
                    $ tiger_lick == True
                    "Gravity draws each of us like falling towers towards one another . . ."
                    tiger "Wait, we need some Glotion™."
                    tiger "It's an innovative combination of lotion and glue."
                    tiger "It's great for children's craft and as a lubricant which gradually increases in friction."
                    "Tiger Mammal walks over to the Glotion™ Vending machine and purchases several bottles."
                    tiger "The machine gave me a few extra, do you want them?"
                    menu:
                        "Yes.":
                            $ inventory['glotion'] = 10;
                            s "Thanks!"
                            "I put 10 bottles of Glotion™ in my back pocket."
                        "No.":
                            s "No Thanks. I prefer self-lubrication to the wonderful, creative, and ergonomic product that is Glotion™."
                            tiger "You're loss. Glotion™ is the #1 trusted brand in glue lubricants."
                            tiger "10/10 Lubricant Dr.s agree."
                    "Tiger pours out a steaming pile of fresh Glotion™ into his cupped hands. He begins glotioning the nape of my neck."

                "Slap him again.":
                    "I slap him back to childhood."
                    babytiger ""
                    babytiger "'Is it too late just to say sorry?'"
                    babytiger "I'm a belieber it's not."
                    "I slap him once more back to adulthood."
            tiger "I need to go take a shower."

    nimo "Tiger Mammal! Nani o shimasuka?!"
    if tiger_lick == True:
        s "I withdraw my tongue"
    tiger "Nimo! Ugh, I had already finished my single set of dumbell barbench curls. I'm spent."
    nimo "Whatever Tiger, ugh."
    nimo "Who are you?"
    s "I am the Big Stella."
    if stella_saw_shrimp == True:
       s "... minion puppet of the crustacean underlord ..."

    nimo "Aren't you giving that big speech today?"
    s "OH MY! Yes, yes I am."
    "I had almost forgotten! The biggest moment of my life!"
    s "What time is it?"
    nimo "Time to get you going! The Big Stella can't make the whole town wait!"
    nimo "Come on, I'll give you a ride."
    nimo "*wink*"
    scene black
    #with Dissolve
    jump alpha_phi

label alpha_phi:
    "As Nimo drops me off in front of the gymnasium, I hastily check my phone."
    if Pucas_flirt == True:
        '*TWO UNREAD MESSAGES*'
        '*FROM: PUCAS POTATO*'
        '*Thinking about you Stella ;)*'
        '*PUCAS SENT A PHOTO*'
        "Huh, I'd have to check that later."
    else:
        '*ONE UNREAD MESSAGE*'
        '*FROM: DAD*'
        '*Where are you! They need you in the green room*!'
    'The big speech! I just need to find my notes...'
    m 'Hey Stella.'
    s '*UAGH*'
    "Maddie had snuck up on me!"
    "I'm trapped', like a lone salmon who'd made the treacherous journey back to her spawning grounds only to discover a recently constructed dam, built to divert stream flow to a dilapidated alpaca ranch."
    s "Hey Maddie... are you... ready for your speech?"
    m "*scoff*"
    m "I could ask you the same question."
    s "Well, I can't seem to find my notes..."
    m "Oh those? I used them as rolling papers."
    m "Nice Bernie Sanders quotes in there. {i}reeeal{/i} original."
    "I can't take this right now, the pettiness, the bad memories..."
    s "Maddie, what do you want?"
    m "I just wanted to know if you wanted to speak before or after me."
    "I scrutinize her, searching for some genuine emotion in her icy eyes."
    "Is she asking me out of genuine kindness, or is this another one of her trademark power plays?"
    "Maddie always was one I never could get a read on."
    "Her and..."
    if Pucas_flirt == True:
        s "...Pucas"
        m "Pucas? Are you daydreaming about that nerd?"
        "I must have said that out-loud."
        s "n-n-no, I..."
        m "*HA*"
        m "Stella and Pucas siting in a tree."
        m "B - E - I - N - G    G - D - Is"
        menu:
            "Ask Maddie what a GDI is.":
                s "GDI?"
                m "Of course you wouldn't know what that is."
                m "Talk to me next year at Yale."
                m "My mom was president of her Sorority."
                $ alpha_phi_points += 25
            "Tell Maddie to Screw Off.":
                s "Screw Off, Maddie."
                m "You can't talk to me that way."
                m "Do you know who my mom is?"
                $ alpha_phi_points -= 10
    else:
        s "...Tiger"
        m "Tiger? He's pretty frat."
        "I must have said that out-loud."
        s "n-n-no, I..."
        m "*HA*"
        m "Stella. Tiger would {i}never{/i} be your friend."
        m "You're a total GDI."
        menu:
            "Ask Maddie what a GDI is.":
                s "GDI?"
                m "Of course you wouldn't know what that is."
                m "Talk to me next year at Yale."
                m "My mom was president of her Sorority."
                $ alpha_phi_points += 25
            "Tell Maddie to Screw Off.":
                s "Screw Off, Maddie."
                m "You can't talk to me that way."
                m "Do you know who my mom is?"
                $ alpha_phi_points -= 10        
    m "Do you know what she drives?"
    m "A 2004 Subaru Cross-Trek."
    "I'm not sure I've ever even seen that car."
    m "A CROSS-TREK."
    m "Anyways, what order do you want to speak?"
    menu:
        "Tell Maddie I want to speak first.":
            s "I want to go first."
            $ alpha_phi_points +=15
            m "Think you're a big dawg, huh?"
            s "I'm really more of a big tiger."
            if stella_saw_shrimp == True:
                s "...destined to conquer this world for our subterranean master."
            elif stanley_influence == True:
                s "Ready to screw over some average American citizens!"
                s "Like your mom."
            elif Pucas_flirt == True:
                s "A tigress in an empty den, just dreaming for my strong man-tiger to find me."
            else:
                s "A tiger with no direction in her life."
            m "Wow, you really need to get some friends."
            m "Well get out there, Everyone's waiting on you."
            jump big_speech

        "Tell Maddie she can speak first.":
            s "You can go first, I guess."
            $ alpha_phi_points -= 5
            m "Good old reliable Stella Belfort."
            m "Never willing to step out of her comfort zone."
            "Maddie is really irkin' the ol' nerves."
            s "I do too!"
            s "I had a day you wouldn't even be able to dream up."
            if stella_saw_shrimp == True:
                s "but soon, you and all your flunkies will be dreaming..."
                s "...at the bottom of the sea."
                s "Minions to our supreme creator."
            elif stanley_influence == True:
                s "And soon, I'll be on Wall Street."
                s "Stacking bands and sipping on crisp Fiber-bucha."
            elif Pucas_flirt == True:
                s "And soon, the man of a generation will be mine."
            else:
                s "And soon, maybe I'll find some direction in my life."
            s "Now I've got a speech to give."
            m "After me, nerd."
            "Maddie trounced out to the podium, leaving me in the green room to reflect on our constant feuding."
            "Why did this girl hate me?"
            "What could I do to make it stop?"
            "Does she think I'm taking something away from her by giving a speech?"
            "I hear the applause die down, and ready myself for the moment I would finally show the world Stella Belfort."
            jump big_speech

label big_speech:
    "An expanse of eager faces lies in front of me."
    "Everyone's waiting."
    "Anticipating."
    "Excited to hear what I have to tell them."
    airhorn "*BWWWWWAAAAAAAAAAAAAAH*"
    "I don't have my notes, I'll have to ad-lib."
    s "Students, teachers, and honored guests, I'm blessed to stand before you today."
    s "High School was a time for us to learn about ourselves."
    s "Learn about our goals."
    s "Our ambitions."
    s "And maybe even find a little love along the way."
    if Pucas_flirt == True:
        p "*blush*"
        jump speech_continue
    else:
        jump speech_continue
label speech_continue:
    s "Next year, we'll be off around the world, doing great things."
    s "College will be a different time, with new friends and new things to learn."
    s "But it's always important to remember everyone who helped you along the way."
    s "Your friends who offered their help when you needed it most."
    s "Even your enemies who pushed you to be the best person you could be."
    airhorn "*BWWWWWAAAAAAAAAAAAAAH*"
    s "I'd like to thank my fellow students for choosing me to speak at graduation."
    airhorn "*BWAA-BWAAAA-BWWWWWAAAAAAAAAAAAAAH*"

    #Choose path here!
    if max(alpha_phi_points, pucas_points, belfort_points, nicaragua_points) == alpha_phi_points:
        s "Next year, I'm excited to attend Yale University."
        s "I hope to meet many new people there."
        s "And climb to the very top of the social ladder."
        airhorn "*BWWWWWAAAAAAAAAAAAAAH*"
        "Maddie gives me the finger."
        s "And soon, I'll have so many friends, I won't even need you suckers!"
        s "Tomorrow is the next-first day of our lives! Let's make the most of it!"
        "The gym erupts in applause, and I am content."
        jump alphaphi

    elif max(alpha_phi_points, pucas_points, belfort_points, nicaragua_points) == pucas_points:
        s "Tonight, I'll embark on the date of my life with a wonderful man."
        s "A man who's luscious blonde locks make me feel things I've never felt before."
        s "Taco Bell."
        s "A beefy five layer burrito."
        s "5 PM tonight."
        s "Sparks will fly."
        s "Tomorrow is the next-first day of our lives! Let's make the most of it!"
        "The gym erupts in applause, and I am content."
        jump pucas


    elif max(alpha_phi_points, pucas_points, belfort_points, nicaragua_points) == belfort_points:
        s "Today, I discovered a new passion."
        s "A passion for cheddar."
        s "Fat stacks."
        s "The benjamins."
        s "Racks on racks."
        s "Decimals and commas."
        s "Dat moo-lah."
        s "And next year, I'm going to pursue the fantasy I never knew I had:"
        s "Screwing over the average American family."
        s "Tomorrow is the next-first day of our lives! Let's make the most of it!"
        "The gym erupts in applause, and I am content."
        jump belfort


    elif max(alpha_phi_points, pucas_points, belfort_points, nicaragua_points) == nicaragua_points:
        s "It's important to remember that our life is so short."
        s "We have to make sure we have a little fun along the way."
        s "Which is why next year I plan to smoke 'da green ganja in Nicaragua."
        s "Searching for more to fight the good fight..."
        s "For our glorious leader..."
        s "Darmascula."
        s "All hail."
        s "Tomorrow is the next-first day of our lives! Let's make the most of it!"
        "The gym erupts in applause, and I am content."
        jump nicaragua


