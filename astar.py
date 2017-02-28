from ASTAR.AStar import AStarApp
from ASTAR.ANode import Node

runAstar = AStarApp()
runAstar.InitGrid(25)
for x in range(0, len(runAstar.grid)):
	print (str(runAstar.grid[x].wWalkable))
raw_input()