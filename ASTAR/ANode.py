class Node:
	xPosition = 0
	yPosition = 0
	nParent = []
	hEstimatedCost = 0
	gMovementCost = 0
	fCost = 0
	wWalkable = False
	def __init__(self):
		self.data = []
		self.wWalkable = True
	def InitNode(self, H, G, F, Walkable):
		self.hEstimatedCost = H
		self.gMovementCost = G
		self.fCost = F
		self.wWalkable = Walkable
	def SetPosition(self, X, Y):
		self.xPosition = int(X)
		self.yPosition = int(Y)
	def SetWalkable(self, walkable):
		self.wWalkable = walkable
	def GetPosition(self):
		return str("(") + str(self.xPosition) + "," + str(self.yPosition) + str(")")
	def SetParent(self, parentNode):
		for x in range(0, len(self.nParent)):
			nParent[x] = parentNode
	def CompareTo(self, X, Y):
		selfPosition = str(self.xPosition) + "," + str(self.yPosition)
		comparePosition = str(X) + "," + str(Y)
		if selfPosition == comparePosition:
			if self.wWalkable == True:
				return True
		return False
	def compareTo(self, positionKey):
		selfPosition = "(" + str(self.xPosition) + "," + str(self.yPosition) + ")"
		if selfPosition == positionKey:
			if self.wWalkable == True:
				return True
		return False
	def UpdateNode(self, G, H):
		self.gMovementCost = G
		self.hEstimatedCost = H
	#updateNode function?