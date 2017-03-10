class Node:
    def __init__(self):
        self.data = []
        self.wWalkable = True
        self.nodeID = None

    def SetPosition(self, X, Y):
        self.xPosition = int(X)
        self.yPosition = int(Y)

    def SetWalkable(self, walkable):
        self.wWalkable = walkable

    def GetPosition(self):
        return (self.xPosition, self.yPosition)

    def SetParent(self, parentNode):
        self.parent = parentNode

    def CompareTo(self, X, Y):
        selfPosition = str(self.xPosition) + "," + str(self.yPosition)
        comparePosition = str(X) + "," + str(Y)
        if selfPosition == comparePosition:
            if self.wWalkable is True:
                return True
        return False

    def compareTo(self, positionKey):
        selfPosition = (self.xPosition, self.yPosition)
        if selfPosition == positionKey:
            if self.wWalkable is True:
                return True
        return False

    def UpdateNode(self, G, H):
        self.gCost = G
        self.hCost = H

    def DebugNode(self):
        print "POS" + self.GetPosition() + " WALKABLE(" + str(self.wWalkable)

    def print_info(self):
        print "Node: " + str(self.nodeID) + " " + str(self.GetPosition())
