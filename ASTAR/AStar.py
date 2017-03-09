from ANode import Node
from AGrid import Grid
import pygame as pyEngine

class AStarApp:
	engine = pyEngine
	screen = None
	openList = []
	closedList = []
	currentNode = Node()
	targetNode = Node()
	astarGrid = Grid()
	
	def __init__(self):
		self.engine.init()
		self.data = []
	def AddGrid(self, appGrid):
		self.astarGrid = appGrid
	def SetStartNode(self, xPos, yPos):
		for x in range(0, len(self.astarGrid.grid)):
			if self.astarGrid.grid[x].CompareTo(xPos, yPos) == True:
				self.currentNode = self.astarGrid.grid[x]
	def SetTargetNode(self, xPos, yPos):
		for x in range(0, len(self.astarGrid.grid)):
			if self.astarGrid.grid[x].CompareTo(xPos, yPos) == True:
				self.targetNode = self.astarGrid.grid[x]
	def Start(self):
		#init display
		self.engine.display.init()
		self.screen = self.engine.display.set_mode((860,600))
		self.engine.display.set_caption('Astar Project')
		self.engine.display.flip()
		self.openList.append(self.currentNode)
		print "START"
	
	
	
	def Update():
		finished = False
		while not finished:
			for event in engine.event.get():
					if event.type == engine.QUIT:
							finished = True
			engine.draw.rect(self.screen, (255,255,255), [600, 200, 50, 20], 2)
			#for node in astarGrid.grid:
				
		adjDict = self.GetAdjacentDictionary()
		for x in adjDict:
			if x not in self.openList:
				self.openList.append(x)
		
		for x in self.openList:
			if x.fCost < self.currentNode.fCost:
				self.closedList.append(self.currentNode)
				self.currentNode = x
				return "NODE CHANGED" + x.GetPosition()
		
		
				
		
		engine.quit()	
	#make a update app function
	#work on class name