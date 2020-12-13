from card.ModelCard import ModelCard
from user.UserCard import UserCard
from card.CardRank import CardRank



# ================================================== ModelCardIndex

def CardCheckerName(tValue: dict, tCard: ModelCard):
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
    """
    return CheckerString(tValue, tCard.mName)

def CardCheckerRank(tValue: dict, tCard: ModelCard):
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
    """
    return CheckerNumber(tValue, tCard.mRank)

def CardCheckerTag(tValue: dict, tCard: ModelCard):
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
    """
    return CheckerString(tValue, tCard.mTag)

def CardCheckerValue(tValue: dict, tCard: ModelCard):
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
    """
    return CheckerNumber(tValue, tCard.mValue)


# ================================================== UserCardIndex
def CardCheckerLevel(tValue: dict, tCard: UserCard):
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
    """
    return CheckerNumber(tValue, tCard.mLevel)

def CardCheckerBond(tValue: dict, tCard: UserCard):
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
    """
    return CheckerNumber(tValue, tCard.mBond)

def CardCheckerUserTags(tValue: dict, tCard: UserCard):
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
    """
    return CheckerNumber(tValue, tCard.GetUserTags())


# ================================================== Tools

def CheckerString(tValue: dict, tCurrentElementBeingCompared: str):
    """
    Check for string/iterable
    OPTIONS
    ----------
    value : str
            Value that will be used as sample
    mode : list of str
            Either 'f' (search for full string)
                or 'nf' (search for substring)
    """
    if 'f' in tValue['mode'] and tValue['value'] == tCurrentElementBeingCompared:
        return True
    elif 'nf' in tValue['mode'] and tValue['value'] in tCurrentElementBeingCompared:
        return True
    return False

def CheckerNumber(tValue: dict, tCurrentElementBeingCompared):
    """
    Check for Number/Enum
    OPTIONS
    ----------
    value : ModelCard
            Value that will be used as sample (or lower bound)
    value_2 : ModelCard
            (Only if mode=='r') Second value that will be used as upper bound
    mode : list of str
            Either 's' (search with a single value)
                or 'r' (search within a range of value. Need another arg <value_2>)
    """
    if 's' in tValue['mode'] and tValue['value'] == tCurrentElementBeingCompared:
        return True
    elif 'r' in tValue['mode'] and tValue['value'] <= tCurrentElementBeingCompared and tValue['value_2'] >= tCurrentElementBeingCompared:
        return True
    return False