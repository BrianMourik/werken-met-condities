print("*********************************************************************************")
print("War of the worlds tiny text based survival game.")
print("*********************************************************************************")
print("Theres some pretty graphic stuff in this just saying.")
graphic_warning = input("Im ready!")
print("*********************************************************************************")
print("I will have to ask you for your 'stats' before we get started.")
print("You have 10 points to distribute over these 2 stats, dont forget to use them all!")
print("(The 'stats' are luck and intelligence.)")
print("---------------------------------------------------------------------------------")
luck = int(input("How lucky are you?: "))
inteligence = int(input("How smart are you?: "))
print("---------------------------------------------------------------------------------")
stats = int(luck+inteligence)
if (stats > 10):
    print("Meer dan 10 punten gebruikt start opnieuw.")
else:
    print("==========================================================================================================================")
    print("Day 1: the arrival")
    print("==========================================================================================================================")
    print("It was just a regular school day when a glass shattering bang was heard outside.")
    print("You look outside to see what has happened, it seems some kind of capsule has crashed into the riverbed.")
    print("People gather around when movement is heard inside, someone must be trying to escape!")
    print("Students and teatchers try to help but the heat of the capsule holds them back.")
    print("The capsule has been sectioned off by the military withing the hour.")
    print("The rest of the school day is fairly normal.")
    print("As you head home you see that there were multiple attempts at getting inside of the capsule, none of them have succeeded.") 
    day_skip = input("next")
    print("==========================================================================================================================")
    print("Day 2: the beginning")
    print("==========================================================================================================================")
    print("It was another normal morning when someone ran into class screaming: THE CAPSULE IS OPENING!")
    print("You stood infront of the window looking over the crowd, hypnotized by the capsule.")
    print("Thats when the lid fell off with a lowd thud.")
    print("2 disk like eyes emerged from the capsule followed by some slimy, leathery blob.")
    print("People looked on in amazement, some shook, some disgusted.")
    print("You were blinded by a bright flash before you were even able to process what just happened.")
    print("When your vision returned you saw that a line of students had dissapeared, or rather been vaporized.")
    print("A panic ensued as the aliën started to vaporize more and more people.")
    print("So, what are you going to do?")
    start = input("Run / Wait it out: ")
    if (start.lower() == "run"):
        print("You packed your stuff as fast as you could and fled the school via the,")
        if inteligence >= int(8):
            print("Int 8: Maybe its best to take the side exit.")
        door = input("Front exit / Side exit: ")
        if (door.lower() == "front exit"):
            print("As you run through the front exit you get vaporized within seconds... try again.")
        else:
            print("You decide not to follow the horde and grab your bike, After about 20 minutes you arrive at home.")
            print("You panic thinking that this must be a dream, pinching just inflicts pain though.")
            print("Your parents still have not returned from work, so you decide to,")
            leave = input("Stay at home / Get out of here: ")
            if (leave.lower() == "get out of here"):
                print("You take everything you would need to survive a few days, with a full bag you decide to take the,")
                if inteligence >= int(5):
                    print("Int 5: It might be smartest to not take the car.")
                
                lexit = input("Bike / Car / Train: ")
                if (lexit.lower() == "car"):
                    print("You grab the keys off the closet and start the car.")
                    print("Driving really isnt that hard as you thought!")
                    print("Unfortunately your driving skill isnt really that great to survive chaotic driving like this.")
                    print("You die in a head on collision... try again.")

                elif (lexit.lower() == "train"):
                    print("You run to the train station and grab the first train out of here")
                    print("You see a pod falling out of the sky pointed at the tracks!")

                    import random
                    rng = random.randint(1,20)

                    if luck >= int(3):
                        print("The pod flies overhead and hits the tracks beyond the bridge, you get launched as the train goes from 200km/h to 0.")
                        print("You died thanks to impact trauma... try again.")
                        print("Well atleast you were lucky anough to not drown...")

                    elif rng >= 10:
                        print("The pod crashed into the brige infront of you, the train launches itself into the water and you drown... try again.")

                    else:
                        print("The pod flies overhead and hits the tracks beyond the bridge, you get launched as the train goes from 200km/h to 0.")
                        print("You died thanks to impact trauma... try again.")
                
                else:
                    print("You grab your bike and head for,")
                    bus = input("The Bus / The bridge: ")
                    if (bus.lower() == "the bus"):
                        print("You park your bike and step on one of the evacuation busses.")
                        print("After a 1 hour long bus drive to Rotterdam you decide to head to,")
                        boat = input("The first boat out / The nearest military outpost: ")
                        if (boat.lower() == "the first boat out"):
                            print("You walk to the harbor and ask to one of the cargo boats if they could you with them.")
                            print("They let you on the ship and show you your own, broom closet, eh its better than nothing.")
                            print("Congratulations, you have escaped! (lets just hope the rest of the world is safe.)")

                        else:
                            print("You are let into the refugee camp.")
                            print("You start to calm down knowing that this all might just be over...")
                            print("You are awakened the next day by gunshots! The aliëns have arrived here aswell!")
                            print("You are hit by a heatray and instantly vaporized... try again!")
                    
                    else:
                        print("You head to the bridge, the entire bridge is filled with cars but your able to go around them.")
                        print("Out of nowhere a pod crashes into the bridge!")
                        print("You are launched into the air! Luckely theres water below you so you will land safely.")
                        print("You drop into the water as you feel your skin burn and blood boil.")
                        print("You forgot about the heat didnt you?")
                        print("You are boiled alive... try again.")

            else:
                print("You decide to stay at home for now.")
                print("The day passes with more pods falling from the sky.")
                print("luckely none landed too close to your house.")
                print("==========================================================================================================================")
                print("Day 3: dead world")
                print("==========================================================================================================================")
                print("You wake up, the morning is weirdly silent.")
                print("Your parents really should have come home by now... they did not even call you once.")
                print("Atleast the water and power is still working.")
                print("Since your parents still have not arrived home you decide to,")
                parents = input("Stay one more day / Just leave: ")
                if (parents.lower() == "stay one more day"):
                    print("==========================================================================================================================")
                    print("Day 4: a new horizon")
                    print("==========================================================================================================================")
                    print("You wake up the next day, the streets still as silent as yesterday.")
                    print("You hear something outside.")
                    print("As you peak out of the window you see a giant tripod walking through your street!")
                    print("Unfortunately he also saw you.")
                    print("You get vaporized as you try to run... try again.")
                
                else:
                    print("You leave your home, the streets weirdly silent.")
                    print("One sound does catch your attention, hammering...")
                    print("You decide to,")
                    hammering = input("Ignore it / Inspect it: ")
                    if (hammering.lower() == "inspect it"):
                        print("You walk towards where the noise is comming from.")
                        print("As you peak over the crater edge you watch a aliën building some kind of machine.")
                        print("You get vaporized before you are even able to stand up.")
                        print("You are nothing but a few water particles now... try again.")
                    
                    else:
                        print("You walk away from the noise, who knows might aswell have been one of them.")
                        print("You think of what your next move should be.")
                        print("The roads are too filled with cars that it even blocks bikes from getting around.")
                        print("You do know that you cant remain here for too long, so decide to,")
                        store = input("Try starting a train / check the nearby store: ")
                        if (store.lower() == "check the nearby store"):
                            print("As you aproach the store hear a scream.")
                            print("It seems to have come from inside the store: ")
                            print("You decide to,")
                            feast = input("Investigate / Run back home: ")
                            if (feast.lower() == "investigate"):
                                print("As you creep inside you see something in the back.")
                                print("Another scream envelops the store as you creep closer.")
                                print("You are able to look through a slit in the door.")
                                print("You see 3 aliëns feasting on... no, People.")
                                print("They seem to be draining thier blood, while they are still alive!")
                                print("You step back in horror and knock over a broom.")
                                print("The aliëns instantly stop feasting to inspect where that noise came from.")
                                print("You tried to hide but are found and dragged into the backroom.")
                                print("You get strapped to the table and see some kind of tube extending from thier bodies.")
                                print("In one swift movement they pierce your body.")
                                print("You start to feel weak as your blood starts being drained out of you.")
                                print("Everything goes black as the last few liters of blood get sucked out of your body.")
                                print("Your bloodless corpse is thrown to the side... try again.")
                            
                            else:
                                print("You run back home and decide that the world outside is worse than in here.")
                                print("==========================================================================================================================")
                                print("Day 17: final cries")
                                print("==========================================================================================================================")
                                print("2 weeks pass, luckely you had more than enough canned food inside.")
                                print("Same as always the world is wierdly silent, when out of nowhere you head some howl.")
                                print("It was the sound of one of the aliëns")
                                print("But it sounded, weak...")
                                print("You decide for once to investigate.")
                                print("As you walk to the source you hear it cry it one more time when,")
                                print("Its cut short... the silence is now truly deafening.")
                                print("You finally see where it was comming from, 3 tripods.")
                                print("They just stand there, unmoving, as you look closer you see crows circling one of the tripods.")
                                print("There are some red strings hanging out of the cockpit wich the crows are feeding on.")
                                print("The aliëns, they are dead!")
                                print("After everything that humanity tried to defeat them with, they forgot about about thier smallest allies.")
                                print("Bacteriä")
                                print("Congratulations, victory is yours!")
                        
                        else:
                            print("You head to the nearby train station.")
                            print("Only one train remained after all that had happened.")
                            print("Its completely abandoned yet the power still seems to function.")
                            print("Now to just start this baby up.")
                            if luck >= int(8):
                                print("Luck 8, Just mash some buttons")
                            energy = input("Start the train: ")
                            
                            import random
                            rmg = random.randint(1,20)
                            
                            if (energy.lower() == "just mash some buttons"):
                                print("You decide to just slam on some of the buttons.")
                                print("The train jumps to life and drives off.")
                                print("You see that the train has set itself to drive to Germany")
                                print("They do have some serious bunkers there.")
                                print("Congratulations! you survived!")

                            elif rmg <= 10:
                                print("You twist some of the buttons and flip a lever.")
                                print("The train jumps to life and drives off.")
                                print("You see that the train has set itself to drive to Germany")
                                print("They do have some serious bunkers there.")
                                print("Congratulations! you survived!")

                            else:
                                print("You accidentally flip the wrong swich.")
                                print("The horn starts to sound, you quickly turn it off.")
                                print("But when you look back up you see one of the tripods standing above the train.")
                                print("Its foot comes down on the cabin crushing you to death... try again.")

    else:
        print("You decide to wait untill this chaos is over.")
        print("You decide to wait for,")
        wait = input("One day / Thirty minutes: ")
        if (wait.lower() == "thirty minutes"):
            print("You see the military arrive as the chaos ends.")
            print("You retreat further into the building for fear of being hit.")
            print("The sounds of fighting die down after a few minutes.")
            print("You step over some broken glass to get a vieuw of the aftermath.")
            print("You watch in horror as you see that the military has been wiped out.")
            print("You get hit by a heatray before you were even able to step away... try again.")

        else:
            print("You decide to find a comfortable place to wait.")
            print("You hear alot of fighting outside but decide not to take a look.")
            print("You baricade yourself inside of the toilets as you fall asleep.")
            print("==========================================================================================================================")
            print("Day 3: dead city.")
            print("==========================================================================================================================")
            print("You are awakened by hammering comming from outside.")
            print("You peek outside the toilets and see the aliëns working on something.")
            print("You decide this is the best time to,")
            if inteligence == int(10):
                print("Int 10: Run now, observe later.")
            sound = input("Observe / Get out: ")
            if (sound.lower() == "observe"):
                print("You are fascinated by what this creature is doing.")
                print("A tripod appears from behind the school and spots you.")
                print("You run deeper into the school and try to hide in a broom closet.")
                print("Suddenly the door swings open as a metalic claw grabs your leg.")
                print("You get dragged outside of school.")
                print("The claw stops infront of the aliëns and they take a good look at you.")
                print("One of the aliëns yells something and the claw starts to tighten around your waist.")
                print("Your ribcage gets crushed and you die of internal bleeding... try again.")
            
            else:
                print("You skip grabbing your bike and stealthfully sneak away from the school.")
                print("This walk is alot longer than you thought but atleast you escaped.")
                print("The streets are weirdly empty, good less to worry about.")
                print("You finally calm down when you start hearing metalic footsteps.")
                print("Its probably best to,")
                walker = input("Run / Hide: ")
                
                if (walker.lower() == "hide"):
                    print("You quickly duck behind one of the parked cars.")
                    print("You use one of the mirrors too look at whats comming.")
                    print("Its a tripod!")
                    print("You quickly lie down under the car.")
                    print("One of its giant metalic legs lands just barely next to the car.")
                    print("That was a close one.")
                    print("You wait a few minutes untill you crawl out from under the car.")
                    print("You arrive at home where you decide to,")
                    suicide = input("Wait this all out / Commit suicide.")
                        
                    if (suicide.lower() == "commit suicide"):
                        print("Yeah today is as good as any to end it all.")
                        print("Finding a strong beam took a few minutes but eventually you got it all set up.")
                        print("you put the rope around your neck and kick the chair away.")
                        print("Victory???, Atleast you didnt die to the aliëns...")
                        print("jej...")

                    else:
                        print("You close the drapes and search around the house for supplies.")
                        print("This might take a while.")
                        print("==========================================================================================================================")
                        print("Day 17: final cries.")
                        print("==========================================================================================================================")
                        print("Thank god that you had anough canned food to last 2 weeks.")
                        print("You were just reading some books when the silence was broken by a howl.")
                        print("You had heard this howl before. Its from one of the aliëns.")
                        print("But it sounded, weak...")
                        print("As you walk to the source you hear it cry it one more time when,")
                        print("Its cut short... the silence is now truly deafening.")
                        print("You finally see where it was comming from, 3 tripods.")
                        print("They just stand there, unmoving, as you look closer you see crows circling one of the tripods.")
                        print("There are some red strings hanging out of the cockpit wich the crows are feeding on.")
                        print("The aliëns, they are dead!")
                        print("After everything that humanity tried to defeat them with, they forgot about about thier smallest allies.")
                        print("Bacteriä")
                        print("Congratulations, victory is yours!")
                
                elif luck == int(10):
                    print("You start running.")
                    print("Luckely the tripod didnt spot you.")
                    print("You reach home and decide to wait all this out.")
                    print("==========================================================================================================================")
                    print("Day 17: final cries.")
                    print("==========================================================================================================================")
                    print("Thank god that you had anough canned food to last 2 weeks.")
                    print("You were just reading some books when the silence was broken by a howl.")
                    print("You had heard this howl before. Its from one of the aliëns.")
                    print("But it sounded, weak...")
                    print("As you walk to the source you hear it cry it one more time when,")
                    print("Its cut short... the silence is now truly deafening.")
                    print("You finally see where it was comming from, 3 tripods.")
                    print("They just stand there, unmoving, as you look closer you see crows circling one of the tripods.")
                    print("There are some red strings hanging out of the cockpit wich the crows are feeding on.")
                    print("The aliëns, they are dead!")
                    print("After everything that humanity tried to defeat them with, they forgot about about thier smallest allies.")
                    print("Bacteriä")
                    print("Congratulations, victory is yours!")
                
                else:
                    print("You try to run but are quickly spotted by the tripod.")
                    print("Your leg gets grabbed by one of its mechanical claws.")
                    print("Your body is janked to the left at incredible speeds.")
                    print("You get swung against one of the nearby trees and die thanks to impact trauma. try again.")