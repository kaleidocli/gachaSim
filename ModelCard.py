from CardRank import CardRank



class ModelCard():
    def __init__(self, tPackage: tuple=()):
        """
        Parameters
        ----------
        tPackage : tuple
            (id, name, rank, level, description, imageDir, tag, value)
        """

        # Init with package
        if tPackage:
            self.mId, self.mName, self.mRank, self.mLevel, self.mDescription, self.mImageDir, self.mTag, self.mValue = tPackage
            return

        # Normal init
        self.mId = ""
        self.mName = ""
        self.mRank = CardRank.NA
        self.mLevel = 0
        self.mDescription = ""
        self.mImageDir = ""
        self.mTag = []
        self.mValue = 0
