
class Item: 
    def __init__(self, name="",wgt=0,val=0):
        self.name = ""
        self.wgt = wgt
        self.val = val

class Coin(Item):
    def __init__(self, name="Coin",wgt=1,val=10):
        self.name = name
        self.wgt = wgt
        self.val = val

class Bread(Item):
    def __init__(self,name="Bread",wgt=1,val=1,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency

class Potion(Item):
    def __init__(self,name="Potion",wgt=1,val=1,potency=10):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
    
class Jewel(Item):
    def __init__(self,name="Jewel",wgt=1,val=100,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency

class Club(Item):
    def __init__(self,name="Club",wgt=1,val=15,modifier=1.3):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.modifier = modifier

class BronzeSword(Item):
    def __init__(self,name="BronzeSword",wgt=1,val=20,modifier=1.7):
        self.name = name
        self.wgt = wgt 
        self.val = val         
        self.modifier = modifier