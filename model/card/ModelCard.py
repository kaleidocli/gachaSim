from typing import List, Tuple, Dict

from model.card.CardRank import ECardRank
from model.card.ModelCardImage import ModelCardImage



class ModelCard():
    """
    Parameters
    ----------
    tPackage : tuple
        (code, name, rank, level, description, imageDir, tag, value)
    + code : str
    + name : str
    + rank : card.CardRank.CardRank
    + descriptions : dict<int, str>
    + imageDir : str
    + tag : list
    + value : int
    """

    def __init__(self, tPackage: tuple=()) -> None:
        self.mCode = ""
        self.mName = ""
        self.mRank = ECardRank.NA
        self.mDescriptions = {}
        self.mCardImages: ModelCardImage; self.mCardImages = None
        self.mTag = []
        self.mValue = 0

        if tPackage:
            self.mCode, self.mName, self.mRank, self.mDescription, self.mImageDir, self.mTag, self.mValue = tPackage
            return