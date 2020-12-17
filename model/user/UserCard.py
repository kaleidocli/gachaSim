class UserCard():
    gCardIds = []

    def __init__(self, tPackage: tuple=()):
        """
        Parameters
        ----------
        tPackage : tuple
            (id, userId, cardCode, level, bond, userTags, moves, skills)
        + id : str
        + userId : str
        + code : str
        + level : int
        + bond : int
        + userTags : iterable
        + moves : iterable
        + skills : iterable
        """

        self.mId = ''
        self.mUserId = ''
        self.mCode = ''

        self.mLevel = 0
        self.mBond = 0
        self._mUserTags = []

        self.mMoves = {}
        self.mSkills = []

        if tPackage:
            self.mId, self.mUserId, self.mCode, self.mLevel, self.mBond, tUserTags, self.mMoves, self.mSkills = tPackage
            # _mUserTags
            for userTag in tUserTags:
                self.AddUserTag(userTag)
            return
    
    def GetUserTags(self):
        return self._mUserTags
        
    def SetUserTags(self, tUserTags: list):
        self._mUserTags = tUserTags

    def AddUserTag(self, tUserTag: str):
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