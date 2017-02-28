class Node:
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
	#updateNode function?