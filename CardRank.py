from enum import Enum

class CardRank(Enum):
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