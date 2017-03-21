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
            x.xIndex = self.xIncrementor
            x.yIndex = self.yIncrementor
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

    def Retrace(self, start, end):
        retraced = []
        currentNode = end         
        while currentNode.parent is not None:
            retraced.append(currentNode)
            currentNode = currentNode.parent
        return retraced

    def GetAdjacentList(self, ID, distance, target):
        adjacentList = []
        adjacents = []        
        node = self.GetNode(ID)

        a_adjacentRight = (node.xPosition + distance, node.yPosition)
        b_diagUpRight = (node.xPosition + distance, node.yPosition - distance)
        c_adjacentUp = (node.xPosition, node.yPosition - distance)
        d_diagUpLeft = (node.xPosition - distance, node.yPosition - distance)
        e_adjacentLeft = (node.xPosition - distance, node.yPosition)
        f_diagDwnLeft = (node.xPosition - distance, node.yPosition + distance)
        g_adjacentDown = (node.xPosition, node.yPosition + distance)
        h_diagDwnRight = (node.xPosition + distance, node.yPosition + distance)
        
        for x in self.grid:
            if x.compareTo(d_diagUpLeft) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("d", x))
                # adjacentList.append(x)
            if x.compareTo(b_diagUpRight) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("b", x))
                # adjacentList.append(x)
            if x.compareTo(f_diagDwnLeft) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("f", x))
                # adjacentList.append(x)
            if x.compareTo(h_diagDwnRight) is True:
                x.UpdateNode(self.diagMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("h", x))
                # adjacentList.append(x)
            if x.compareTo(c_adjacentUp) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("c", x))
                # adjacentList.append(x)
            if x.compareTo(g_adjacentDown) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("g", x))
                # adjacentList.append(x)
            if x.compareTo(e_adjacentLeft) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("e", x))
                # adjacentList.append(x)
            if x.compareTo(a_adjacentRight) is True:
                x.UpdateNode(self.regMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("a", x))
                # adjacentList.append(x)

        # for node in adjacentDict:
        adjacents.sort(key=lambda x: x[0])
        for node in adjacents:
            adjacentList.append(node[1])
        
        return adjacentList
   
    def drawAdjacents(self, ID, distance):        
        adjacentList = []
        adjacents = []        
        node = self.GetNode(ID)

        a_adjacentRight = (node.xPosition + distance, node.yPosition)
        b_diagUpRight = (node.xPosition + distance, node.yPosition - distance)
        c_adjacentUp = (node.xPosition, node.yPosition - distance)
        d_diagUpLeft = (node.xPosition - distance, node.yPosition - distance)
        e_adjacentLeft = (node.xPosition - distance, node.yPosition)
        f_diagDwnLeft = (node.xPosition - distance, node.yPosition + distance)
        g_adjacentDown = (node.xPosition, node.yPosition + distance)
        h_diagDwnRight = (node.xPosition + distance, node.yPosition + distance)
        
        for x in self.grid:
            if x.compareTo(d_diagUpLeft) is True:
                #x.UpdateNode(self.diagMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("d", x))
                # adjacentList.append(x)
            if x.compareTo(b_diagUpRight) is True:
                #x.UpdateNode(self.diagMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("b", x))
                # adjacentList.append(x)
            if x.compareTo(f_diagDwnLeft) is True:
                #x.UpdateNode(self.diagMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("f", x))
                # adjacentList.append(x)
            if x.compareTo(h_diagDwnRight) is True:
                #x.UpdateNode(self.diagMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("h", x))
                # adjacentList.append(x)
            if x.compareTo(c_adjacentUp) is True:
                #x.UpdateNode(self.regMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("c", x))
                # adjacentList.append(x)
            if x.compareTo(g_adjacentDown) is True:
                #x.UpdateNode(self.regMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("g", x))
                # adjacentList.append(x)
            if x.compareTo(e_adjacentLeft) is True:
                #x.UpdateNode(self.regMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("e", x))
                # adjacentList.append(x)
            if x.compareTo(a_adjacentRight) is True:
                #x.UpdateNode(self.regMovement, x.GetDistance(target))
                # x.SetParent(node)
                adjacents.append(("a", x))
                # adjacentList.append(x)

        # for node in adjacentDict:
        adjacents.sort(key=lambda x: x[0])
        for node in adjacents:
            adjacentList.append(node[1])
        
        return adjacentList
        