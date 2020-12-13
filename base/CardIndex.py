


class CardIndex():
    def __init__(self):
        self.mCardIndex = {}

    def CardIndexAdd(self, tCardKey: str, tCard):
        self.mCardIndex[tCardKey] = tCard

    def CardIndexGet(self, tCardKey: str):
        return self.mCardIndex[tCardKey]

    def CardIndexLookUp(self, tCheckerAndValues: dict, tAttrToRecord: str):
        """
        Retrieve a list of Keys of cards that satisfied the condition of <tCheckers>.
        Pre-made checkers can be found in CardIndexCheckers.py
        + Raise KeyError if a key (of tValues' dict) required by a checker is not found

        Parameters
        ----------
        tAttrToRecord : str
                Name of the attribute to be used as Key. (e.g. CardCode, CardId)

        tCheckerAndValues : dict
                Pairs of <(Checker, i): Values>
                i is an int, solely to allow multiple dupilcated Checkers in dict.

        + Checker : function
                Function that receive 2 args: Values, Card
                Return true if Card satisfied the condition, else false.

        + Values : dict
                Contain the options of its paired Checker.
                See the doc of the Checker for options.
        """

        res = []

        for tCard in self.mCardIndex.values():
            tResCard = self.CardIndexLookUpOne(tCheckerAndValues, tCard)
            if tResCard:
                res.append(getattr(tResCard, tAttrToRecord))
        
        return res

    def CardIndexLookUpOne(self, tCheckerAndValues: dict, tCard):
        """
        Look up for a single Card.
        Return the Card itself, else return False.
        """

        for tChecker in tCheckerAndValues.keys():
            try:
                if tChecker[0](tCheckerAndValues[tChecker[0]], tCard):
                    return tCard
            except KeyError as e:
                # TODO: get some log here later
                raise e
        return False