


class UserCard():
    gCardIds = []

    def __init__(self, tPackage: tuple=()):
        """
        Parameters
        ----------
        tPackage : tuple
            (id, userId, cardCode, level, bond, userTags, moves, skills)
        """

        if tPackage:
            self.mId, self.mUserId, self.mCode, self.mLevel, self.mBond, self._mUserTags, self.mMoves, self.mSkills = tPackage
            return

        self.mId = ''
        self.mUserId = ''
        self.mCode = ''

        self.mLevel = 0
        self.mBond = 0
        self._mUserTags = []

        self.mMoves = {}
        self.mSkills = []
    
    def GetUserTags(self):
        return self._mUserTags
        
    def SetUserTags(self, tUserTags: list):
        self._mUserTags = tUserTags

    def AddUserTags(self, tUserTag: str):
        """
        Add user's tag. If dupes is found, return False.
        """
        if tUserTag in self._mUserTags: return False
        self._mUserTags.append(tUserTag)

    @property
    def mId(self):
        return self.mId
    
    @mId.setter
    def mId(self, tCardId):
        if int(tCardId) == -1:  # Find best fit in the ID list
            i = 0
            while True:
                if int(tCardId) not in UserCard.gCardIds:
                    tCardId = str(i)
                    break
                i += 1
        UserCard.gCardIds.append(tCardId)

        return tCardId