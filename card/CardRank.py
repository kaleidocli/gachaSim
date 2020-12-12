from enum import Enum



class ECardRank(Enum):
    def __str__(self):
        if self.value == 0:
            return "n/a"
        elif self.value == 1:
            return "common"
        elif self.value == 2:
            return "uncommon"
        elif self.value == 3:
            return "rare"
        elif self.value == 4:
            return "super rare"
        elif self.value == 5:
            return "super super rare"
        elif self.value == 6:
            return "legendary"

    NA = 0
    C = 1
    UC = 2
    R = 3
    SR = 4
    SSR = 5
    L = 6

class CardRank():
    def __init__(self):
        self.CARD_RANK_RATE = {      # Denominator is 1000
            ECardRank.NA: 0,
            ECardRank.C: 489,
            ECardRank.UC: 300,
            ECardRank.R: 150,
            ECardRank.SR: 50,
            ECardRank.SSR: 10,
            ECardRank.L: 1
        }