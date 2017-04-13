from _test import *


def GetDistance(one, two):
    xDist = abs(two[0] - one[0])
    yDist = abs(two[1] - one[1])
    return xDist + yDist

def Retrace(end):
    retraced = []
    currentNode = end
    while currentNode.parent is not None:
        retraced.append(currentNode)
        currentNode = currentNode.parent
    retraced.append(currentNode)
    return retraced

def MoveCost(node, other):
    if node[0] == other[0] or node[1] == other[1]:
        return 10
    return 14

def AStarAlgorithum(start, goal, environment):
    '''ASTAR ALGORITHUM'''
    openlist = []
    closedlist = []
    result = []
    current = start
    target = goal
    
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
            result = Retrace(current) # RESULT IS ASSIGNED THE LIST FROM FUNCTION 'RETRACE()'
            break
        
        adjList = getneighbors(current, environment)  # GET CURRENTNODE'S ADJACENTS
        
        for node in adjList:  # CHECK ALL ADJACENT NODES FOR BEST PATH
            if node in closedlist or node.walkable is False: # IF NODE IS IN THE CLOSED LIST OR NOT WALKABLE, CONTINUE THE SEARCH
                continue
            
            tgCost = node.g + MoveCost(current, node) # CALCULATE THE TGCOST

            if node not in openlist and node.walkable is True: # IF NODE IS NOT IN THE OPENLIST AND WALKABLE, UPDTAE NODE 'FCOST' AND ASSIGN A PARENT
                node.parent = current
                node.f = node.g + node.h
                openlist.append(node) # APPEND NODE TO THE OPENLIST

            if tgCost >= node.g: # IF 'TGCOST' IS GREATER THAN NODE.G, CONTINUE THE SEARCH
                continue
            
            # IF 'TGCOST' IS LESS THAN NODE.G, UPDATE NODE AND RE-ASSIGN A PARENT (RE-PARENTING)
            node.parent = current 
            node.g = tgCost
            node.h = GetDistance(node, target)
            node.f = node.g + node.h

    return result # RETURN THE MOST OPTIMAL PATH
    