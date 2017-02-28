from ANode import Node

class AStarApp:
	openList = []
	closedList = []
	currentNode = Node()
	grid = []
	def __init__(self):
		self.data = []
	def InitGrid(self, gridSize):
		for x in range(0, gridSize):
			self.grid.append(Node())
	#make a update app function
	#work on class name