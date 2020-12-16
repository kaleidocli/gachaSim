from card.ModelCard import ModelCard
from base.Index import Index



class ModelCardIndex(Index):
    def CardIndexAdd(self, tCardCode: str, tCard: ModelCard):
        """
        Add a card in to the UserCardIndex, with tCardId as key and tCard as value.

        Exceptions
        ----------
        TypeError
                if tCard is not an card.ModelCard
        """
        if not isinstance(tCard, ModelCard): raise TypeError("tCard needs to be a card.ModelCard")
        super().IndexAdd(tCardCode, tCard)

    def CardIndexLookUp(self, tCheckerAndValues: dict):
        """
        Retrieve a list of Codes of cards that satisfied the condition of <tCheckers>.
        Pre-made checkers can be found in this class
        + Raise KeyError if a key (of tValues' dict) required by a checker is not found

        Parameters
        ----------
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

        return super().IndexLookUp(tCheckerAndValues, "mCode")



    # Checkers ================================================

    def CardCheckerName(self, tValue: dict, tCard: ModelCard):
        """
        Check for name
        If tCard is UserCard, convert it to ModelCard beforehand.
        OPTIONS
        ----------
        value : str
                Value that will be used as sample
        mode : list of str
                Either 'f' (search for full string)
                    or 'nf' (search for substring)
        Exceptions
        ----------
        TypeError
                if tCard is not an card.ModelCard
        """
        if not isinstance(tCard, ModelCard): raise TypeError("tCard needs to be a card.ModelCard")
        return super().CheckerString(tValue, tCard.mName)

    def CardCheckerRank(self, tValue: dict, tCard: ModelCard):
        """
        Check for rank
        If tCard is UserCard, convert it to ModelCard beforehand.
        OPTIONS
        ----------
        value : CardRank.CardRank
                Value that will be used as sample (or lower bound)
        value_2 : CardRank.CardRank
                (Only if mode=='r') Second value that will be used as upper bound
        mode : list of str
                Either 's' (search with a single value)
                    or 'r' (search within a range of value. Need another arg <value_2>)
        Exceptions
        ----------
        TypeError
                if tCard is not an card.ModelCard
        """
        if not isinstance(tCard, ModelCard): raise TypeError("tCard needs to be a card.ModelCard")
        return super().CheckerNumber(tValue, tCard.mRank)

    def CardCheckerTag(self, tValue: dict, tCard: ModelCard):
        """
        Check for tag
        If tCard is UserCard, convert it to ModelCard beforehand.
        OPTIONS
        ----------
        value : str, iterable
                Value or values that will be used as sample
        mode : list of str
                Either 'f' (search for full string)
                    or 'nf' (search for substring)
        Exceptions
        ----------
        TypeError
                if tCard is not an card.ModelCard
        """
        if not isinstance(tCard, ModelCard): raise TypeError("tCard needs to be a card.ModelCard")
        return super().CheckerString(tValue, tCard.mTag)

    def CardCheckerValue(self, tValue: dict, tCard: ModelCard):
        """
        Check for value
        If tCard is UserCard, convert it to ModelCard beforehand.
        OPTIONS
        ----------
        value : int
                Value that will be used as sample (or lower bound)
        value_2 : ModelCard
                (Only if mode=='r') Second value that will be used as upper bound
        mode : list of str
                Either 's' (search with a single value)
                    or 'r' (search within a range of value. Need another arg <value_2>)
        Exceptions
        ----------
        TypeError
                if tCard is not an card.ModelCard
        """
        if not isinstance(tCard, ModelCard): raise TypeError("tCard needs to be a card.ModelCard")
        return super().CheckerNumber(tValue, tCard.mValue)
            