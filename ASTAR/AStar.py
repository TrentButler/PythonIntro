from AstarTest import UnitTest
import AstarTest
from vector import Vector2

# WHAT I NEED

# GetPosition()
def GetPosition(node):
    return (node.position.xpos, node.position.ypos)

# COMPARETO
def compareTo(one, positionKey):
    if GetPosition(one) == positionKey:
        if one.iswalkable is True:
            return True
    return False
# GetDistance()
def GetDistance(one, two):
    xDist = abs(one.position.xpos - two.position.xpos) * 10
    yDist = abs(one.position.ypos - two.position.ypos) * 10
    return xDist + yDist
# GetAdjacentList()
def GetAdjacentList(self, ID, grid):
    adjacentList = []
    adjacents = []
    node = grid.getnode(ID)

    a_adjacentRight = (node.position.xpos + distance, node.position.ypos)
    b_diagUpRight = (node.position.xpos + distance, node.position.ypos - distance)
    c_adjacentUp = (node.position.xpos, node.position.ypos - distance)
    d_diagUpLeft = (node.position.xpos - distance, node.position.ypos - distance)
    e_adjacentLeft = (node.position.xpos - distance, node.position.ypos)
    f_diagDwnLeft = (node.position.xpos - distance, node.position.ypos + distance)
    g_adjacentDown = (node.position.xpos, node.position.ypos + distance)
    h_diagDwnRight = (node.position.xpos + distance, node.position.ypos + distance)

    for node in self.grid.nodes:
        if compareTo(GetPosition(node), d_diagUpLeft) is True:
            # x.UpdateNode(self.diagMovement, x.GetDistance(target))
            # x.SetParent(node)
            adjacents.append(("d", node))
            # adjacentList.append(x)
        if compareTo(GetPosition(node), b_diagUpRight) is True:
            # x.UpdateNode(self.diagMovement, x.GetDistance(target))
            # x.SetParent(node)
            adjacents.append(("b", node))
            # adjacentList.append(x)
        if compareTo(GetPosition(node), f_diagDwnLeft) is True:
            # x.UpdateNode(self.diagMovement, x.GetDistance(target))
            # x.SetParent(node)
            adjacents.append(("f", node))
            # adjacentList.append(x)
        if compareTo(GetPosition(node), h_diagDwnRight) is True:
            # x.UpdateNode(self.diagMovement, x.GetDistance(target))
            # x.SetParent(node)
            adjacents.append(("h", node))
            # adjacentList.append(x)
        if x.compareTo(GetPosition(node), c_adjacentUp) is True:
            # x.UpdateNode(self.regMovement, x.GetDistance(target))
            # x.SetParent(node)
            adjacents.append(("c", node))
            # adjacentList.append(x)
        if x.compareTo(GetPosition(node), g_adjacentDown) is True:
            # x.UpdateNode(self.regMovement, x.GetDistance(target))
            # x.SetParent(node)
            adjacents.append(("g", node))
            # adjacentList.append(x)
        if x.compareTo(GetPosition(node), e_adjacentLeft) is True:
            # x.UpdateNode(self.regMovement, x.GetDistance(target))
            # x.SetParent(node)
            adjacents.append(("e", node))
            # adjacentList.append(x)
        if x.compareTo(GetPosition(node), a_adjacentRight) is True:
            # x.UpdateNode(self.regMovement, x.GetDistance(target))
            # x.SetParent(node)
            adjacents.append(("a", node))
            # adjacentList.append(x)

    # for node in adjacentDict:
    adjacents.sort(key=lambda x: x[0])
    for node in adjacents:
        adjacentList.append(node[1])

    return adjacentList
# SetParent()
def SetParent(node, parentNode):
    node.parent = parentNode
# RETRACE()
def Retrace(end):
    retraced = []
    currentNode = end
    while currentNode.parent is not None:
        retraced.append(currentNode)
        currentNode = currentNode.parent
    return retraced

# UpdateNode()
def UpdateNode(node, G, H):
    node.gcost = G
    node.hcost = H
    node.fcost = node.gcost + node.hcost


# ALGORITHUM 

def AStarAlgorithum(start, goal, environment):  # PARENTING NEEDS WORK
        openlist = []
        closedlist = []
        current = start
        target = goal        
        
        UpdateNode(current.gcost, GetDistance(current, target))
        openlist.append(current)

        while len(openlist) is not 0:

            openlist.sort(key=lambda x: x.fcost)  # SORT OPENLIST
            current = openlist[0]  # ASSIGN CURRENTNODE MOST OPTIMAL NODE IN OPENLIST

            if current is target:  # CHECK IF CURRENTNODE IS TARGETNODE
                Retrace(goal)
                break
            
            openlist.remove(current)  # REMOVE CURRENTNODE FROM OPENLIST
            closedlist.append(current)  # APPEND CURRENTNODE TO CLOSED LIST
            adjList = GetAdjacentList(current.value, 1)  # GET CURRENTNODE'S ADJACENTS

            for node in adjList:  # CHECK ALL ADJACENT NODES FOR BEST PATH
                if node in closedlist:
                    continue

                tgCost = current.gcost + node.gcost  # needs work

                if node not in openlist and node.iswalkable is True:
                    SetParent(node, current)                    
                    openlist.append(node)

                if tgCost >= node.gcost:
                    continue

                SetParent(node, current)
                node.gcost = tgCost
                node.hcost = GetDistance(node, target)
                node.fcost = node.gcost + node.hcost


test = UnitTest("test.txt")
testing = test.testastar(AStarAlgorithum)