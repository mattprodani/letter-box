from rootNode import RootNode
class Node(RootNode):
    efficiency = 0
    isTerminal = False
    def __init__(self, letter, parent):
        self.letter = letter
        self.parent = parent
    def getEfficiency(self):
        return self.efficiency
    def isRoot(self):
        return False
    def getIsTerminal(self):
        return self.isTerminal
    def getLetter(self):
        return self.letter
    def getParent(self):
        return self.parent
    def setEfficiency(self, efficiency):
        self.efficiency = efficiency
    def makeTerminal(self):
        isTerminal = True