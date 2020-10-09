from Item import Coin, Bread, Potion
from Person import Peasant, Bandit, Trader
from Room import *

def getDescription(curPos): 
    print(curPos.getDescription())

def makeMove(curPos): 
    choice = input("Which way to go? (N|E|S|W). To check your inventory, enter I. To quit game, enter Q.  ")
    while((choice  == "N" and curPos.getNorth() == None) or 
          (choice  == "S" and curPos.getSouth() == None) or
          (choice  == "E" and curPos.getEast() == None)  or
          (choice  == "W" and curPos.getWest() == None) or 
          (choice != "N" and choice != "E" and choice != "W" and choice != "S" and choice != "I" and choice != "Q")):

        if ((choice  == "N" and curPos.getNorth() == None) or 
          (choice  == "S" and curPos.getSouth() == None) or
          (choice  == "E" and curPos.getEast() == None)  or
          (choice  == "W" and curPos.getWest() == None)):
            print("You cannot go that way. ")
        if (choice != "N" and choice != "E" and choice != "W" and choice != "S" and choice != "I" and choice != "Q"):
            print("Please select between North (N), South (S), West (W), or East (E). To check your inventory, enter I. To quit game, enter Q.  ")
        choice = input("Which way to go? (N|E|S|W). To check your inventory, enter I. To quit game, enter Q.  ")
    if choice == "N": 
        return curPos.getNorth() 
    elif choice == "S": 
        return curPos.getSouth()
    elif choice == "E":
        return curPos.getEast() 
    elif choice == "W":
        return curPos.getWest()
    elif choice == "I":
        p.printInventory()
        return curPos
    elif choice == "Q":
        print("Exiting game...")
        quit()
    else:
        pass


### Persons
p = Peasant()
p.printStats()

b1 = Bandit()
b2 = Bandit()

t1 = Trader()

### Items 
coin1 = Coin()
coin2 = Coin()
coin3 = Coin()
bread1 = Bread()

potion1 = Potion()

p.addInventory(coin1)
p.addInventory(coin2)
p.addInventory(bread1)
p.addInventory(potion1)


t1.addInventory(bread1)
t1.addInventory(bread1)
t1.addInventory(bread1)
t1.addInventory(bread1)
t1.addInventory(bread1)


### Locations

home = Room()
home.setDescription("Home, a simple cottage with a hearth, a table, and a small bed. Sunlight streams through a small window. To your right lies the door.")

yard = Room()
yard.setDescription('''Your yard is overgrown with weeds. It has not been cultivated for some time. Ahead in the distance, lies the castle of your Lord. Immediately in front of you lies a dirt path.''')

path = Room()

southPath = Room()
southPath.setDescription("The road opens up a little on both sides...")
southPath.setOccupants([b1,t1])

northPath = Room()
northPath.setDescription("It's a cool but mild day. The road stretches on in front of you.")

path.setDescription("You are on the path, do you go north towards the village or south towards the unknown?")

goldPath = Room()
goldPath.setDescription("The path becomes narrow again. The trees around you press in...")

goldPath.setInventory([coin3])

home.setEast(yard)

yard.setEast(path)
yard.setWest(home)

path.setSouth(southPath)
path.setNorth(northPath)

southPath.setNorth(path)

northPath.setSouth(path)

goldPath.setNorth(southPath)




curLoc = home 
while(1): 
    # Fight enemies 
    # Pick up things 
    # Get a description 
    # Make a move
    #print(home.getEast())
    print(curLoc.getDescription())
    p.processEncounters(curLoc)    
    curLoc = makeMove(curLoc)
      
    #getDescription(curLoc)
    #fightEnemies(curLoc)
    #acquireObjects(curLoc)
    
'''
Beer makes you stronger
Beer +10 hp 
Bread +5 hp 

Equipment? 

Combat? 

Start in home 

 __ 
|__| 

'''



