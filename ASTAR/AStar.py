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
			self.grid.append(newNode)
			self.nodeCount += 1
		for x in range(0, self.nodeCount):
			self.grid[x].SetPosition(xIncrementor,yIncrementor)
			xIncrementor += 1
			if xIncrementor == xBounds:
				xIncrementor = 0
				yIncrementor += 1
	def SetStartNode(self, xPos, yPos):
		for x in range(0, len(self.grid)):
			if self.grid[x].CompareTo(xPos, yPos) == True:
				self.currentNode = self.grid[x]
	def SetTargetNode(self, xPos, yPos):
		for x in range(0, len(self.grid)):
			if self.grid[x].CompareTo(xPos, yPos) == True:
				self.targetNode = self.grid[x]
	def Start(self):
		self.openList.append(self.currentNode)
	def GetAdjacent(self):
		adjacentList = []
		diagUpLeft = "(" + str(self.currentNode.xPosition - 1) + "," + str(self.currentNode.yPosition + 1) + ")"
		diagUpRight = "(" + str(self.currentNode.xPosition + 1) + "," + str(self.currentNode.yPosition + 1) + ")"
		diagDwnLeft = "(" + str(self.currentNode.xPosition - 1) + "," + str(self.currentNode.yPosition - 1) + ")"
		diagDwnRight = "(" + str(self.currentNode.xPosition + 1) + "," + str(self.currentNode.yPosition - 1) + ")"
		adjacentUp = "(" + str(self.currentNode.xPosition) + "," + str(self.currentNode.yPosition + 1) + ")"
		adjacentDown = "(" + str(self.currentNode.xPosition) + "," + str(self.currentNode.yPosition - 1) + ")"
		adjacentLeft = "(" + str(self.currentNode.xPosition - 1) + "," + str(self.currentNode.yPosition) + ")"
		adjacentRight = "(" + str(self.currentNode.xPosition + 1) + "," + str(self.currentNode.yPosition) + ")"
		
		for x in range(0, len(self.grid)):
			if self.grid[x].compareTo(diagUpLeft) == True:
				self.grid[x].UpdateNode(14,0)
				adjacentList.append(self.grid[x])
			if self.grid[x].compareTo(diagUpRight) == True:
				self.grid[x].UpdateNode(14,0)
				adjacentList.append(self.grid[x])
			if self.grid[x].compareTo(diagDwnLeft) == True:
				self.grid[x].UpdateNode(14,0)
				adjacentList.append(self.grid[x])
			if self.grid[x].compareTo(diagDwnRight) == True:
				self.grid[x].UpdateNode(14,0)
				adjacentList.append(self.grid[x])
			if self.grid[x].compareTo(adjacentUp) == True:
				self.grid[x].UpdateNode(10,0)
				adjacentList.append(self.grid[x])
			if self.grid[x].compareTo(adjacentDown) == True:
				self.grid[x].UpdateNode(10,0)
				adjacentList.append(self.grid[x])
			if self.grid[x].compareTo(adjacentLeft) == True:
				self.grid[x].UpdateNode(10,0)
				adjacentList.append(self.grid[x])
			if self.grid[x].compareTo(adjacentRight) == True:
				self.grid[x].UpdateNode(10,0)
				adjacentList.append(self.grid[x])
		return adjacentList
	#def Update():
	#make a update app function
	#work on class name