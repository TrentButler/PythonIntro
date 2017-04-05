from _test import *
# WHAT I NEED


# GetDistance()
def GetDistance(one, two):
    xDist = abs(two[0] - one[0])
    yDist = abs(two[1] - one[1])
    return xDist + yDist
# GetAdjacentList()
def GetAdjacentList(node, grid):
    return getneighbors(node, grid)

def Retrace(end):
    retraced = []
    currentNode = end
    while currentNode.parent is not None:
        retraced.append(currentNode)
        currentNode = currentNode.parent
    # retraced.append(currentNode)
    return retraced

def MoveCost(node, other):
    if node[0] == other[0] or node[1] == other[1]:
        return 10
    return 14

# ALGORITHUM 

def AStarAlgorithum(start, goal, environment):  # PARENTING NEEDS WORK
    openlist = []
    closedlist = []
    result = []
    current = start
    target = goal
    
    # UpdateNode(current, current.g, GetDistance(current, target))
    current.g = 0
    current.h = GetDistance(current, target)
    current.f = current.g + current.h
    openlist.append(current)

    while len(openlist) is not 0:

        openlist.sort(key=lambda x: x.f)  # SORT OPENLIST
        current = openlist[0]  # ASSIGN CURRENTNODE MOST OPTIMAL NODE IN OPENLIST
        openlist.remove(current)  # REMOVE CURRENTNODE FROM OPENLIST
        closedlist.append(current)  # APPEND CURRENTNODE TO CLOSED LIST            
        if current is target:  # CHECK IF CURRENTNODE IS TARGETNODE
            result = Retrace(current)
            break
        
        adjList = GetAdjacentList(current, environment)  # GET CURRENTNODE'S ADJACENTS
        
        for node in adjList:  # CHECK ALL ADJACENT NODES FOR BEST PATH
            if node in closedlist or node.walkable is False:
                continue
            
            tgCost = node.g + MoveCost(current, node)  # needs work

            if node not in openlist and node.walkable is True:
                node.parent = current
                node.g = MoveCost(current, node)
                node.h = GetDistance(node, target)
                node.f = node.g + node.h
                openlist.append(node)

            if tgCost >= node.g:
                continue

            node.parent = current
            node.g = tgCost
            node.h = GetDistance(node, target)
            node.f = node.g + node.h

    return result