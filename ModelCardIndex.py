from ModelCard import ModelCard



class ModelCardIndex():
    def __init__(self):
        self.mCardIndex = {}

    def CardIndexAdd(self, tCardId: str, tCard: ModelCard):
        if not isinstance(tCard, ModelCard): return False

        self.mCardIndex[tCardId] = tCard

    def CardIndexGet(self, tCardId: str):
        return self.mCardIndex[tCardId]