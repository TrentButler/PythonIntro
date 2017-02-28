class Node:
	xPosition = 0
	yPosition = 0
	hEstimatedCost = 0
	gMovementCost = 0
	fCost = 0
	wWalkable = False
	def __init__(self):
		self.data = []
		self.wWalkable = True
	def ANode(self, H, G, F, Walkable):
		self.hEstimatedCost = H
		self.gMovementCost = G
		self.fCost = F
		self.wWalkable = Walkable
	def SetPosition(self, X, Y):
		self.xPosition = int(X)
		self.yPosition = int(Y)
	#updateNode function?