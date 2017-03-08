from ANode import Node
from AGrid import Grid

class AStarApp:
	openList = []
	closedList = []
	currentNode = Node()
	targetNode = Node()
	astarGrid = Grid()
	diagMovement = 14
	regMovement = 10
	def __init__(self):
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
		
		for x in range(0, len(self.astarGrid.grid)):
			if self.astarGrid.grid[x].compareTo(diagUpLeft) == True:
				self.astarGrid.grid[x].UpdateNode(self.diagMovement,0)
				adjacentList.append(self.astarGrid.grid[x])
			if self.astarGrid.grid[x].compareTo(diagUpRight) == True:
				self.astarGrid.grid[x].UpdateNode(self.diagMovement,0)
				adjacentList.append(self.astarGrid.grid[x])
			if self.astarGrid.grid[x].compareTo(diagDwnLeft) == True:
				self.astarGrid.grid[x].UpdateNode(self.diagMovement,0)
				adjacentList.append(self.astarGrid.grid[x])
			if self.astarGrid.grid[x].compareTo(diagDwnRight) == True:
				self.astarGrid.grid[x].UpdateNode(self.diagMovement,0)
				adjacentList.append(self.astarGrid.grid[x])
			if self.astarGrid.grid[x].compareTo(adjacentUp) == True:
				self.astarGrid.grid[x].UpdateNode(self.regMovement,0)
				adjacentList.append(self.astarGrid.grid[x])
			if self.astarGrid.grid[x].compareTo(adjacentDown) == True:
				self.astarGrid.grid[x].UpdateNode(self.regMovement,0)
				adjacentList.append(self.astarGrid.grid[x])
			if self.astarGrid.grid[x].compareTo(adjacentLeft) == True:
				self.astarGrid.grid[x].UpdateNode(self.regMovement,0)
				adjacentList.append(self.astarGrid.grid[x])
			if self.astarGrid.grid[x].compareTo(adjacentRight) == True:
				self.astarGrid.grid[x].UpdateNode(self.regMovement,0)
				adjacentList.append(self.astarGrid.grid[x])
		return adjacentList
	def GetAdjacentDictionary(self):
		adjacentDictionary = {}
		
		diagUpLeft = "(" + str(self.currentNode.xPosition - 1) + "," + str(self.currentNode.yPosition + 1) + ")"
		diagUpRight = "(" + str(self.currentNode.xPosition + 1) + "," + str(self.currentNode.yPosition + 1) + ")"
		diagDwnLeft = "(" + str(self.currentNode.xPosition - 1) + "," + str(self.currentNode.yPosition - 1) + ")"
		diagDwnRight = "(" + str(self.currentNode.xPosition + 1) + "," + str(self.currentNode.yPosition - 1) + ")"
		adjacentUp = "(" + str(self.currentNode.xPosition) + "," + str(self.currentNode.yPosition + 1) + ")"
		adjacentDown = "(" + str(self.currentNode.xPosition) + "," + str(self.currentNode.yPosition - 1) + ")"
		adjacentLeft = "(" + str(self.currentNode.xPosition - 1) + "," + str(self.currentNode.yPosition) + ")"
		adjacentRight = "(" + str(self.currentNode.xPosition + 1) + "," + str(self.currentNode.yPosition) + ")"
		
		for x in range(0, len(self.astarGrid.grid)):
			if self.astarGrid.grid[x].compareTo(diagUpLeft) == True:
				self.astarGrid.grid[x].UpdateNode(self.diagMovement,0)
				adjacentDictionary["DIAGUPLEFT"] = self.astarGrid.grid[x] 
			if self.astarGrid.grid[x].compareTo(diagUpRight) == True:
				self.astarGrid.grid[x].UpdateNode(self.diagMovement,0)
				adjacentDictionary["DIAGUPRIGHT"] = self.astarGrid.grid[x]
			if self.astarGrid.grid[x].compareTo(diagDwnLeft) == True:
				self.astarGrid.grid[x].UpdateNode(self.diagMovement,0)
				adjacentDictionary["DIAGDWNLEFT"] = self.astarGrid.grid[x]
			if self.astarGrid.grid[x].compareTo(diagDwnRight) == True:
				self.astarGrid.grid[x].UpdateNode(self.diagMovement,0)
				adjacentDictionary["DIAGDWNRIGHT"] = self.astarGrid.grid[x]
			if self.astarGrid.grid[x].compareTo(adjacentUp) == True:
				self.astarGrid.grid[x].UpdateNode(self.regMovement,0)
				adjacentDictionary["UP"] = self.astarGrid.grid[x]
			if self.astarGrid.grid[x].compareTo(adjacentDown) == True:
				self.astarGrid.grid[x].UpdateNode(self.regMovement,0)
				adjacentDictionary["DOWN"] = self.astarGrid.grid[x]
			if self.astarGrid.grid[x].compareTo(adjacentLeft) == True:
				self.astarGrid.grid[x].UpdateNode(self.regMovement,0)
				adjacentDictionary["LEFT"] = self.astarGrid.grid[x]
			if self.astarGrid.grid[x].compareTo(adjacentRight) == True:
				self.astarGrid.grid[x].UpdateNode(self.regMovement,0)
				adjacentDictionary["RIGHT"] = self.astarGrid.grid[x]
		
		return adjacentDictionary
	def GetAdjacentList(self, ID):
		adjacentList = []
		
		diagUpLeft = "(" + str(self.astarGrid.grid[ID].xPosition - 1) + "," + str(self.astarGrid.grid[ID].yPosition + 1) + ")"
		diagUpRight = "(" + str(self.astarGrid.grid[ID].xPosition + 1) + "," + str(self.astarGrid.grid[ID].yPosition + 1) + ")"
		diagDwnLeft = "(" + str(self.astarGrid.grid[ID].xPosition - 1) + "," + str(self.astarGrid.grid[ID].yPosition - 1) + ")"
		diagDwnRight = "(" + str(self.astarGrid.grid[ID].xPosition + 1) + "," + str(self.astarGrid.grid[ID].yPosition - 1) + ")"
		adjacentUp = "(" + str(self.astarGrid.grid[ID].xPosition) + "," + str(self.astarGrid.grid[ID].yPosition + 1) + ")"
		adjacentDown = "(" + str(self.astarGrid.grid[ID].xPosition) + "," + str(self.astarGrid.grid[ID].yPosition - 1) + ")"
		adjacentLeft = "(" + str(self.astarGrid.grid[ID].xPosition - 1) + "," + str(self.astarGrid.grid[ID].yPosition) + ")"
		adjacentRight = "(" + str(self.astarGrid.grid[ID].xPosition + 1) + "," + str(self.astarGrid.grid[ID].yPosition) + ")"
		
		for x in range(0, len(self.astarGrid.grid)):
			if self.astarGrid.grid[ID].compareTo(diagUpLeft) == True:
				self.astarGrid.grid[ID].UpdateNode(self.diagMovement,0)
				adjacentList.append(self.astarGrid.grid[ID])
			if self.astarGrid.grid[ID].compareTo(diagUpRight) == True:
				self.astarGrid.grid[ID].UpdateNode(self.diagMovement,0)
				adjacentList.append(self.astarGrid.grid[ID])
			if self.astarGrid.grid[ID].compareTo(diagDwnLeft) == True:
				self.astarGrid.grid[ID].UpdateNode(self.diagMovement,0)
				adjacentList.append(self.astarGrid.grid[ID])
			if self.astarGrid.grid[ID].compareTo(diagDwnRight) == True:
				self.astarGrid.grid[ID].UpdateNode(self.diagMovement,0)
				adjacentList.append(self.astarGrid.grid[ID])
			if self.astarGrid.grid[ID].compareTo(adjacentUp) == True:
				self.astarGrid.grid[ID].UpdateNode(self.regMovement,0)
				adjacentList.append(self.astarGrid.grid[ID])
			if self.astarGrid.grid[ID].compareTo(adjacentDown) == True:
				self.astarGrid.grid[ID].UpdateNode(self.regMovement,0)
				adjacentList.append(self.astarGrid.grid[ID])
			if self.astarGrid.grid[ID].compareTo(adjacentLeft) == True:
				self.astarGrid.grid[ID].UpdateNode(self.regMovement,0)
				adjacentList.append(self.astarGrid.grid[ID])
			if self.astarGrid.grid[ID].compareTo(adjacentRight) == True:
				self.astarGrid.grid[ID].UpdateNode(self.regMovement,0)
				adjacentList.append(self.astarGrid.grid[ID])
		return adjacentList
	def Update():
		adjDict = self.GetAdjacentDictionary()
		for x in adjDict:
			if x not in self.openList:
				self.openList.append(x)
		
		for x in self.openList:
			if x.fCost < self.currentNode.fCost:
				self.closedList.append(self.currentNode)
				self.currentNode = x
				return "NODE CHANGED" + x.GetPosition()
		
		
				
		
			
	#make a update app function
	#work on class name