from ANode import Node

class Grid:
	grid = []	
	nodeCount = 0

	def __init__(self):
		self.data = []
	def InitilizeGrid(self, xBounds, yBounds):
		xIncrementor = 0
		yIncrementor = 0
		for x in range(0, int((xBounds * yBounds))):
			newNode = Node()
			newNode.nodeID = x
			self.grid.append(newNode)
			self.nodeCount += 1
		for x in range(0, self.nodeCount):
			self.grid[x].SetPosition(xIncrementor,yIncrementor)
			xIncrementor += 1
			if xIncrementor == xBounds:
				xIncrementor = 0
				yIncrementor += 1
	def GetGrid(self):
		return self.grid
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
	