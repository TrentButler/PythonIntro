from ANode import Node


class Grid:	
	grid = []	
	nodeCount = 0
	diagMovement = 14
	regMovement = 10

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
	
	def GetAdjacentList(self, ID):
		adjacentList = []
		
		diagUpLeft = "(" + str(self.grid[ID].xPosition - 1) + "," + str(self.grid[ID].yPosition + 1) + ")"
		diagUpRight = "(" + str(self.grid[ID].xPosition + 1) + "," + str(self.grid[ID].yPosition + 1) + ")"
		diagDwnLeft = "(" + str(self.grid[ID].xPosition - 1) + "," + str(self.grid[ID].yPosition - 1) + ")"
		diagDwnRight = "(" + str(self.grid[ID].xPosition + 1) + "," + str(self.grid[ID].yPosition - 1) + ")"
		adjacentUp = "(" + str(self.grid[ID].xPosition) + "," + str(self.grid[ID].yPosition + 1) + ")"
		adjacentDown = "(" + str(self.grid[ID].xPosition) + "," + str(self.grid[ID].yPosition - 1) + ")"
		adjacentLeft = "(" + str(self.grid[ID].xPosition - 1) + "," + str(self.grid[ID].yPosition) + ")"
		adjacentRight = "(" + str(self.grid[ID].xPosition + 1) + "," + str(self.grid[ID].yPosition) + ")"
		
		for x in self.grid:
			if x.compareTo(diagUpLeft) == True:
				x.UpdateNode(self.diagMovement,0)
				adjacentList.append(x)
			if x.compareTo(diagUpRight) == True:
				x.UpdateNode(self.diagMovement,0)
				adjacentList.append(x)
			if x.compareTo(diagDwnLeft) == True:
				x.UpdateNode(self.diagMovement,0)
				adjacentList.append(x)
			if x.compareTo(diagDwnRight) == True:
				x.UpdateNode(self.diagMovement,0)
				adjacentList.append(x)
			if x.compareTo(adjacentUp) == True:
				x.UpdateNode(self.regMovement,0)
				adjacentList.append(x)
			if x.compareTo(adjacentDown) == True:
				x.UpdateNode(self.regMovement,0)
				adjacentList.append(x)
			if x.compareTo(adjacentLeft) == True:
				x.UpdateNode(self.regMovement,0)
				adjacentList.append(x)
			if x.compareTo(adjacentRight) == True:
				x.UpdateNode(self.regMovement,0)
				adjacentList.append(x)
		return adjacentList
	def GetAdjacentDictionary(self, ID):
		adjacentDictionary = {}
		
		diagUpLeft = "(" + str(self.grid[ID].xPosition - 1) + "," + str(self.grid[ID].yPosition + 1) + ")"
		diagUpRight = "(" + str(self.grid[ID].xPosition + 1) + "," + str(self.grid[ID].yPosition + 1) + ")"
		diagDwnLeft = "(" + str(self.grid[ID].xPosition - 1) + "," + str(self.grid[ID].yPosition - 1) + ")"
		diagDwnRight = "(" + str(self.grid[ID].xPosition + 1) + "," + str(self.grid[ID].yPosition - 1) + ")"
		adjacentUp = "(" + str(self.grid[ID].xPosition) + "," + str(self.grid[ID].yPosition + 1) + ")"
		adjacentDown = "(" + str(self.grid[ID].xPosition) + "," + str(self.grid[ID].yPosition - 1) + ")"
		adjacentLeft = "(" + str(self.grid[ID].xPosition - 1) + "," + str(self.grid[ID].yPosition) + ")"
		adjacentRight = "(" + str(self.grid[ID].xPosition + 1) + "," + str(self.grid[ID].yPosition) + ")"
		
		for x in self.grid:
			if x.compareTo(diagUpLeft) == True:
				x.UpdateNode(self.diagMovement,0)
				adjacentDictionary["DIAGUPLEFT"] = x
			if x.compareTo(diagUpRight) == True:
				x.UpdateNode(self.diagMovement,0)
				adjacentDictionary["DIAGUPRIGHT"] = x
			if x.compareTo(diagDwnLeft) == True:
				x.UpdateNode(self.diagMovement,0)
				adjacentDictionary["DIAGDWNLEFT"] = x
			if x.compareTo(diagDwnRight) == True:
				x.UpdateNode(self.diagMovement,0)
				adjacentDictionary["DIAGDWNRIGHT"] = x
			if x.compareTo(adjacentUp) == True:
				x.UpdateNode(self.regMovement,0)
				adjacentDictionary["UP"] = x
			if x.compareTo(adjacentDown) == True:
				x.UpdateNode(self.regMovement,0)
				adjacentDictionary["DOWN"] = x
			if x.compareTo(adjacentLeft) == True:
				x.UpdateNode(self.regMovement,0)
				adjacentDictionary["LEFT"] = x
			if x.compareTo(adjacentRight) == True:
				x.UpdateNode(self.regMovement,0)
				adjacentDictionary["RIGHT"] = x
		
		return adjacentDictionary
	
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
	