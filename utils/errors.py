


class ElementNotInRangeError(Exception):
    """
    ATTRIBUTES
    ----------
    tElementName : str
            String describing the violating element. Not necessarily variable's name.
    tRangeMax : str
            String describing the upper bound.
    tRangeMin : str
            String describing the lower bound.
    tMsg : str
            Custom message, with optional parameters using the parameter's name e.g. "This is {tParamName}!"
    """

    def __init__(self, tElementName: str, tRangeMax: int, tRangeMin: int=0, tMsg: str=""):
        self.mElementName = tElementName
        self.mRangeMin = tRangeMin
        self.mRangeMax = tRangeMax
        if tMsg:
            self.message = tMsg.replace("{{tElementName}}", self.mElementName).replace("{{tRangeMin}}", self.mRangeMin).replace("{{tRangeMax}}", self.mRangeMax)
        else:
            self.message = "{} is not within the required range ({} ~ {})".format(self.mElementName, self.mRangeMin, self.mRangeMax)
        super().__init__(self.message)