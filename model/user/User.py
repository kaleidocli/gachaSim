from model.user.UserCardIndex import UserCardIndex
from utils.errors import ElementNotInRangeError



class User():
    """
    Parameters
    ----------
    tPackage : tuple
        (id, password, name, description, level, wins, losses, cardIndex)
    + id : str
            Less than 10 character
    + password : str
            Less than 20 character
    + name : str
            Less than 20 character
    + description : str
            Less than 200 character
    + level : int
    + wins : int
    + losses : int
    + cardIndex : base.UserCardIndex.UserCardIndex

    Exceptions
    ----------
    utils.errors.ElementNotInRangeError
            Raised when the length of any attribute goes out of range
    """

    def __init__(self, package: tuple=()) -> None:
        self._ID_MAX_LENGTH = 10
        self._PASSWORD_MAX_LENGTH = 20
        self._NAME_MAX_LENGTH = 20
        self._DESCRIPTION_MAX_LENGTH = 200

        self.mId = ''
        self.mPassword = ''
        self.mName = ''
        self.mDescription = ''

        self.mLevel = 0
        self.mWins = 0
        self.mLosses = 0

        self.mCardIndex: User; self.mCardIndex = None

        if package:
            self.mId, self.mPassword, self.mName, self.mDescription, self.mLevel, self.mWins, self.mLosses, self.mCardIndex = package
            return

    @property
    def mId(self):
        return self.mId

    @mId.setter
    def mId(self, tId):
        if len(tId) > self._ID_MAX_LENGTH:
            raise ElementNotInRangeError("The length of given ID", self._ID_MAX_LENGTH)
        self.mId = tId

    @property
    def mPassword(self):
        return self.mPassword

    @mPassword.setter
    def mPassword(self, tPassword):
        if len(tPassword) > self._PASSWORD_MAX_LENGTH:
            raise ElementNotInRangeError("The length of given password", self._PASSWORD_MAX_LENGTH)
        self.mPassword = tPassword

    @property
    def mName(self):
        return self.mName

    @mName.setter
    def mName(self, tName):
        if len(tName) > self._NAME_MAX_LENGTH:
            raise ElementNotInRangeError("The length of given name", self._NAME_MAX_LENGTH)
        self.mName = tName

    @property
    def mDescription(self):
        return self.mDescription

    @mDescription.setter
    def mDescription(self, tDescription):
        if len(tDescription) > self._DESCRIPTION_MAX_LENGTH:
            raise ElementNotInRangeError("The length of given description", self._DESCRIPTION_MAX_LENGTH)
        self.mDescription = tDescription