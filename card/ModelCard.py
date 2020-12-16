from card.CardRank import ECardRank



class ModelCard():
    """
    Parameters
    ----------
    tPackage : tuple
        (code, name, rank, level, description, imageDir, tag, value)
    + code : str
    + name : str
    + rank : card.CardRank.CardRank
    + description : str
    + imageDir : str
    + tag : list
    + value : int
    """

    def __init__(self, tPackage: tuple=()):
        self.mCode = ""
        self.mName = ""
        self.mRank = ECardRank.NA
        self.mDescription = ""
        self.mImageDir = ""
        self.mTag = []
        self.mValue = 0

        if tPackage:
            self.mCode, self.mName, self.mRank, self.mDescription, self.mImageDir, self.mTag, self.mValue = tPackage
            return