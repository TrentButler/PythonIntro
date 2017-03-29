from ASTAR.AStar import AStarApp
from ASTAR.ANode import Node
from ASTAR.AGrid import Grid


runAstar = AStarApp()
grid = Grid(10, 10)
runAstar.AddGrid(grid)
runAstar.SetStartNode(1)
runAstar.SetTargetNode(len(runAstar.astarGrid.grid))
runAstar.Start()
runAstar.Run()

#make two functions manhattan_distance(node) return int and costtomove(node)
#manhattan_distance will always be divisible by 10
