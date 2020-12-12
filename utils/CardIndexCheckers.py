from card.ModelCard import ModelCard
from card.CardRank import CardRank



def CardCheckerName(tValue: dict, tCard: ModelCard):
    """
    Check for name
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

def CardCheckerLevel(tValue: dict, tCard: ModelCard):
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

def CardCheckerTag(tValue: dict, tCard: ModelCard):
    """
    Check for tag
    OPTIONS
    ----------
    value : str
            Value that will be used as sample
    mode : list of str
            Either 'f' (search for full string)
                or 'nf' (search for substring)
    """
    return CheckerString(tValue, tCard.mTag)

def CardCheckerValue(tValue: dict, tCard: ModelCard):
    """
    Check for value
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






def CheckerString(tValue: dict, tSample: str):
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
    if 'f' in tValue['mode'] and tValue['value'] == tSample:
        return True
    elif 'nf' in tValue['mode'] and tValue['value'] in tSample:
        return True
    return False

def CheckerNumber(tValue: dict, tSample):
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
    if 's' in tValue['mode'] and tValue['value'] == tSample:
        return True
    elif 'r' in tValue['mode'] and tValue['value'] <= tSample and tValue['value_2'] >= tSample:
        return True
    return False