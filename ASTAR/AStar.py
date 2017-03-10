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
    circleList = []

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

        circleSize = 20
        pixelDistance = 40

        xStart = self.xBoundary / 4
        yStart = (self.yBoundary / 2) + len(self.astarGrid.grid)

        xEnd = xStart + (pixelDistance * rowCount)
        # calculate end of x row

        x = xStart
        y = yStart

        for node in self.astarGrid.grid:
            node.SetPosition(x, y)
            self.engine.draw.circle(
                self.screen, (255, 255, 255), (x, y), circleSize)
            x += pixelDistance
            if x == xEnd:
                x = xStart
                y -= pixelDistance

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
        finished = False
        while not finished:
            for event in self.engine.event.get():
                if event.type == self.engine.QUIT:
                    finished = True

            # self.engine.draw.line(self.screen, 100, 200)
            self.DrawGrid()
            for node in self.astarGrid.grid:
                if self.currentNode == node:
                    node.print_info()

            self.engine.display.flip()
            # for node in astarGrid.grid:

        self.engine.quit()
    # make a update app function
    # work on class name
