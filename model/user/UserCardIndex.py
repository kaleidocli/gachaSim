from base.Index import Index
from model.user.UserCard import UserCard



class UserCardIndex(Index):
    def IndexAdd(self, tCardId: str, tCard: UserCard):
        """
        Add a card in to the UserCardIndex, with tCardId as key and tCard as value.

        Exceptions
        ----------
        TypeError
                if tCard is not an user.UserCard
        """
        if not isinstance(tCard, UserCard): raise TypeError("tCard needs to be a user.UserCard")
        super().IndexAdd(tCardId, tCard)

    def IndexLookUp(self, tCheckerAndValues: list):
        """
        Retrieve a list of IDs of cards that satisfied ALL conditions of <tCheckers>.
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
        return super().IndexLookUp(tCheckerAndValues, "mId")

    

    # Checkers ===============================================

    def CardCheckerLevel(self, tValue: dict, tCard: UserCard):
        """
        Check for level
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
                if tCard is not an user.UserCard
        """
        if not isinstance(tCard, UserCard): raise TypeError("tCard needs to be a user.UserCard")
        return super().CheckerNumber(tValue, tCard.mLevel)

    def CardCheckerBond(self, tValue: dict, tCard: UserCard):
        """
        Check for bond
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
                if tCard is not an user.UserCard
        """
        return super().CheckerNumber(tValue, tCard.mBond)

    def CardCheckerUserTags(self, tValue: dict, tCard: UserCard):
        """
        Check for user's tag
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
                if tCard is not an user.UserCard
        """
        if not isinstance(tCard, UserCard): raise TypeError("tCard needs to be a user.UserCard")
        return super().CheckerNumber(tValue, tCard.GetUserTags())