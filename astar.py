from ASTAR.AStar import AStarApp
from ASTAR.ANode import Node

runAstar = AStarApp()
runAstar.InitGrid(4,4)
for x in range(0, len(runAstar.grid)):
	print (str(runAstar.grid[x].wWalkable) + " " + "POSITION: " + runAstar.grid[x].GetPosition() +" numPosition: "+str(runAstar.grid[x].Position))
print("COUNT: " + str(runAstar.nodeCount))
raw_input()