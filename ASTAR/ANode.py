class Node:
    def __init__(self):
        self.data = []
        self.walkable = True
        self.nodeID = None
        self.parent = None    
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
        xDist = abs(self.xPosition - node.GetPosition()[0])
        yDist = abs(self.yPosition - node.GetPosition()[1])
        return xDist + yDist

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
