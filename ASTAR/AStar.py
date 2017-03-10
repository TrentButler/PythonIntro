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
        rowCount = m.sqrt(len(self.astarGrid.grid))

        self.circleSize = 20
        self.pixelDistance = 40

        xStart = self.xBoundary / 4
        yStart = (self.yBoundary / 2) + len(self.astarGrid.grid)

        xEnd = xStart + (self.pixelDistance * rowCount)
        # calculate end of x row

        x = xStart
        y = yStart

        for node in self.astarGrid.grid:
            node.SetPosition(x, y)
            self.engine.draw.circle(
                self.screen, (255, 255, 255), (x, y), self.circleSize)
            x += self.pixelDistance
            if x == xEnd:
                x = xStart
                y -= self.pixelDistance

    def Start(self, xBound, yBound):
        # init display
        self.engine.display.init()
        self.xBoundary = xBound
        self.yBoundary = yBound
        self.screen = self.engine.display.set_mode((xBound, yBound))
        self.engine.display.set_caption('Astar Project')
        # self.engine.display.flip()
        self.openList.append(self.currentNode)
        print "START"

    def Run(self):
        BLK = (0, 0, 0)
        BRN = (139 ,69 ,19)
        BLU = (0, 0, 255)
        GRE = (0, 255, 0)
        RED = (255, 0, 0)
        finished = False
        while not finished:
            for event in self.engine.event.get():
                if event.type == self.engine.QUIT:
                    finished = True

            # self.engine.draw.line(self.screen, 100, 200)
            self.DrawGrid()
            self.engine.draw.circle(self.screen, GRE, (self.currentNode.GetPosition()), self.circleSize) # currentNode
            self.engine.draw.circle(self.screen, RED, (self.targetNode.GetPosition()), self.circleSize) # targetNode
            for node in self.astarGrid.GetAdjacentList(self.currentNode.nodeID, self.pixelDistance): # adjacents
                self.engine.draw.circle(self.screen, BLU, (node.GetPosition()), self.circleSize)
                # node.print_info()
            for node in self.astarGrid.grid:
                if node.walkable is False:
                    self.engine.draw.circle(self.screen, BRN, (node.GetPosition()), self.circleSize)
            self.engine.display.flip()
        for node in self.astarGrid.GetAdjacentList(self.currentNode.nodeID, self.pixelDistance):
            node.print_info()
        self.engine.quit()
    # make a update app function
    # work on class name
    # make a updateAlgorithum function
