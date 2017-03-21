class Node:
    def __init__(self):
        self.data = []
        self.walkable = True
        self.nodeID = None
        self.parent = None
        self.xIndex = None
        self.yIndex = None
        self.gCost = 0
        self.hCost = 0
        self.fCost = 0

    def SetPosition(self, X, Y):
        self.xPosition = int(X)
        self.yPosition = int(Y)

    def SetWalkable(self, Walkable):
        self.walkable = Walkable

    def GetPosition(self):
        return (self.xPosition, self.yPosition)

    def GetDistance(self, node):
        xDist = abs(self.xIndex - node.xIndex) * 10
        yDist = abs(self.yIndex - node.yIndex) * 10
        return xDist + yDist
        # needs work
        # base this in the grid
        # needs to be dependant on node position  
        
    def getDist(self, node, size):
        diagUpLeft = (self.xPosition - size, self.yPosition - size)
        diagUpRight = (self.xPosition + size, self.yPosition - size)
        diagDwnLeft = (self.xPosition - size, self.yPosition + size)
        diagDwnRight = (self.xPosition + size, self.yPosition + size)
        adjacentUp = (self.xPosition, self.yPosition - size)
        adjacentDown = (self.xPosition, self.yPosition + size)
        adjacentLeft = (self.xPosition - size, self.yPosition)
        adjacentRight = (self.xPosition + size, self.yPosition)

        if node.compareTo(diagUpLeft) is True:
            return 14
        if node.compareTo(diagUpRight) is True:
            return 14
        if node.compareTo(diagDwnLeft) is True:
            return 14
        if node.compareTo(diagDwnRight) is True:
            return 14
        if node.compareTo(adjacentUp) is True:
            return 10
        if node.compareTo(adjacentDown) is True:
            return 10
        if node.compareTo(adjacentLeft) is True:
            return 10
        if node.compareTo(adjacentRight) is True:
            return 10
        print "ERROR"

    def SetParent(self, parentNode):
        self.parent = parentNode
    
    def compareTo(self, positionKey):
        if self.GetPosition() == positionKey:
            if self.walkable is True:
                return True
        return False

    def UpdateNode(self, G, H):
        self.gCost = G
        self.hCost = H
        self.fCost = self.gCost + self.hCost

    def print_parent(self):
        return self.parent.print_info()

    def print_info(self):
        print "Node: " + str(self.nodeID) + " " + str(self.GetPosition())
