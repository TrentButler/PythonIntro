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
runAstar.Start()

