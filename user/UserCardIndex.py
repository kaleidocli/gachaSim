from user.UserCard import UserCard
from base.CardIndex import CardIndex



class UserCardIndex(CardIndex):
    def __init__(self):
        super().__init__()
        self.mUserId = ''

    def CardIndexAdd(self, tCardId: str, tCard: UserCard):
        if not isinstance(tCard, UserCard): return False
        super().CardIndexAdd(tCardId, tCard)
        return True

    def CardIndexLookUp(self, tCheckerAndValues: dict):
        """
        Retrieve a list of IDs of cards that satisfied the condition of <tCheckers>.
        Pre-made checkers can be found in CardIndexCheckers.py
        + Raise KeyError if a key (of tValues' dict) required by a checker is not found

        Parameters
        ----------
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

        return super().CardIndexLookUp(tCheckerAndValues, "mId")