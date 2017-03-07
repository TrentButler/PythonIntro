from ASTAR.AStar import AStarApp
from ASTAR.ANode import Node

runAstar = AStarApp()
runAstar.InitGrid(4,4)
runAstar.SetStartNode(0,0)
runAstar.SetTargetNode(3,2)
runAstar.grid[2].SetWalkable(False)
runAstar.grid[10].SetWalkable(False)
runAstar.Start
for x in range(0, len(runAstar.grid)):
	print (str(runAstar.grid[x].wWalkable) + " " + "POSITION: " + runAstar.grid[x].GetPosition())
print ("NODECOUNT: " + str(runAstar.nodeCount))
print ("CURRENTNODE" + str(runAstar.currentNode.GetPosition()))
print ("TARGET" + runAstar.targetNode.GetPosition())

for x in range(0, len(runAstar.openList)):
	print("OPENLIST" + runAstar.openList[x].GetPosition())
for x in range(0, len(runAstar.GetAdjacent())):
	adjList = runAstar.GetAdjacent()
	print("ADJACENTLIST" + adjList[x].GetPosition())
raw_input()