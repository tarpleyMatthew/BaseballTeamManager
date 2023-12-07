##player class

from dataclasses import dataclass

@dataclass
class Player:
    batOrder: int
    firstName: str
    lastName: str
    position: str
    atBats: int
    hits: int
    playerID: int = None

    #methods
    def getFullName(self):
        return self.firstName + ', ' + self.lastName
    
    def getAverage(self):
        return format(float(self.hits) / float(self.atBats), '.3f' )
