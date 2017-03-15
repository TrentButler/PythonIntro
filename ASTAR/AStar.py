from ANode import Node
from AGrid import Grid
import pygame as pyEngine
import math as m


class AStarApp:
       

    def __init__(self):
        self.engine = pyEngine
        self.xBoundary = None
        self.yBoundary = None
        self.screen = None
        self.openList = []
        self.closedList = []
        self.currentNode = Node()
        self.targetNode = Node()
        self.startNode = Node()
        self.blockerNode = Node()
        self.astarGrid = None 
        self.engine.init()
        self.data = []
        self.run = True

    def AddGrid(self, appGrid):
        self.astarGrid = appGrid
        self.saveGrid = appGrid

    def SetStartNode(self, ID):
        for node in self.astarGrid.grid:
            if node.nodeID == ID:
                self.currentNode = node
                self.startNode = node

    def SetTargetNode(self, ID):
        for node in self.astarGrid.grid:
            if node.nodeID == ID:
                self.targetNode = node

    def RunStarAlgorithum(self):
        if self.run:
            
            while self.currentNode is not self.targetNode:
                self.currentNode.UpdateNode(self.currentNode.gCost, self.currentNode.GetDistance(self.targetNode))
                if self.currentNode not in self.closedList:
                    self.closedList.append(self.currentNode)

                adjList = self.astarGrid.GetAdjacentList(self.currentNode.nodeID, self.offset, self.targetNode)
                for node in adjList:
                    if node in self.closedList:
                        continue
                    tgCost = self.currentNode.gCost + node.GetDistance(self.currentNode)
                    if node not in self.openList and node.walkable is True:
                        self.openList.append(node)
                    if tgCost >= node.gCost:
                        continue
                    node.SetParent(self.currentNode)
                    node.UpdateNode(tgCost, node.GetDistance(self.targetNode)) 
                self.openList.sort(key=lambda x: x.fCost)
                self.currentNode = self.openList[0]
                if self.currentNode is self.targetNode:
                    self.closedList.append(self.currentNode)
                    for node in self.closedList:
                        node.print_parent()
                    self.run = False
                    # make returnPath function                                  

    def DrawGrid(self):
        AZU = (240, 255, 255)
        self.circleSize = int(self.offset/2)
        self.pixelDistance = self.offset
        xStart = self.offset
        yStart = self.yBoundary - self.offset
        xEnd = xStart + (self.pixelDistance * self.cols)
        # calculate end of x row
        x = int(xStart)
        y = int(yStart)
        for node in self.astarGrid.grid:
            node.SetPosition(x, y)
            self.engine.draw.circle(
                self.screen, AZU, (x, y), self.circleSize)
            x += self.pixelDistance
            if x == xEnd:
                x = xStart
                y -= self.pixelDistance

    def UpdateGrid(self): 
        BLK = (0, 0, 0)
        BRN = (139 ,69 ,19)
        BLU = (0, 0, 255)
        GRE = (0, 255, 0)
        RED = (255, 0, 0)
        YEL = (255, 255, 0)
        PNK = (255, 0, 255)
        
        self.engine.draw.circle(self.screen, PNK, (self.blockerNode.GetPosition()), self.circleSize, 2) # blockerNode
        for node in self.astarGrid.GetAdjacentList(self.currentNode.nodeID, self.offset, self.targetNode): # adjacents
            self.engine.draw.circle(self.screen, BLU, (node.GetPosition()), self.circleSize)
                # node.print_info()
        for node in self.astarGrid.grid:  # walkable
            if node.walkable is False:
                self.engine.draw.circle(self.screen, BRN, (node.GetPosition()), self.circleSize)
        
        for node in self.openList:  # openList
            self.engine.draw.circle(self.screen, YEL, (node.GetPosition()), self.circleSize, 2)
        self.engine.draw.circle(self.screen, GRE, (self.startNode.GetPosition()), self.circleSize) # startNode
        self.engine.draw.circle(self.screen, RED, (self.targetNode.GetPosition()), self.circleSize) # targetNode
        for node in self.closedList:  # path
            self.engine.draw.circle(self.screen, BLK, (node.parent.GetPosition()), self.circleSize / 2)
         
    def ReStart(self, start, target):
        self.engine = pyEngine
        self.xBoundary = None
        self.yBoundary = None
        self.screen = None
        self.openList = []
        self.closedList = []
        self.currentNode = Node()
        self.targetNode = target
        self.startNode = start
        self.blockerNode = Node()
        self.astarGrid = self.saveGrid 
        self.engine.init()
        self.data = []
        self.run = True

        self.Start()
        self.Run()

    def Start(self):
        # init display
        self.rows = self.astarGrid.GetBounds()[1]
        self.cols = self.astarGrid.GetBounds()[0]
        self.offset = 40        

        self.xBoundary = (self.cols * self.offset) + self.offset
        self.yBoundary = (self.rows * self.offset) + self.offset

        self.engine.display.init()
        self.screen = self.engine.display.set_mode((int(self.xBoundary), int(self.yBoundary)))
        self.engine.display.set_caption('Astar Project')

        if self.currentNode is not None:            
            self.openList.append(self.currentNode)        
        
        self.blockerNode.SetPosition(-(self.offset), -(self.offset))

        print "START"

    def Run(self):       
        finished = False
        while not finished:
           # self.blockerNode.SetPosition(self.engine.mouse.get_pos()[0], self.engine.mouse.get_pos()[1])
            for event in self.engine.event.get():               
                if event.type == self.engine.QUIT:
                    finished = True

                if event.type == self.engine.MOUSEBUTTONDOWN:
                    for node in self.astarGrid.grid:
                        if node.GetPosition() == self.blockerNode.GetPosition():
                            node.SetWalkable(False)

                if event.type == self.engine.KEYDOWN:
                    if self.engine.key.get_pressed()[self.engine.K_F8]:
                        self.RunStarAlgorithum()

                    if self.engine.key.get_pressed()[self.engine.K_F2]:                        
                        self.blockerNode.SetPosition(self.astarGrid.grid[0].GetPosition()[0], self.astarGrid.grid[0].GetPosition()[1])
                        
                    if self.engine.key.get_pressed()[self.engine.K_UP]:
                        self.blockerNode.yPosition -= (self.offset)
                    
                    if self.engine.key.get_pressed()[self.engine.K_DOWN]:
                        self.blockerNode.yPosition += (self.offset)

                    if self.engine.key.get_pressed()[self.engine.K_LEFT]:
                        self.blockerNode.xPosition -= (self.offset)

                    if self.engine.key.get_pressed()[self.engine.K_RIGHT]:
                        self.blockerNode.xPosition += (self.offset)

                    if self.engine.key.get_pressed()[self.engine.K_RETURN]:
                        for node in self.astarGrid.grid:
                            if node.GetPosition() == self.blockerNode.GetPosition():
                                node.SetWalkable(False)

                    if self.engine.key.get_pressed()[self.engine.K_SPACE]:
                        for node in self.astarGrid.grid:
                            if node.GetPosition() == self.blockerNode.GetPosition():
                                node.SetWalkable(True)
                                
                    if self.engine.key.get_pressed()[self.engine.K_LSHIFT]:
                        for node in self.astarGrid.grid:
                            if node.GetPosition() == self.blockerNode.GetPosition():
                                self.currentNode = node
                                self.startNode = node
                                self.openList = []
                                self.openList.append(self.currentNode)
                
                    if self.engine.key.get_pressed()[self.engine.K_RSHIFT]:
                        for node in self.astarGrid.grid:
                            if node.GetPosition() == self.blockerNode.GetPosition():
                                self.targetNode = node

                    # if self.engine.key.get_pressed()[self.engine.K_r]:
                        # self.ReStart(self.startNode, self.targetNode)
                        # print "RESTART SUCCESSFUL"

                    if self.engine.key.get_pressed()[self.engine.K_ESCAPE]:
                        finished = True


            self.DrawGrid()
            # self.RunStarAlgorithum()
            self.UpdateGrid()                       
            self.engine.display.flip()
        for node in self.astarGrid.GetAdjacentList(self.currentNode.nodeID, self.offset, self.targetNode):
            node.print_info()
        self.engine.quit()
    # make a update app function
    # work on class name
    # make a updateAlgorithum function
