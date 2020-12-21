from __future__ import annotations
from typing import List

from base.Image import Image



class ModelCardExpr():
    """
    A node of an expression, may or may not contain Images.
    If the node is called while empty, 
    
    Attributes
    ----------
    mKeyword : str
            See "ModelCardImage._EXPRESSION_KW"
    mImageDirs : str
            URLs of images
    mParent : ModelCardExpr
            Parent node. Set to None if current node is head.
    mChildren : dict<str, ModelCardExpr>
            Dict of pairs <exprKeyword, ModelCardExpr>
    _mPriorityValue : int
            Priority value
    mBestChild : ModelCardExpr
            Non-empty child with lowest _mPriorityValue. Updated this object's parent if it goes from empty to non-empty.
    """
    def __init__(self, tKeyword: str, tPriorityValue: int) -> None:
        self.mKeyword = tKeyword
        self._mImages: List[Image]; self._mImages = []

        self.mParent: ModelCardExpr; self.mParent = None
        self.mChildren = {}
        self.mBestChild: ModelCardExpr; self.mBestChild = None
        self._mPriorityValue = tPriorityValue

    def GetPriorityValue(self):
        return self._mPriorityValue

    def SetPriorityValue(self, tValue):
        self._mPriorityValue = tValue
        self.UpdateBestChild()

    def GetImages(self) -> List[Image]:
        return self._mImages

    def AddImage(self, tImage: Image) -> None:
        """
        Insert an Image. Updated this object's parent's best child if it goes from empty to non-empty.
        """
        self._mImages.append(tImage)
        if len(self._mImages) == 1:
            self.UpdateBestChild()

    def RemoveImage(self, tValues: dict) -> bool:
        """
        Removed an image, equally evaluated by tValues
        
        PARAMETERS
        ----------
        tValues : dict
                <"url": str>
        """
        tRemoveds = []
        for tImage in self._mImages:
            if tImage.IsEqual(tValues):
                tRemoveds.append(tImage)
        if not tRemoveds: return False
        for tImage in tRemoveds:
            self._mImages.remove(tImage)

    def IsEmpty(self) -> bool:
        if self._mImages:
            return True
        return False

    def GetBestChild(self) -> ModelCardExpr:
        return self.mBestChild

    def UpdateBestChild(self) -> None:
        if self.mBestChild:
            tBestChild = self.mBestChild
        else:
            tBestChild = None
        for tChild in self.mChildren.values():
            if ((not tBestChild) or (tChild._mPriorityValue < tBestChild._mPriorityValue)) and tChild.mImageDirs:
                tBestChild = tChild
        self.mBestChild = tBestChild

class ModelCardImage():
    """
    Hold a collection of Images, categorized into image types (full, half, face, CG) and expressions.
    Allow image lookup to find a resembling image to the one not found.
    """
    _EXPRESSION_HIERARCHY = {
        "NEUTRAL": "HEAD",
        "SAD": "HEAD",
        "SMILE": "HEAD",
        "ANNOYED": "HEAD",
        "BLUSH": "SMILE",
        "SMUG": "SMILE",
        "HAPPY": "SMILE",
        "ANGRY": "ANNOYED",
        "CONTEMPTOUS": "ANNOYED",
        "WORRIED": "SAD",
        "CRYING": "SAD"
    }
    _EXPRESSION_DEFAULT_PRIORITY_VALUES = {
        "HEAD": 0,
        "NEUTRAL": 1,
        "SMILE": 2,
        "ANNOYED": 3,
        "SAD": 4,
        "HAPPY": 1,
        "SMUG": 2,
        "BLUSH": 3,
        "ANGRY": 1,
        "CONTEMPTOUS": 2,
        "WORRIED": 1,
        "CRYING": 2
    }
    _IMAGE_TYPE_KW = ["full", "half", "face", "cg"]

    def __init__(self, tExprPriorityValues: dict=None) -> None:
        if tExprPriorityValues:
            self._mExprPriorityValues = tExprPriorityValues
        else:
            self._mExprPriorityValues = {}
        self._mFull = {}; self._InitExprTree("full")
        self._mHalf = {}; self._InitExprTree("half")
        self._mFace = {}; self._InitExprTree("face")
        self._mCg = {}; self._InitExprTree("cg")

    def SetExprPriorityValues(self, tExprPriorityValues: dict) -> None:
        """
        Set _mExprPriorityValues and update the trees
        """
        self._mExprPriorityValues = tExprPriorityValues
        self._UpdateExprPriorityValues()
    
    def GetImages(self, tType: str, tExprKw: str) -> List[Image]:
        """
        Get a list of Image based on given type (tree) and expression.
        If expression is empty, search for the best sibling.
        If best sibling is also empty, recurse the same process with its parents until reach Head node.

        PARAMETERS
        ----------
        tType : str
                Type of image. See: _IMAGE_TYPE_KW
        tExpr : str
                Expression keyword. See: _EXPRESSION_HIERARCHY.keys()
        
        EXCEPTIONS
        ----------
        KeyError:
                tExprKw not found
        """
        
        tExpr = self._ExpTreeGet(tType, tExprKw)
        # C#1: Expr good
        if not tExpr.IsEmpty():
            return tExpr.GetImages()
        # C#2: Expr empty -> Best sibling
        else:
            tExprSibling = self._ExpTreeGet(tType, tExpr.mParent.mKeyword)
            if not tExprSibling.IsEmpty():
                return tExprSibling.GetImages()
            # C#3: Sibling empty -> Recurse in parent
            elif tExpr.mParent:
                return self.GetImages(tType, tExpr.mParent.mKeyword)
            # C#4: Head node // The rest
            return False

    def AddImage(self, tType: str, tExprKw: str, tImage: ModelCardImage) -> None:
        """
        Add an Image based on given type (tree) and expression.

        PARAMETERS
        ----------
        tType : str
                Type of image. See: _IMAGE_TYPE_KW
        tExpr : str
                Expression keyword. See: _EXPRESSION_HIERARCHY.keys()
        
        EXCEPTIONS
        ----------
        KeyError:
                tExprKw not found
        """
        self._ExpTreeGet(tType, tExprKw).AddImage(tImage)

    def _UpdateExprPriorityValues(self) -> None:
        """
        Update ModelCardImage's trees' priority values, based on "_mExprPriorityValues". 
        Can be used for resetting priority values, or add new attributes to the dict.
        
        Exceptions
        ----------
        AttributeError:
                If one of the trees are empty
        """
        if self._mExprPriorityValues:
            for tKeyword, tValue in self._mExprPriorityValues.items():
                self._mFull[tKeyword].SetPriorityValue(tValue)
                self._mHalf[tKeyword].SetPriorityValue(tValue)
                self._mFace[tKeyword].SetPriorityValue(tValue)
                self._mCg[tKeyword].SetPriorityValue(tValue)
        else:
            for tKeyword, tValue in ModelCardImage._EXPRESSION_DEFAULT_PRIORITY_VALUES.items():
                self._mFull[tKeyword].SetPriorityValue(tValue)
                self._mHalf[tKeyword].SetPriorityValue(tValue)
                self._mFace[tKeyword].SetPriorityValue(tValue)
                self._mCg[tKeyword].SetPriorityValue(tValue)

    def _InitExprTree(self, tType : str) -> None:
        """
        Construct a tree with no dirs, priority value based on "_mExprPriorityValues", or the default one.
        """
        tRes = {}
        for tKeyword in ModelCardImage._EXPRESSION_HIERARCHY.keys():
            if self._mExprPriorityValues:
                self._ExprTreeGrow(ModelCardExpr(tKeyword, self._mExprPriorityValues[tKeyword]), tType)
            else:
                self._ExprTreeGrow(ModelCardExpr(tKeyword, ModelCardImage._EXPRESSION_DEFAULT_PRIORITY_VALUES[tKeyword]), tType)
        return tRes

    def _ExprTreeGrow(self, tNode: ModelCardExpr, tType : str) -> None:
        """
        Add the node and its parents, grandparents, etc.
        """
        # Checking dupes
        try:
            if self._ExpTreeGet(tType, tNode.mKeyword):
                return
        except KeyError: pass

        # Init the nodes and connect it with its parents. Create the parents if not available
        try:
            tParentKw = ModelCardImage._EXPRESSION_HIERARCHY[tNode.mKeyword]
            # Parent available
            try:
                tNode.mParent = self._ExpTreeGet(tType, tParentKw)      # Bind child to parent
            # Parent un-available
            except KeyError:
                # Create parent
                if self._mExprPriorityValues:
                    self._ExprTreeGrow(ModelCardExpr(tParentKw, self._mExprPriorityValues[tParentKw]), tType)
                else:
                    self._ExprTreeGrow(ModelCardExpr(tParentKw, ModelCardImage._EXPRESSION_DEFAULT_PRIORITY_VALUES[tParentKw]), tType)
                tNode.mParent = self._ExpTreeGet(tType, tParentKw)      # Bind child to parent
            tNode.mParent.mChildren[tNode.mKeyword] = tNode     # Bind parent to child
        # Head
        except KeyError:
            pass
        self._ExprTreeAdd(tType, tNode)

    def _ExpTreeGet(self, tType: str, tExprKw: str) -> ModelCardExpr:
        """
        Return a ModelCardExpr node on the chosen tree
        Exceptions
        ----------
        KeyError:
                If tExprKw not found
        """
        if tType == "full":
            return self._mFull[tExprKw]
        elif tType == "half":
            return self._mHalf[tExprKw]
        elif tType == "face":
            return self._mFace[tExprKw]
        elif tType == "cg":
            return self._mCg[tExprKw]

    def _ExprTreeAdd(self, tType: str, tExpr: ModelCardExpr) -> bool:
        """
        Add a ModelCardExpr into the given tree and expression
        """
        if tType == "full":
            self._mFull[tExpr.mKeyword] = tExpr
            return True
        elif tType == "half":
            self._mHalf[tExpr.mKeyword] = tExpr
            return True
        elif tType == "face":
            self._mFace[tExpr.mKeyword] = tExpr
            return True
        elif tType == "cg":
            self._mCg[tExpr.mKeyword] = tExpr
            return True
        return False