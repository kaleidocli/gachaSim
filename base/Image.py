class Image():
    def __init__(self) -> None:
        self.mImageUrl = ""

    @property
    def mImageUrl(self) -> str:
        return self.mImageUrl

    @mImageUrl.setter
    def mImageUrl(self, tUrl: str) -> bool:
        if not tUrl.endswith((".png", ".jpg")):
            return False
        self.mImageUrl = tUrl
        return True

    def IsEqual(self, tValues: dict) -> bool:
        if tValues['url'] == self.mImageUrl:
            return True
        return False