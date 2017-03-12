from ANode import Node


class Grid(object):
    '''grid'''
    def __init__(self, xBounds, yBounds):
        '''init grid'''
        self.grid = []
        self.nodeCount = 0
        self.diagMovement = 14
        self.regMovement = 10
        self.xIncrementor = 0
        self.yIncrementor = 0
        self.nodeCount = 0
        self.xLimit = xBounds
        self.yLimit = yBounds
        self.data = []
        for x in range(0, int((xBounds * yBounds))):
            newNode = Node()
            newNode.nodeID = x + 1
            self.grid.append(newNode)
            self.nodeCount += 1
        for x in self.grid:
            x.SetPosition(self.xIncrementor, self.yIncrementor)
            self.xIncrementor += 1
            if self.xIncrementor == xBounds:
                self.xIncrementor = 0
                self.yIncrementor += 1

    def GetBounds(self):
        return (self.xLimit, self.yLimit)
    def GetNode(self, ID):
        for node in self.grid:
            if node.nodeID == ID:
                return node
    def GetAdjacentList(self, ID, distance, target):
        adjacentList = []        
        node = self.GetNode(ID)

        diagUpLeft = ((node.xPosition - distance), (node.yPosition - distance))
        diagUpRight = ((node.xPosition + distance), (node.yPosition - distance))
        diagDwnLeft = ((node.xPosition - distance), (node.yPosition + distance))
        diagDwnRight = ((node.xPosition + distance), (node.yPosition + distance))
        adjacentUp = ((node.xPosition), (node.yPosition - distance))
        adjacentDown = ((node.xPosition), (node.yPosition + distance))
        adjacentLeft = ((node.xPosition - distance), (node.yPosition))
        adjacentRight = ((node.xPosition + distance), (node.yPosition))
        
        for x in self.grid:
            if x.compareTo(diagUpLeft) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                adjacentList.append(x)
            if x.compareTo(diagUpRight) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                adjacentList.append(x)
            if x.compareTo(diagDwnLeft) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                adjacentList.append(x)
            if x.compareTo(diagDwnRight) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                adjacentList.append(x)
            if x.compareTo(adjacentUp) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                adjacentList.append(x)
            if x.compareTo(adjacentDown) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                adjacentList.append(x)
            if x.compareTo(adjacentLeft) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                adjacentList.append(x)
            if x.compareTo(adjacentRight) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                adjacentList.append(x)
        return adjacentList

    def GetAdjacentDictionary(self, ID, distance, target):
        adjacentDictionary = {}

        node = self.GetNode(ID)

        diagUpLeft = ((node.xPosition - distance), (node.yPosition - distance))
        diagUpRight = ((node.xPosition + distance), (node.yPosition - distance))
        diagDwnLeft = ((node.xPosition - distance), (node.yPosition + distance))
        diagDwnRight = ((node.xPosition + distance), (node.yPosition + distance))
        adjacentUp = ((node.xPosition), (node.yPosition - distance))
        adjacentDown = ((node.xPosition), (node.yPosition + distance))
        adjacentLeft = ((node.xPosition - distance), (node.yPosition))
        adjacentRight = ((node.xPosition + distance), (node.yPosition))

        for x in self.grid:
            if x.compareTo(diagUpLeft) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                adjacentDictionary["DIAGUPLEFT"] = x
            if x.compareTo(diagUpRight) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                adjacentDictionary["DIAGUPRIGHT"] = x
            if x.compareTo(diagDwnLeft) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                adjacentDictionary["DIAGDWNLEFT"] = x
            if x.compareTo(diagDwnRight) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                adjacentDictionary["DIAGDWNRIGHT"] = x
            if x.compareTo(adjacentUp) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                adjacentDictionary["UP"] = x
            if x.compareTo(adjacentDown) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                adjacentDictionary["DOWN"] = x
            if x.compareTo(adjacentLeft) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                adjacentDictionary["LEFT"] = x
            if x.compareTo(adjacentRight) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                adjacentDictionary["RIGHT"] = x

        return adjacentDictionary
