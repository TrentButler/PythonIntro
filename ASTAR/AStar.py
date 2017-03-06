from ANode import Node

class AStarApp:
	openList = []
	closedList = []
	currentNode = Node()
	targetNode = Node()
	grid = []
	nodeCount = 0
	def __init__(self):
		self.data = []
	def InitGrid(self, xBounds, yBounds):
		xIncrementor = 0
		yIncrementor = 0
		for x in range(0, int((xBounds * yBounds))):
			newNode = Node()
			newNode.setPosition(x + 1)
			self.grid.append(newNode)
			self.nodeCount += 1
		for x in range(0, self.nodeCount):
			self.grid[x].SetPosition(xIncrementor,yIncrementor)
			xIncrementor += 1
			if xIncrementor == xBounds:
				xIncrementor = 0
				yIncrementor += 1
	def Start(self, xPos, yPos):
		
		self.openList.append(self.grid)
	#def Update():
	#make a update app function
	#work on class name