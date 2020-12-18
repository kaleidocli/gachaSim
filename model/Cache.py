from typing import List, Tuple, Callable, Union

from model.card.ModelCardIndex import ModelCardIndex
from model.user.UserCardIndex import UserCardIndex
from model.user.UserIndex import UserIndex
from model.card.ModelCard import ModelCard
from model.user.User import User
from model.user.UserCard import UserCard



class Cache():
    def __init__(self) -> None:
        self._mUserIndex: ModelCardIndex; self._mUserCardIndex = None
        self._mModelCardIndex: ModelCardIndex; self._mModelCardIndex = None
        self._mUserCardIndex: UserCardIndex; self._mUserCardIndex = None

    def SetUserIndex(self, tUserIndex) -> None:
        self._mUserIndex = tUserIndex

    def GetUserIndex(self) -> UserIndex:
        return self._mUserIndex

    def SetModelCardIndex(self, tModelCardIndex) -> None:
        self._mModelCardIndex = tModelCardIndex

    def GetModelCardIndex(self) -> ModelCardIndex:
        return self._mModelCardIndex

    def SetUserCardIndex(self, tUserCardIndex) -> None:
        self._mUserCardIndex = tUserCardIndex

    def GetUserCardIndex(self) -> UserCardIndex:
        return self._mUserCardIndex


    def CacheIndexAdd(self, tItem) -> bool:
        """
        Add an item to one of the indexes based on its type
        """
        try:
            self._mModelCardIndex.IndexAdd(tItem)
            return True
        except TypeError: pass
        try:
            self._mUserCardIndex.IndexAdd(tItem)
            return True
        except TypeError: pass
        try:
            self._mUserIndex.IndexAdd(tItem)
            return True
        except TypeError: pass
        return False

    def CacheIndexGet(self, tKey: str) -> Union[UserCard, User, ModelCard]:
        """
        Get the value associated with given key from one of the indexes. Return False if not found
        + Which index to use for looking up is based on the prefix the given key. See "_notes/id_naming_convention.txt"
        """
        if tKey.startswith("u"):
            return self._mUserIndex.IndexGet(tKey)
        elif tKey.startswith("uc"):
            return self._mUserCardIndex.IndexGet(tKey)
        elif tKey.startswith("mc"):
            return self._mModelCardIndex.IndexGet(tKey)
        return False

    def CacheIndexLookUp(self, tCheckerAndValues: List[Tuple[Callable, dict]], tIndexNum: int) -> List[str]:
        """
        Retrieve a list of Keys of items (from one of the indexes) that satisfied ALL conditions of <tCheckers>.
        Pre-made Checkers can be found and should be implemented in children classes
        + Raise KeyError if a key (of tValues' dict) required by a checker is not found

        Parameters
        ----------
        tCheckerAndValues : list
                List contains tuples of (Checker, Values)
        
        tIndexNum : int
                0==ModelCardIndex   1==UserCardIndex    2==UserIndex

        + Checker : function
                Function that receive 2 args: Values, Card
                Return true if Card satisfied the evaluation of the function using Values, else false.

        + Values : dict
                Contain the options of its paired Checker.
                See the doc of the Checker for options.
        """
        if tIndexNum == 0:
            return self._mModelCardIndex.IndexLookUp(tCheckerAndValues)
        elif tIndexNum == 1:
            return self._mUserCardIndex.IndexLookUp(tCheckerAndValues)
        elif tIndexNum == 2:
            return self._mUserIndex.IndexLookUp(tCheckerAndValues)
