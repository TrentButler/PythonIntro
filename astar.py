from ASTAR.AStar import AStarApp
from ASTAR.ANode import Node
from ASTAR.AGrid import Grid

runAstar = AStarApp()


grid = Grid()
grid.InitilizeGrid(4,4)


runAstar.AddGrid(grid)
runAstar.SetStartNode(0,0)
runAstar.SetTargetNode(3,2)
runAstar.astarGrid.grid[2].SetWalkable(False)
runAstar.astarGrid.grid[10].SetWalkable(False)
runAstar.Start

adjacentList = runAstar.GetAdjacentList(6)
for x in adjacentList:
	print(str(self) + x.GetPosition())

raw_input()


for x in range(0, len(runAstar.astarGrid.grid)):
	print (runAstar.astarGrid.grid[x].DebugNode())
print ("NODECOUNT: " + str(runAstar.astarGrid.grid.nodeCount))
print ("CURRENTNODE" + str(runAstar.currentNode.GetPosition()))
print ("TARGET" + runAstar.targetNode.GetPosition())

for x in range(0, len(runAstar.openList)):
	print("OPENLIST" + runAstar.openList[x].GetPosition())
for x in range(0, len(runAstar.GetAdjacent())):
	adjList = runAstar.GetAdjacent()
	print("ADJACENTLIST" + adjList[x].GetPosition())

adjDict = runAstar.GetAdjacentDictionary()	
for x in adjDict:
	print (x + adjDict[x].GetPosition())
	
raw_input()
