


class Index():
    def __init__(self):
        self._mDict = {}

    def IndexAdd(self, tCardKey: str, tCard):
        self._mDict[tCardKey] = tCard

    def IndexGet(self, tCardKey: str):
        return self._mDict[tCardKey]

    def IndexLookUp(self, tCheckerAndValues: dict, tAttrToRecord: str):
        """
        Retrieve a list of Keys of cards that satisfied the condition of <tCheckers>.
        Pre-made checkers can be found and should be implemented in children classes
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
                Return true if Card satisfied the evaluation of the function using Values, else false.

        + Values : dict
                Contain the options of its paired Checker.
                See the doc of the Checker for options.
        """

        res = []

        for tCard in self._mDict.values():
            tResCard = self.IndexLookUpOne(tCheckerAndValues, tCard)
            if tResCard:
                res.append(getattr(tResCard, tAttrToRecord))
        
        return res

    def IndexLookUpOne(self, tCheckerAndValues: dict, tCard):
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



    # ============================================== Base checker

    def CheckerString(self, tValue: dict, tCurrentElementBeingCompared: str):
        """
        Check for string/iterable
        OPTIONS
        ----------
        value : str
                Value that will be used as sample
        mode : list of str
                Either 'f' (search for full string)
                    or 'nf' (search for substring)
        """
        if 'f' in tValue['mode'] and tValue['value'] == tCurrentElementBeingCompared:
            return True
        elif 'nf' in tValue['mode'] and tValue['value'] in tCurrentElementBeingCompared:
            return True
        return False

    def CheckerNumber(self, tValue: dict, tCurrentElementBeingCompared):
        """
        Check for Number/Enum
        OPTIONS
        ----------
        value : ModelCard
                Value that will be used as sample (or lower bound)
        value_2 : ModelCard
                (Only if mode=='r') Second value that will be used as upper bound
        mode : list of str
                Either 's' (search with a single value)
                    or 'r' (search within a range of value. Need another arg <value_2>)
        """
        if 's' in tValue['mode'] and tValue['value'] == tCurrentElementBeingCompared:
            return True
        elif 'r' in tValue['mode'] and tValue['value'] <= tCurrentElementBeingCompared and tValue['value_2'] >= tCurrentElementBeingCompared:
            return True
        return False