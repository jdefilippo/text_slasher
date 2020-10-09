import random 
import numpy as np
from prettytable import PrettyTable

class Person: 
    def __init__(self, name="Van Eycke", hp=1, maxHp=1, strength=0,inventory={}, curWgt=0, maxWgt=0): 
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.strength = strength
        self.inventory = inventory
        self.curWgt    = curWgt
        self.maxWgt    = maxWgt

    def getHp(self):
        return self.hp 
    def setHp(self,hp):
        self.hp = hp

    def setStrength(self,strength):
        self.strength = strength 
    def getStrength(self):
        return self.strength
    
    def addInventory(self,item):
        if self.curWgt + item.wgt > self.maxWgt: 
            print("You cannot pick up the item. Inventory is full. ")
            return
        if item.name in self.inventory: 
            self.inventory[item.name] = [self.inventory[item.name][0]+1,item]
        else:
            self.inventory[item.name] = [1, item] 
        self.curWgt += item.wgt

    def heal(self, potency):
        if self.hp + potency > self.maxHp:
            self.hp = self.maxHp
        else:
            self.hp += potency
        self.printStats()
    
    def removeItem(self,itemName):
        if self.inventory[itemName][0] == 1: 
            del self.inventory[itemName]
        else:
            self.inventory[itemName][0] -= 1

    def printInventory(self):
        if self.inventory == {}:
            print("You have no items on your person. ")
        else: 
            print("Current Inventory:")
            x = PrettyTable()   
            x.field_names = ["Item", "Quantity", "Weight", "Value"]
            for i in self.inventory:
                x.add_row([i,self.inventory[i][0], self.inventory[i][1].wgt, self.inventory[i][1].val])
            print(x)
            choice = input("Do you want to use (U) or drop an item (D)? Otherwise, to quit the dialogue and return to the game, press Q. ")
            while(choice != "U" and choice != "D" and choice != "Q"):
                choice = input("Do you want to use (U) or drop an item (D)? Otherwise, to quit the dialogue and return to the game, press Q. ")
            if choice == "U": 
                itemName = input("Which item would you like to use? Enter the item name. ")
                if itemName in self.inventory and hasattr(self.inventory[itemName][1], 'potency') and self.inventory[itemName][1].potency > 0: 
                    self.heal(self.inventory[itemName][1].potency)     
                    self.removeItem(itemName) 
                else:
                    print("Item cannot be used.")             
            elif choice == "D":
                itemName = input("Which item would you like to drop? Enter the item name. ")
                if itemName in self.inventory: 
                    self.removeItem(itemName)
            else:
                return 

    def printStats(self):
        print("{} has {} remaining hitpoints".format(self.name, self.hp))

class Peasant(Person): 
    def __init__(self,name="Joe", hp=50,maxHp=50,strength=10,inventory={}, maxCarry=3, curWgt=0, maxWgt=10 ):
        self.name   = name 
        self.hp     = hp 
        self.maxHp  = maxHp
        self.strength = strength 
        self.inventory = inventory
        self.maxCarry = maxCarry
        self.curWgt    = curWgt
        self.maxWgt    = maxWgt

    def encounterTrader(self,trader):
        choice = input("Would you like to meet with the Trader? (Y|N)") 
        while(choice != "Y" and choice != "N"):
            choice = input("Would you like to meet with the Trader? (Y|N)") 
        print("The trader wanders off.")



    def fightEnemy(self,enemy):
        print("A ", enemy.name, "approaches you, brandishing a sword.")
        # Determine who takes the first hit. Assume 50% probability.
        firstSwing = random.randint(0,2)
        if firstSwing == 1: 
            heroTurn = True
        else:
            heroTurn = False
        while(enemy.getHp() > 0 and self.getHp() > 0):
            if heroTurn: 
                damage = np.random.rand() * self.getStrength()
                print("You ( hp =", self.getHp(), ") take a swing at the intruder ( hp =", enemy.getHp(), "), exacting", int(damage), "damage.")
                enemy.setHp(int(enemy.getHp() - damage))
                heroTurn = False
            else:
                damage = np.random.rand() * enemy.getStrength()
                print("The intruder ( hp =", enemy.getHp(), ") takes a swing at you ( hp =", self.getHp(), "), exacting", int(damage), "damage.")
                self.setHp(int(self.getHp() - damage))
                heroTurn = True
        if self.getHp() == 0:
            print("You have died. :( ")
            quit()
        else:
            print("You have killed the ", enemy.name)

    def processEncounters(self, curLoc):

        for occupant in curLoc.getOccupants():
            if occupant.name == "Bandit":
                self.fightEnemy(occupant)
            elif occupant.name == "Trader":
                self.encounterTrader(occupant)

        
        # Ensure that you do not see the same people again
        curLoc.setOccupants([])


class Bandit(Person): 
    def __init__(self, name="Bandit", hp=25,strength=7):
        self.name = name 
        self.hp = hp 
        self.strength = strength 


class Trader(Person): 
    def __init__(self, name="Trader", hp=25,strength=7, inventory={}, curWgt=0, maxWgt=10):
        self.name = name 
        self.hp = hp 
        self.strength = strength 
        self.inventory = inventory
        self.curWgt    = curWgt
        self.maxWgt    = maxWgt

    
    
        

