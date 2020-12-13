from card.ModelCard import ModelCard
from base.CardIndex import CardIndex



class ModelCardIndex(CardIndex):
    def CardIndexAdd(self, tCardCode: str, tCard: ModelCard):
        if not isinstance(tCard, ModelCard): return False
        super().CardIndexAdd(tCardCode, tCard)
        return True

    def CardIndexLookUp(self, tCheckerAndValues: dict):
        """
        Retrieve a list of Codes of cards that satisfied the condition of <tCheckers>.
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

        return super().CardIndexLookUp(tCheckerAndValues, "mCode")