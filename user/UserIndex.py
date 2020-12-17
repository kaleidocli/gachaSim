from user.User import User
from base.Index import Index



class UserIndex(Index):
    def IndexAdd(self, tUserId: str, tUser: User):
        """
        Add a card in to the UserIndex, with tUserId as key and tUser as value.

        Exceptions
        ----------
        TypeError
                if tUser is not an user.User
        """
        if not isinstance(tUser, User): raise TypeError("tCard needs to be a user.User")
        super().IndexAdd(tUserId, tUser)

    def IndexLookUp(self, tCheckerAndValues: dict):
        """
        Retrieve a list of IDs of User that satisfied the condition of <tCheckers>.
        Pre-made checkers can be found in this class

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

        Exceptions
        ----------
        KeyError
                If a key (of Values' dict) required by a checker is not found
        """

        return super().IndexLookUp(tCheckerAndValues, "mId")



    # Checkers ===============================================

    def UserCheckerName(self, tValue: dict, tUser: User):
        """
        Check for name
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
                if tUser is not an user.User
        """
        if not isinstance(tUser, User): raise TypeError("tUser needs to be a user.User")
        return super().CheckerString(tValue, tUser.mName)

    def UserCheckerLevel(self, tValue: dict, tUser: User):
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
                if tUser is not an user.UserCard
        """
        if not isinstance(tUser, User): raise TypeError("tUser needs to be a user.User")
        return super().CheckerNumber(tValue, tUser.mLevel)

    def UserCheckerWins(self, tValue: dict, tUser: User):
        """
        Check for number of wins
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
                if tUser is not an user.UserCard
        """
        if not isinstance(tUser, User): raise TypeError("tUser needs to be a user.User")
        return super().CheckerNumber(tValue, tUser.mWins)

    def UserCheckerLosses(self, tValue: dict, tUser: User):
        """
        Check for number of losses
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
                if tUser is not an user.UserCard
        """
        if not isinstance(tUser, User): raise TypeError("tUser needs to be a user.User")
        return super().CheckerNumber(tValue, tUser.mLosses)