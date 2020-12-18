class Index():
    def __init__(self):
        self._mDict = {}

    def IndexAdd(self, tKey: str, tItem):
        self._mDict[tKey] = tItem

    def IndexGet(self, tKey: str):
        return self._mDict[tKey]

    def IndexLookUp(self, tCheckerAndValues: list, tAttrToRecord: str):
        """
        Retrieve a list of Keys of items that satisfied ALL conditions of <tCheckers>.
        Pre-made checkers can be found and should be implemented in children classes
        + Raise KeyError if a key (of tValues' dict) required by a checker is not found

        Parameters
        ----------
        tAttrToRecord : str
                Name of the attribute to be used as Key. (e.g. CardCode, CardId)

        tCheckerAndValues : list
                List contains tuples of (Checker, Values)

        + Checker : function
                Function that receive 2 args: Values, Card
                Return true if Card satisfied the evaluation of the function using Values, else false.

        + Values : dict
                Contain the options of its paired Checker.
                See the doc of the Checker for options.
        """

        res = []

        for tItem in self._mDict.values():
            tResItem = self.CheckerEval(tCheckerAndValues, tItem)
            if tResItem:
                res.append(getattr(tResItem, tAttrToRecord))
        
        return res

    def CheckerEval(self, tCheckerAndValues: list, tItem):
        """
        Evaluate ALL checkers on a single item.
        Return the Card itself, else return False.
        """

        for tChecker, tValue in tCheckerAndValues:
            try:
                if not tChecker(tValue, tItem):
                    return False
            except KeyError as e:
                # TODO: get some log here later
                raise e
        return tItem



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