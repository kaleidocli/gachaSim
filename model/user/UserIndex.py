from typing import List, Tuple, Callable

from base.Index import Index
from model.user.User import User



class UserIndex(Index):
    def IndexAdd(self, tUser: User, tUserId: str='') -> None:
        """
        Add a card in to the UserIndex, with tUserId as key and tUser as value.

        Exceptions
        ----------
        TypeError
                if tUser is not an user.User
        """
        if not isinstance(tUser, User): raise TypeError("tCard needs to be a user.User")
        super().IndexAdd(tUser.mId, tUser)

    def IndexLookUp(self, tCheckerAndValues: List[Tuple[Callable, dict]]) -> List[str]:
        """
        Retrieve a list of IDs of User that satisfied ALL conditions of <tCheckers>.
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

    def UserCheckerName(self, tValue: dict, tUser: User) -> bool:
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

    def UserCheckerLevel(self, tValue: dict, tUser: User) -> bool:
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

    def UserCheckerWins(self, tValue: dict, tUser: User) -> bool:
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

    def UserCheckerLosses(self, tValue: dict, tUser: User) -> bool:
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