from ASTAR.AStar import AStarApp
from ASTAR.ANode import Node
from ASTAR.AGrid import Grid


# def getNode(id, graph):
# for x in graph.grid:
# if x.nodeID == id:
# return x
# return "ERROR"


# def getNeighbors(node, graph):
# return graph.GetAdjacentList(node.nodeID)

# node = getNode(2, grid)
# neighbors = getNeighbors(node, grid)

# node.print_info()

# for n in neighbors:
# n.print_info()


runAstar = AStarApp()
grid = Grid(10, 10)
runAstar.AddGrid(grid)
runAstar.SetStartNode(100)
runAstar.SetTargetNode(1)

runAstar.astarGrid.grid[1].SetWalkable(False)
runAstar.astarGrid.grid[10].SetWalkable(False)
for x in range(80,87):
    runAstar.astarGrid.grid[x].SetWalkable(False)
for x in range(77, 79):
    runAstar.astarGrid.grid[x].SetWalkable(False)
runAstar.Start()
runAstar.Run()
