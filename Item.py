
class Item: 
    def __init__(self, name="",wgt=0,val=0):
        self.name = ""
        self.wgt = wgt
        self.val = val

### VALUABLES ### 

class Coin(Item):
    def __init__(self, name="Coin",wgt=1,val=10):
        self.name = name
        self.wgt = wgt
        self.val = val
        self.rarity = 0.25
        self.id = 0

class Jewel(Item):
    def __init__(self,name="Jewel",wgt=1,val=50,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.rarity = 0.05
        self.id = 1


### MEDICINE / STIMULANTS ### 

class HealingPotion(Item):
    def __init__(self,name="Potion",wgt=1,val=1,potency=10):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.rarity = 0.15
        self.id = 2
    
### FOOD ###

class Bread(Item):
    def __init__(self,name="Bread",wgt=1,val=1,potency=2):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.rarity = 0.15
        self.id = 3

        
class Apple(Item):
    def __init__(self,name="Apple",wgt=1,val=2,potency=3):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.rarity = 0.10
        self.id = 4


### WEAPONS ###

class Club(Item):
    def __init__(self,name="Club",wgt=1,val=15,modifier=1.3):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.modifier = modifier
        self.rarity = 0.15
        self.id = 5

class BronzeSword(Item):
    def __init__(self,name="BronzeSword",wgt=1,val=20,modifier=1.7):
        self.name = name
        self.wgt = wgt 
        self.val = val         
        self.modifier = modifier
        self.rarity = 0.10
        self.id = 6


class SteelSword(Item):
    def __init__(self,name="SteelSword",wgt=1,val=20,modifier=2.0):
        self.name = name
        self.wgt = wgt 
        self.val = val         
        self.modifier = modifier
        self.rarity = 0.05
        self.id = 7
