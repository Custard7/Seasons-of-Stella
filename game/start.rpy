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
    
    p "Hey Stella!"
    
    "I whip around, surprised, upon hearing my name"
    "It's none other than Pucas P. Potato"
    "His long, fluffy blonde hair flows elegantly as he speaks. He's tall, handsome, with a rugged, masculine exterior"
    "The last time I'd talked to Pucas, we'd . . . "
    "Well, let's just say we didn't talk"
    "I'm too nervous to say anything other than-"
    s "Pucas. Hi, um. Congrats!"
    p "Congrats to me? No way, it's all on you! You're the one giving a big speech"
    "He pats me on the back. Is he patronizing me?"
    s "No, not at all. It's not that big of a deal"


    menu:
         "What should I do?"

         "Ask him out.":
            p "No."
            $ pucas_points += 10
         "Ride him like a pony.":
            s "I'm going to ride you like a pony"
            $ pucas_points -= 50
            "That happened."
            "Afterwards, Pucas just kept staring at me. It was kind of strange, sort of mystifying. It was as if his eyes were large black holes."
            "Inside those black holes was the old Pucas."
            "Stuck."
            "Alone."
            pause
            "He never talked again."

    jump pucas
#Don't fuck up my shit Jackson
#Zeke added a comment here!
#More fuckin shit
#Keeth
