


class User():
    def __init__(self, package: tuple=()):
        """
        Parameters
        ----------
        tPackage : tuple
            (id, password, name, description, level, wins, losses, cardIndex)
        """

        if package:
            self.mId, self.mPassword, self.mName, self.mDescription, self.mLevel, self.mWins, self.mLosses, self.mCardIndex = package
            return

        self.mId = ''
        self.mPassword = ''
        self.mName = ''
        self.mDescription = ''

        self.mLevel = 0
        self.mWins = 0
        self.mLosses = 0

        self.mCardIndex = ''