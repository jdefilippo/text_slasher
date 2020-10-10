from Item import *
from Person import *
from Room import *

import random
import numpy as np


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


p = Peasant()
p.addInventory(Club())

'''activeMap = [[1,1,0,0,0,0,0,0],
             [1,1,0,1,0,1,1,0],
             [0,0,0,1,0,1,0,0],
             [0,1,1,0,0,1,0,1],
             [0,1,1,0,1,1,0,1],
             [0,1,1,0,1,1,0,1],
             [0,1,1,0,1,1,0,1],
             [0,0,0,0,0,0,0,1]]'''

activeMap = [[1,1,0,0,0,1,1,1],
             [1,1,0,1,0,1,1,1],
             [0,0,0,1,0,1,1,1],
             [0,1,1,0,0,1,1,1],
             [0,1,1,0,1,1,1,1],
             [0,1,1,0,1,1,1,1],
             [0,1,1,0,1,1,1,1],
             [0,0,0,0,0,1,1,1]]

originX = 5
originY = 0

roomMap = [[Room() for i in range(0,len(activeMap),1)] for j in range(0,len(activeMap[0]),1)] 

for i in range(0,len(activeMap),1):
    for j in range(0,len(activeMap[0]),1):
        if activeMap[i][j] == 0:
            roomMap[i][j].blocked = False

for i in range(0,len(activeMap),1):
    for j in range(0,len(activeMap[0]),1):
        if(i-1 >= 0 and not roomMap[i-1][j].blocked):
             roomMap[i][j].north = roomMap[i-1][j]
        if(i+1 < len(activeMap) and not roomMap[i+1][j].blocked):
             roomMap[i][j].south = roomMap[i+1][j]    
        if(j-1 >= 0 and not roomMap[i][j-1].blocked):
             roomMap[i][j].west = roomMap[i][j-1]
        if(j+1 < len(activeMap) and not roomMap[i][j+1].blocked):
             roomMap[i][j].east = roomMap[i][j+1]    

universe = [Coin(),Bread(),Jewel(),Apple(),HealingPotion(),Club(),BronzeSword(),SteelSword()]
totalProb = 0.0

for item in universe: 
    totalProb += item.rarity

if totalProb != 1.0:
    print("ERROR: Total probabilities are not correct")
    quit()

chanceOneItem = 0.25
chanceTwoItem = 0.125

chanceOneEnemy = 0.10
chanceTwoEnemy = 0.05

chanceTrader = 0.05

def populateItems(curLoc):
    if random.random() <= chanceOneItem:
        itemIdx1 = np.random.choice(len(universe), None, p=[item.rarity for item in universe])
        if random.random() <= chanceTwoItem:
            itemIdx2 = np.random.choice(len(universe), None, p=[item.rarity for item in universe])
            curLoc.setInventory([universe[itemIdx1], universe[itemIdx2]])
        else:
            curLoc.setInventory([universe[itemIdx1]])

def populateEnemies(curLoc):
    if random.random() <= chanceOneEnemy:
        if random.random() <= chanceTwoEnemy:  
            curLoc.setOccupants([Bandit()])
        else:
            curLoc.setOccupants([Bandit(),Bandit()])    

def populateTraders(curLoc):
    if random.random() <= chanceTrader and curLoc.occupants == []:
        newTrader = Trader()

        itemIdx1 = np.random.choice(len(universe), None, p=[item.rarity for item in universe])
        itemQt1  = random.randint(1,3)
        for i in range(itemQt1):
            newTrader.addInventory(universe[itemIdx1])

        itemIdx2 = np.random.choice(len(universe), None, p=[item.rarity for item in universe])
        itemQt2  = random.randint(1,3)
        for i in range(itemQt2):
            newTrader.addInventory(universe[itemIdx2])

        itemIdx3 = np.random.choice(len(universe), None, p=[item.rarity for item in universe])
        itemQt3  = random.randint(1,3)
        for i in range(itemQt3):
            newTrader.addInventory(universe[itemIdx3])



        curLoc.setOccupants([newTrader])

for i in range(0,len(roomMap),1):
    for j in range(0,len(roomMap[0]),1):
        if not roomMap[i][j].blocked and (i != originX and j != originY):
            populateItems(roomMap[i][j])
            populateEnemies(roomMap[i][j])
            populateTraders(roomMap[i][j])



# Column 1 
roomMap[2][0].setDescription("A rock face stares in your direction while the path veers to the right...")
roomMap[3][0].setDescription("The road opens up and you notice a marsh which lies to your left and right.")
roomMap[4][0].setDescription("The path grows narrower but continues in the same direction as before.")
roomMap[originX][originY].setDescription("You find yourself on a dirt path in the woods, facing towards the north.")
roomMap[6][0].setDescription("The path stretches on, but you can see a clearing in front of you.")
roomMap[7][0].setDescription("The road is blocked with heavy forest in front of you and the path curves to the left.")

roomMap[2][1].setDescription("The path narrows and a turn is imminent.")
roomMap[7][1].setDescription("The road stretches on into the distance.")

roomMap[0][2].setDescription("The path veers off to the right.")
roomMap[1][2].setDescription("Trees encroach up ahead.")
roomMap[2][2].setDescription("The path takes a sharp turn to the left.")
roomMap[7][2].setDescription("The path begins to open up for you to your left and in front of you.")

roomMap[0][3].setDescription("The path continues to the right.")
roomMap[3][3].setDescription("The path veers off to the right...")
roomMap[4][3].setDescription("The path continues ahead...")
roomMap[5][3].setDescription("The path continues ahead...")
roomMap[6][3].setDescription("The path continues ahead...")
roomMap[7][3].setDescription("The path continues to the left and straight ahead")

roomMap[0][4].setDescription("Fork in the road. Continue in the current direction or turn to the right.")
roomMap[1][4].setDescription("The tower appears in the distance...")
roomMap[2][4].setDescription("The path continues..you are approaching the tower.")
roomMap[3][4].setDescription("You begin climbing the steps to the tower...up and away you go...")
roomMap[7][4].setDescription("The path contniues to the right...")

roomMap[0][5].setDescription("")
roomMap[7][5].setDescription("")

roomMap[0][6].setDescription("")
roomMap[2][6].setDescription("")
roomMap[3][6].setDescription("")
roomMap[4][6].setDescription("")
roomMap[5][6].setDescription("")
roomMap[6][6].setDescription("")
roomMap[7][6].setDescription("")

roomMap[0][7].setDescription("")
roomMap[1][7].setDescription("")
roomMap[2][7].setDescription("")

curLoc = roomMap[5][0] 
prevLoc = None
while(1): 
    # Fight enemies 
    # Pick up things 
    # Get a description 
    # Make a move
    if(prevLoc != curLoc):
       print(curLoc.getDescription())
    p.processEncounters(curLoc)
    p.gatherResources(curLoc)

    prevLoc = curLoc
    curLoc = makeMove(curLoc)
    




