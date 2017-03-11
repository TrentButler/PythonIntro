from ANode import Node
from AGrid import Grid
import pygame as pyEngine
import math as m


class AStarApp:
    engine = pyEngine
    xBoundary = None
    yBoundary = None
    screen = None
    openList = []
    closedList = []
    currentNode = Node()
    targetNode = Node()
    astarGrid = None    

    def __init__(self):
        self.engine.init()
        self.data = []

    def AddGrid(self, appGrid):
        self.astarGrid = appGrid

    def SetStartNode(self, ID):
        for node in self.astarGrid.grid:
            if node.nodeID == ID:
                self.currentNode = node

    def SetTargetNode(self, ID):
        for node in self.astarGrid.grid:
            if node.nodeID == ID:
                self.targetNode = node

    def DrawGrid(self):
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
                self.screen, (255, 255, 255), (x, y), self.circleSize)
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
        for node in self.astarGrid.GetAdjacentList(self.currentNode.nodeID, self.pixelDistance): # adjacents
            self.engine.draw.circle(self.screen, BLU, (node.GetPosition()), self.circleSize)
                # node.print_info()
        for node in self.astarGrid.grid:  # walkable
            if node.walkable is False:
                self.engine.draw.circle(self.screen, BRN, (node.GetPosition()), self.circleSize)
        self.engine.draw.circle(self.screen, GRE, (self.currentNode.GetPosition()), self.circleSize) # currentNode
        self.engine.draw.circle(self.screen, RED, (self.targetNode.GetPosition()), self.circleSize) # targetNode

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
        # self.engine.display.flip()
        self.openList.append(self.currentNode)
        print "START"

    def Run(self):       
        finished = False
        while not finished:           
            for event in self.engine.event.get():               
                if event.type == self.engine.QUIT:
                    finished = True
                # if event.type == (mouseclick in range of a node)
            self.DrawGrid()
            self.UpdateGrid()                       
            self.engine.display.flip()
        for node in self.astarGrid.GetAdjacentList(self.currentNode.nodeID, self.pixelDistance):
            node.print_info()
        self.engine.quit()
    # make a update app function
    # work on class name
    # make a updateAlgorithum function
