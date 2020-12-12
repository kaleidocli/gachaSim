from card.ModelCard import ModelCard




class ModelCardIndex():
    def __init__(self):
        self.mCardIndex = {}

    def CardIndexAdd(self, tCardId: str, tCard: ModelCard):
        if not isinstance(tCard, ModelCard): return False

        self.mCardIndex[tCardId] = tCard

    def CardIndexGet(self, tCardId: str):
        return self.mCardIndex[tCardId]

    def CardIndexLookUp(self, tCheckerAndValues: dict):
        """
        Retrieve a list of IDs of cards that satisfied the condition of <tCheckers>.
        Pre-made checkers can be found in CardIndexCheckers.py
        + Raise KeyError if a key (of tValues' dict) required by a checker is not found

        Parameters
        ----------
        tCheckerAndValues: dict
                Pairs of <(Checker, checkerId): Values>
                checkerId is an int, solely to allow multiple dupilcated Checkers in dict.

        + Checker : function
                Function that receive 2 args: Values, Card
                Return true if Card satisfied the condition, else false.

        + Values : dict
                Contain the options of its paired Checker.
                See the doc of the Checker for options.
        """

        res = []

        for tCard in self.mCardIndex.values():
            for tChecker in tCheckerAndValues.keys():
                try:
                    if tChecker[0](tCheckerAndValues[tChecker[0]], tCard):
                        res.append(tCard.mId)
                except KeyError as e:
                    # TODO: get some log here later
                    raise e
        
        return res