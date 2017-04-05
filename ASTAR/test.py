import sys
sys.path.insert(0, "C:\Users\\trent.butler\Documents\GitHub\PythonIntro")
from AStar import *
from _test import *
 
#to test your astar it must follow these conventions
#preconditions: node objects must have g f h and parent variables
#node objects must access position elements through node[0] "posx" or node[1] "posy"
#so if you have a node.positionx it will be node[0]
#so if you have a node.positiony it will be node[1]
#to calculate neighbors replace your fetch for adjacents/neighbors with
#getneighbors(current, graph)
#this returns a list of nodes
#parameters: start, goal, graph
#postconditions: function will return a list


def main():
    failcount = 0
    passcount = 0
    for _ in range(100):
        res = testfunc(AStarAlgorithum)
        if res:
            passcount += 1
        else:
            failcount += 1
    print str.format('fails {0}, passes {1}', failcount, passcount)
    

if __name__ == '__main__':
    main()