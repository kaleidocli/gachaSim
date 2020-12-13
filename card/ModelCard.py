from card.CardRank import ECardRank



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
            self.mCode, self.mName, self.mRank, self.mDescription, self.mImageDir, self.mTag, self.mValue = tPackage
            return

        # Normal init
        self.mCode = ""
        self.mName = ""
        self.mRank = ECardRank.NA
        self.mDescription = ""
        self.mImageDir = ""
        self.mTag = []
        self.mValue = 0
