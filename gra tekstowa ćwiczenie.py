from enum import Enum
import random

Event = Enum('Event', ['Chest', 'Empty'])
eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
    }
Colours = Enum ('Colours', {'Green': 'zielony',
                            'Orange': 'pomaranczowy',
                            'Purple': 'fiolet',
                            'Gold': "złoty"
                            }
                )

eventList = tuple(eventDictionary.keys())
eventProbalility = tuple(eventDictionary.values())

chestColoursDictionary = {
                            Colours.Green : 0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                        }

chestColourList = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())


rewardsForChest = {
                        chestColourList[reward]: (reward + 1) * ( reward + 1) * 1000
                        for reward in range(len(chestColourList))
                                        }


gameLength = 5
goldAcquired = 0

print("Welcome in my game called KOMNATA")
print("""You have only 5 steps to make,
        see yourself how much gold you gonna acquire till the end!""")

while gameLength > 0:
    gamerAnswer = input("Do you want to move forward?")
    if (gamerAnswer == "yes"):
        print("Great, let's see what you got..")
        drawnEvent = random.choices(eventList,eventProbalility)[0]
        if (drawnEvent == Event.Chest):
            print("You've drawn a CHEST")
            drawnColour = random.choices(chestColourList,chestColourProbability)[0]
            print("The chest color is", drawnColour.value)
            gamerReward = rewardsForChest[drawnColour]
            goldAcquired = goldAcquired + gamerReward
        elif(drawnEvent == Event.Empty):
            print("You've drawn nothing, you are so unlukcy!")
        print(drawnEvent)
    else:
        print("You can go just straight man, nothing else, this game is simple")
        continue

    
    gameLength = gameLength - 1
print("Congratulation, you have acquired: ", goldAcquired)
