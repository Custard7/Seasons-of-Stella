label pucasCh1: 
    $ sexy_factor = 100
    $ ate_falafel = False
    $ grabbed_drumchata = False
    play "snowmen.mp3" loop
    show bg black
    centered "Winter"
    centered "1.5 years later"
    show bg snowy_road
    with dissolve
    "It's cold."
    "Even in the car, the cold seeps through the thin window panes."
    "Our breath is frozen onto the inside of the glass, a web of crystal."
    "I let out a little shiver."
    jacques "You're cold? We're close to my cabin."
    "Jàçqüés turns to me, and nods reassuringly."
    "I've known Jàçqüés for years."
    "Our dads used to work together, so we ran in to each other at work functions often."
    "Now, he's going to school in California."
    "He takes one of his tiny hands off the steering wheel, and points to his shirt."
    "It's a cute little walrus face."
    jacques "Good thing my spirit animal is a walrus. Otherwise I'd be freezing too!"
    "He turns back to the wheel, concentrating on the crunchy, snowy road."
    prof "Jàçqüés, I'm tired desu."
    jacques "Stop."
    jacques "Whining."
    jacques "Dirty weaboo."
    prof "Grrrrr."
    "From the back seat, Professor Fukklesprout grumbles."
    "He's lanky, with long, brown hair that hangs in his face like an anime character."
    "After spending time in Japan, he developed some strange psychological disorder, where he thought he was still in Japan."
    "When I first met him, he'd only speak Japanese."
    "Slowly, over the last few years, he's come out of his shell and used English again."
    frito "Yeah Fukklesprout, cut it out, you little bitch."
    "Frito Cubby glares at him over top her glasses."
    "I never went to school with Frito. She went to the school across town."
    "She's always felt a little enigmatic to me, like somehow, I'm her competition."
    "But, she's so much fun to have around, so it's not a big deal."
    "She pulls a small takeout box out of her coat pocket."
    frito "Have some of this, it'll warm you up."
    "Fukklesprout peers around the box curiously."
    prof "This kind of looks like a box I had in Japan once. When I opened it up, a bunch of really kawaii neko popped out from the box and gave me an allergy attack. What's in here?"
    zach "Just open it."
    "Zach Peterson."
    "What a guy."
    "He was in many of my classes in high school."
    "An expert cartographer, statistician, and master of wit, Zach was one of my most valuable assets in high school."
    "He's also quite the catch."
    "His red hair flows in elegant dreads, like an Irish reggae band's frontman."
    zach "Come on. What's the worst it could be?"
    "Fukklesprout sighs."
    "He pops the lid on the box."
    prof "Aaagggghhhh!!!!"
    frito "Hahahaha, suck it, nerd."
    zach "Nice going dude."
    "Frito and Zach hi-five overtop Fukklesprout."
    "I peer over the edge of the box."
    "Inside is a big chunk of falafel."
    menu: 
        "Stuff the falafel in your mouth.":
            $ sexy_factor -= 20
            $ ate_falafel = True
            "I reach into the box, pluck up the piece of falafel, and plop right in my mouth."
            "It's pretty big, but I swallow it with only minor difficulty"
            "Fukklesprout glares at me warily."
            "His eyes grow enormous."
            prof "You... You monster!"
            frito "That was hella weird, yo."
            "The taste of falafel spreads throughout my palate, powerful, savory flavor."
            "I look at Frito and give her a satisfied nod."
            s "What a tasty piece of falafel."
            "Frito, Zach, and Fukklesprout recoil in disgust."
            zach "Damn, that is some nasty falafel breath!"
            prof "Literally, for real, I'm gonna throw up."
            s "Well, sorry I enjoy falafel."
            frito "Yeah, and it seems like we're going to 'enjoy' the smell of it for the next two days."
            zach "They can probably smell it all the way in Tristan da Cunha, the world's most remote inhabited island chain."
            "Zach's geographical prowess isn't always helpful . . . "
            s "Lay off, okay? It can't be that bad."

        "Giggle obnoxiously":
             prof "This isn't funny, Stella!"
             prof "GET THIS GARBAGE AWAY FROM ME!"
             "He quickly rolls down the window, letting in a rush of cold air."
             prof "BEGONE FOUL SUBSTANCE!"
             "He hucks the box with his full strength."
             "It lands with a-"
             "*poof*"
             "-before sinking into the twilit snow."
             frito "Hey, come on man, that was my dinner!"
             prof "You all KNOW how much I hate non-Japanese food!"
             "Jàçqüés rolls his eyes. He must be used to this."
             jacques "Just deal with it, dude. Most of the world isn't Japanese, so you're going to have to be a little flexible."
             "Fukklesprout throws up a peace sign in exasperation."
             prof "Just, just leave me alone, okay! The only person who cares about me is my girlfriend. Good thing I can talk to her on the phone, instead of getting bullied by you falafel-lovers."
             "He pulls out his Pikachu-cased smartphone, with a little anime girl keychain attached."
             "Fukklesprout types furiously."


    jacques "Well, you all can stop bitching, because we're finally here! New Year's 2K16 is a GO!"

    show bg cabin_exterior
    with fade
    "We all hop out of the car, our breath steaming up in the biting air."
    "The trees rustle in a light winter breeze, shaking off a cascade of powder."
    "Nestled underneath the canopy is Jàçqüés' cabin."
    "Its rustic wood exterior is worn, but in just the right way."
    "I've never seen anything so tranquil in my life."
    s "Jàçqüés, this place is incredible!"
    jacques "Well, my papa built it with his own two hands, so you have him to thank for that."
    jacques "Let's unpack the car."
    frito "I didn't pack anything, so I'm not unloading anything."
    prof "I'm too traumatized to carry anything."
    zach "I just don't want to."
    frito "We're going to wait by the door."
    "Frito, Fukklesprout, and Zach stride through the snow to the door of the cabin."
    "Jàçqüés sighs deeply."
    jacques "Well, can {i}you{/i} help me, Stella? I can't carry all this stuff in by myself."
    menu: 
        "Help him":
            s "Yeah, no problem!"
            "Jàçqüés walks around to the back of his car and opens up the trunk."
            "He beckons me to come around."
            "In the back of his trunk are several large boxes, a sheathed broadsword, and a 50 gallon drum, labeled 'Drumchata'."
            jacques "Thanks so much, Stell. You're being a huge help! Just grab something and I can get the rest."
            menu:
                "Grab the Drumchata":
                    $ grabbed_drumchata = True
                    "I reach forward into the trunk, and wrap my arms around the Drumchata."
                    jacques "You sure you got that?"
                    s "Yeah, I'm fine"
                    "I heft up the giant drum."
                    "I'm not fine."
                    "I waddle a few feet, barely keeping my balance on the compacted snow."
                    "This thing is way too heavy!"
                    "My grip starts to slip, so I lean backwards to lift the drum up higher."
                    s "Ahhh!"
                    "The snow gives way under my feet, and I'm falling."
                    "The giant drum looms above, plummeting towards me in slow motion."
                    "This is it. I've lived a good life, but I never got to fix things with-"
                    s "Pucas."
                    "Ka-Ching!"
                    "The drum flies across the snowy road, landing with a *THUD* at the foot of the door."
                    "Standing above me, gleaming broadsword in hand, is none other than Pucas P. Potato."
                    "What is he doing here? I had no idea..."
                    "He's grown older since the last time I saw him. You can sense the wisdom behind his strong, masculine features."
                    "He reaches down a hand to me."
                    "I take it."
                    "With a mighty heave, he rights me."
                    p "Are you all right?"
                    "I'm breathless, so I nod."
                    p "Glad to hear."
                    jacques "Pucas, that was awesome. Mind carrying the broadsword in?"
                    "Pucas nods, sheathes the blade."
                "Grab the broadsword":
                    "I reach for the broadsword."
                    "It's kind of heavy, but I can handle it."
                    "I stride toward the front door of the cabin, being careful not to step on any-"
                    "Ice."
                    s "Aahhhhhhh!"
                    "*SHICK*"
                    "I'm lying on my back."
                    "Looking down, I see-"
                    "A broadsword sticking out of my chest."
                    s "Oh God-"
                    jacques "Stella..."
                    "Jàçqüés flees into the woods."
                    "My vision begins to fade."
                    "This can't be happening."
                    "Not now."
                    "Not before I get to fix things with-"
                    s "Pucas."
                    show bg black
                    with fade
                    centered "Maybe you shouldn't have been so arrogant."
                    centered "Have you ever even handled a broadsword before?"
                    centered "Either way, you made a mistake."
                    centered "Which means-"
                    centered "YOU DIED"
                    return
                "Grab some boxes":
                    $ sexy_factor -= 20
                    "I pick up several boxes."
                    jacques "Getting ambitious there, Stell. Make sure you don't drop anything!"
                    s "Don't worry, I've got it."
                    "I step carefully through the snow. After all, I'd hate to drop whatever is in here."
                    "*clink*"
                    "The contents of the box rattle about."
                    s "What's in here, by the way?"
                    "I glance a Jàçqüés, who is hefting the Drumchata with one hand."
                    jacques "For real, just wine."
                    s "Oooh, nice! What kind of-"
                    "My foot shoots through a spot in the snow."
                    s "Ahhhh!"
                    "*clink*"
                    "*clang*"
                    "*CRASH*"
                    "A bottle lands full force right on my cheekbone."
                    "Wine bottles are scattered throughout the snow."
                    jacques "Stella! Are you all right? Let me help you clean that up."
                    "He tosses the Drumchata toward the doorway. It lands with a resounding *THUD* at the foot of the door."
                    p "Hey, can I help bring anything in?"
                    s "Pucas?"
                    "Standing in the twilight is an illuminated silhouette."
                    "Belonging to none other than Pucas P. Potato."
                    p "That was a pretty gnarly fall, Stella! You've got a big-"
                    "He gestures awkwardly to my face."
                    p "-thing, going on there. Looks like it hurts."
                    "In the reflection of a nearby wine bottle, I see a large bruise beginning to form on my face."
                    "I recoil in embarrassment."
                    "I can't believe this happened, in front of Pucas of all people!"
                    jacques "Hey Pucas, would you mind carrying that broadsword while I help Stella here?"

        "Kick him in the shin":
            "Why would he think that I, Stella Belfort, should carry any of his dirty stuff in?"
            "I bring back my leg and swing with all my might."
            "*WHACK*"
            "Jàçqüés recoils, grabbing his shin in agony."
            "His keys fly out of his hands, and into the snow."
            jacques "Dammit! What was that for?"
            "He winces, as blood soaks through the leg of his jeans."
            s "Don't presume that I'll carry things for you, Jàçqüés."
            "He glares at me."
            jacques "Why do you always have to be so pretentious, Stella? This is why you didn't have any friends in high school."
            "What did he just say to me?"
            s "You can't just {i}say{/i} that to people, Jàçqüés. What gives you the right to-"
            jacques "Oh no."
            s "What, are you gonna cry now?"
            "Jàçqüés hobbles over to me, a look of horror in his eyes."
            jacques "Stella, did you see where I dropped the keys?"
            s "You dropped the keys?"
            jacques "Yeah, when you kicked me, I let go reflexively..."
            "He puts a hand to his forehead, fear glazing over his eyes."
            jacques "Stella Belfort. We are 50 miles into the mountains, a minimum of 10 miles from the nearest house. It's almost sunset, and we have no car, no food, and no way of getting inside the cabin."
            "I can't..."
            "I can't believe I did that."
            s "Can't we look for the keys?"
            jacques "We can, but we better do it fast. These mountains, well-"
            "He leans in close."
            jacques "-let's just say we're not alone."
            "I gaze out into the darkening forest."
            "*shudder*"
            "What have I done?"
            show bg black
            with fade
            centered "Three Days Later"
            centered ". . ."
            centered ". . ."
            centered ". . ."
            show bg coldforest
            with dissolve
            "It's been three days since we lost the keys."
            "We tried to follow the creek west, but when Fukklesprout fell in, we began to break down."
            "Frito was the first to suggest that we eat him."
            "We didn't want to at first."
            "But we were so cold."
            "So-"
            centered "{size=+30}HUNGRY{/size}"
            $ renpy.pause(3)
            "After Fukklesprout, Frito, Zach, and even Jàçqüés succumbed to cold and hunger."
            "Now its just me."
            "Ever since Jàçqüés went, I've heard strange echoes from the trees."
            "I know they're getting closer."
            beast "*ah uh* *ah uh*"
            $ renpy.pause(1)
            beast "ooooooOOOOO AH AH!"
            centered "{size=+30}Help Me{/size}"
            show bg black
            with fade
            centered "Looks like you made the wrong choice."
            centered "Instead of just offering help to your friend, your arrogance got in the way."
            centered "Now? You're dead."
            centered "Well, good as dead, anyway. Once {i}they{/I} get to you."
            centered "Not only that, but all of your friends are dead, too."
            centered "Regardless, you really screwed up big time on this one."
            centered "Which means-"
            centered "YOU DIED"
            return

    "He struts toward the house, broadsword slung on his back, a swagger to his step."
    jacques "That could have been really bad, Stella. Try and be more careful next time!"
    "I nod. This was definitely my bad."
    if grabbed_drumchata:
        "Good thing Pucas was there to save the day."
    "Jàçqüés helps me carry everything, and eventually, we're ready to go inside."
    s "Finally! I'm freezing."



    return
