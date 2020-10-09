
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
