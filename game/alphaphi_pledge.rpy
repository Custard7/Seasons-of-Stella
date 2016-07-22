label alphaphi_pledge:
    centered "Thursday"
    show bg quad_busy
    "The days of the week come and go, like fast fading watercoloured blots on a canvas sheet."
    "Every once in a while, I spot a long forgotten contact from Montana."
    "Nimo sits in the front row of my History of Women's Power-lifting Seminar."
    "I pass Tiger in the student life center, on his way to buy a crisp apple-pro-biotic-nutri-shake."
    "Maddie brushes by me in the rooftop-coffeeshop, cool and collected as ever."
    "But now, the fateful day has come."
    "It's time to compete with 50 other freshman girls, to show that I'd be the best pledge for Alpha Phi."
    show bg srat
    "I walk across campus to the gargantuan sorority house."
    "Its massive white pillars evoke images of Southern plantation estates."
    "A sorority girl stands at the entryway, gatekeeeper to this magical kingdom."
    girl "Who do you know here?"
    s "I have this invitation card, I was told to come here."
    girl "all right, head on in."
    show bg aphi_enter
    "All around me, girls mill around, nervously chatting away."
    "I see Stormee walk out above the ornate staircase to address the crowd."
    stormee "Welcome girls!"
    stormee "We're excited to have all you PNMs here today!"
    stormee "All of us actives are ready to find the cream of the social crop for our fall '14 pledge class!"
    stormee "All girls please walk down to the basement and we'll begin stage one of the bid process!"
    "I nervously shuffles down to the cold basement, ready to prove I've got what it takes."
    show bg black
    centered "Stage One"

    show bg basement
    "I line up with the rest of the girls."
    "In front of us, the actives prepare buckets of hot grease."
    stormee "We will ask you a series of questions!"
    stormee "If you answer correctly, you'll move to the next stage of the competition!"
    stormee "If you answer incorrectly, we'll douse you in hot grease."
    stormee "haha!"
    stormee "Each PNM must answer 2 questions correctly!"
    stormee "First up: Maddie!"
    "I had hardly noticed Maddie was here, time to size up my competition."
    stormee "In the context of the passage, the author’s use of the phrase “her light step flying to keep time with his long stride” (line 3) is primarily meant to convey the idea that..."
    "Thank god I had done all that SAT prep."
    m "Ethan and Jamie share a powerful enthusiasm."
    stormee "That's right, great job!"
    stormee "Kennedy, you're up!"
    girl "o-ok."
    stormee "Explain how bureaucratic discretion increases the power of the bureaucracy in the policy making process."
    "Wow, these girls weren't playing around."
    girl "um... so the bureaucracy can choose what laws they want to make which influences policy."
    stormee "The bureaucracy doesn't make laws."
    stormee "I'm sorry, you're not Alpha Phi material."
    stormee "Burn her."
    stormee "haha!"
    "*TTTTSSSSSSSSSSSSSSSS*"
    girl "UUUAAAAGGGGHHH!"
    stormee "Stella Belfort, you're up."
    "I got this."
    stormee "Which pioneering innovator once said 'Tough times don't last, tough people do.'"
    "I think I know this one!"

    menu:
        "Elon Musk":
            s "I believe that was the brilliant Elon Musk."
            stormee "Yeah, great job!"
            jump stage1_continue
        
        "Tiger Mammal":
            s "Did Tiger Mammal say that?"
            stormee "hahaha!"
            stormee "No silly, he goes to school here!"
            stormee "Burn her."
            s "n-n-no, wait!"
            "It was too late, my face is doused in burning hot oil."
            show bg black
            "My vision quickly fades."
            "I wish I had taken Greek Life more seriously."
            "Maybe I'd still be alive."
            centered "You Have Died."
            centered "R.I.P. Stella Belfort"
            centered "She died the way she lived:"
            centered "Like a Calamari."
            jump game_over
        
        "Mark Zuckerberg":
            s "That was definitely Mark Zuckerberg."
            stormee "Mark Zuckerberg!?"
            stormee "You think we'd use a quote from a Harvard man?"
            stormee "Burn her."
            s "n-n-no, wait!"
            "It was too late, my face is doused in burning hot oil."
            show bg black
            "My vision quickly fades."
            "I wish I had taken Greek Life more seriously."
            "Maybe I'd still be alive."
            centered "You Have Died."
            centered "R.I.P. Stella Belfort"
            centered "She died the way she lived:"
            centered "Like a Calamari."
            jump game_over

label stage1_continue:
    "The girls continue answering questions."
    "Maddie and Nimo both make it to the next stage."
    "The less fortunate are rushed to the hospital burn ward."
    "Soon it's time for my second question."
    stormee "All right Stella."
    stormee "If you answer this correctly you advance to stage two."
    stormee "According to the website 'www.totalfratmove.com' name two of the '45 hottest girl names.'"
    "Stormee had served me up a curveball."
    "In all my studying, I'd never read that website."
    "Time for a solid educated guess."
    menu:
        "Stella & Stella":
            stormee "Self-flattery will get you nowhere, Stella Belfort."
            stormee "Burn her."
            s "n-n-no, wait!"
            "It was too late, my face is doused in burning hot oil."
            show bg black
            "My vision quickly fades."
            "I wish I had taken Greek Life more seriously."
            "Maybe I'd still be alive."
            centered "You Have Died."
            centered "R.I.P. Stella Belfort"
            centered "She died the way she lived:"
            centered "Like a Calamari."
            jump game_over

        "Savannah & Courtney":
            stormee "Very good, Stella Belfort."
            stormee "You've clearly done your research on TFM's website."
            stormee "You'll be one of the select few advancing to the next stage of the competition."
            jump stage2

        "Jessie & Jamie":
            stormee "You cleary haven't done your TFM research."
            stormee "Burn her."
            s "n-n-no, wait!"
            "It was too late, my face is doused in burning hot oil."
            show bg black
            "My vision quickly fades."
            "I wish I had taken Greek Life more seriously."
            "Maybe I'd still be alive."
            centered "You Have Died."
            centered "R.I.P. Stella Belfort"
            centered "She died the way she lived:"
            centered "Like a Calamari."
            jump game_over

label stage2:
    "Out of the 50 girls that had come here, only 30 remained."
    stormee "All right PNMs, come out to the pool outside for stage two!"
    show bg black
    centered "Stage Two"
    show bg pool
    stormee "Stage two is a swimming competition."
    stormee "The top 20 times will advance to the final stage."
    "Thank god I had done swimming in high school!"
    stormee "But that's not all."
    stormee "The pool will be filled with..."
    stormee "Guac."
    "A massive dump truck backs up to the edge of the pool, smashing a fence in it's way."
    "*BEEP BEEP BEEP BEEP*"
    "The dump truck unloads, and hundreds of gallons of guac flow into the pool."
    "A rouge chunk of red onion hits me in the cheek."
    stormee "All right girls, suit up!"
    stormee "Stella! You're up first!"
    "I prepare myself for the slimy plunge into the guac pool."
    "The velvety aroma of lime and avocado overwhelms me."
    "I jump in, my skin starts burning."
    "This is some spicy guac."
    "I had to collect myself. I start my breaststroke that I've practiced my whole life."
    "Closing my eyes, I picture I'm back at my hometown YMCA."
    "My family is cheering my on."
    "My coach is encouraging me from the sidelines."
    "In my state of zen, I lap back and forth through the guac."
    "Upon completion, I look up at the large digital scoreboard."
    "2:06! Not bad for swimming through guac."
    "The rest of the girls swim, but none can beat my score."
    "I guess I'm headed to stage three."
    stormee "All right everyone! Head on back to the basement!"
    show bg black
    centered "Stage Three"
    show bg basement
    stormee "Stage Three is a poetry slam."
    stormee "Those who perform the least geedy poems will get a bid to Alpha Phi."
    s "Um, what's a geed?"
    stormee "A God-Dammned-Independent. Somebody not in a sorority or frat."
    stormee "AKA your worst nightmare."
    stormee "Anybody want to go first?"
    s "I was feeling really confident after the guac swim." 
    s "Yeah, I'll go!"
    # menu:
    #    "What should I perform a poem about?"
#
 #       ""



    return 
