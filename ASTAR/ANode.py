class Node:
	xPosition = 0
	yPosition = 0
	Position = 0
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
	def setPosition(self, Pos):
		self.Position = Pos
	def GetPosition(self):
		return str("(") + str(self.xPosition) + "," + str(self.yPosition) + str(")")
	def SetParent(self, parentNode):
		for x in range(0, len(self.nParent)):
			nParent[x] = parentNode
	def UpdateNode(self, H, G, F):
		self.hEstimatedCost = H
		self.gMovementCost = G
		self.fCost = F
	#updateNode function?