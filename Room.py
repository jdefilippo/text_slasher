
class Room: 
    def __init__(self,north=None, south=None, east=None, west=None, desc="", inventory=[], occupants=[]): 
        self.north = north 
        self.south = south 
        self.east  = east 
        self.west  = west
        self.desc  = "" 
        self.inventory = inventory
        self.occupants = occupants

    def setDescription(self,desc):
        self.desc = desc
    def getDescription(self):
        return self.desc

    def setNorth(self,north): 
        self.north = north 
    def setSouth(self,south): 
        self.south = south 
    def setEast(self,east):
        self.east = east 
    def setWest(self,west):
        self.west = west

    def setOccupants(self,occupants):
        self.occupants = occupants
    def getOccupants(self):
        return self.occupants

    def setInventory(self,inventory):
        self.inventory = inventory
    def getInventory(self):
        return self.inventory
        
    def getNorth(self):
        return self.north 
    def getSouth(self): 
        return self.south 
    def getEast(self):
        return self.east
    def getWest(self):
        return self.west
    
