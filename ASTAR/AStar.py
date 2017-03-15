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
        self.currentNode.UpdateNode(self.currentNode.gCost, self.currentNode.GetDistance(self.targetNode))
        self.currentNode.SetParent(self.startNode)
        if self.run is True:
            while len(self.openList) is not 0:
                self.openList.sort(key=lambda x: x.fCost)  # SORT OPENLIST
                self.currentNode = self.openList[0]  # ASSIGN CURRENTNODE MOST OPTIMAL NODE IN OPENLIST                
                if self.currentNode is self.targetNode:  # CHECK IF CURRENTNODE IS TARGETNODE
                    self.closedList.append(self.targetNode)
                    for node in self.closedList:
                        node.print_info()
                        # node.print_parent()
                    print "COUNT: " + str(len(self.closedList))
                    self.run = False
                    break                   
                    # make returnPath function 
                
                # if len(self.openList) > 1:  # REMOVE CURRENTNODE FROM OPENLIST
                self.openList.remove(self.currentNode)
                # if self.currentNode not in self.closedList:  # APPEND CURRENTNODE TO CLOSED LIST                    
                self.closedList.append(self.currentNode)
                adjList = self.astarGrid.GetAdjacentList(self.currentNode.nodeID, self.offset, self.targetNode)  # GET CURRENTNODE'S ADJACENTS
                for node in adjList:  # CHECK ALL ADJACENT NODES FOR BEST PATH
                    if node in self.closedList:
                        continue
                    
                    if node not in self.openList and node.walkable is True:
                        self.openList.append(node)
                    
                    # if node in self.openList:
                        # if node.gCost > self.currentNode.gCost:
                            # node.SetParent(self.currentNode)
                            # node.UpdateNode(node.gCost, node.GetDistance(self.targetNode))
                    
                    tgCost = self.currentNode.gCost + node.gCost  # needs work
                    if tgCost >= node.gCost:
                        continue
                    # node.SetParent(self.currentNode)
                    # node.UpdateNode(tgCost, node.GetDistance(self.targetNode)) 
                    node.gCost = tgCost
                    node.hCost = node.GetDistance(self.targetNode)
                    node.fCost = node.gCost + node.hCost

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
        pointOne = 0
        pointTwo = 1
        
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
            if pointOne >= len(self.closedList) or pointTwo >= len(self.closedList):
               pointOne -= 1
               pointTwo -= 1        
            self.engine.draw.line(self.screen, PNK, self.closedList[pointOne].GetPosition(), self.closedList[pointTwo].GetPosition(), 6)
            pointOne += 1
            pointTwo += 1

        
         
    def ReStart(self, start, target):
        self.openList = []
        self.closedList = []
        self.currentNode = start
        self.targetNode = target
        self.startNode = start
        self.blockerNode = Node()
        self.astarGrid = self.saveGrid        
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

                    if self.engine.key.get_pressed()[self.engine.K_r]:
                        self.ReStart(self.startNode, self.targetNode)
                        print "RESTART SUCCESSFUL"

                    if self.engine.key.get_pressed()[self.engine.K_ESCAPE]:
                        finished = True


            self.DrawGrid()
            # self.RunStarAlgorithum()
            self.UpdateGrid()                       
            self.engine.display.flip()
        
        self.engine.quit()
    # make a update app function
    # work on class name
    # make a updateAlgorithum function
