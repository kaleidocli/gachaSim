from base.Index import Index
from model.card.ModelCard import ModelCard



class ModelCardIndex(Index):
    def IndexAdd(self, tCardCode: str, tCard: ModelCard):
        """
        Add a card in to the UserCardIndex, with tCardId as key and tCard as value.

        Exceptions
        ----------
        TypeError
                if tCard is not an card.ModelCard
        """
        if not isinstance(tCard, ModelCard): raise TypeError("tCard needs to be a card.ModelCard")
        super().IndexAdd(tCardCode, tCard)

    def IndexLookUp(self, tCheckerAndValues: list):
        """
        Retrieve a list of Codes of cards that satisfied ALL conditions of <tCheckers>.
        Pre-made checkers can be found in this class

        Parameters
        ----------
        tCheckerAndValues : list
                List contains tuples of (Checker, Values)

        + Checker : function
                Function that receive 2 args: Values, Card
                Return true if Card satisfied the evaluation of the function using Values, else false.

        + Values : dict
                Contain the options of its paired Checker.
                See the doc of the Checker for options.

        Exceptions
        ----------
        KeyError
                If a key (of Values' dict) required by a checker is not found
        """

        return super().IndexLookUp(tCheckerAndValues, "mCode")



    # Checkers ================================================

    def ModelCardCheckerName(self, tValue: dict, tCard: ModelCard):
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

    def ModelCardCheckerRank(self, tValue: dict, tCard: ModelCard):
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

    def ModelCardCheckerTag(self, tValue: dict, tCard: ModelCard):
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

    def ModelCardCheckerValue(self, tValue: dict, tCard: ModelCard):
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
            