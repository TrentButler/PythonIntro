import os
import sys
sys.path.insert(0, "C:\Users\\trent.butler\Documents\GitHub\PythonIntro")
from Tools._MathLib import Vector2
from AGENT._agent import Agent

class ColliderAgent(Agent):
    '''AGENTCOLLIDER'''
    def __init__(self, identifier, size):
        super(ColliderAgent, self).__init__(identifier)
        self._position = Vector2(-1,-1)
        self._size = size
        self._hitbox = []

    def _setpos(self, position):
        self._position = position

    def _dist(self, col):
        xdist = abs(self._position._get_x() - col._position._get_x())
        ydist = abs(self._position._get_y() - col._position._get_y())
        return xdist + ydist

    def _run(self, force):
        self._position = self._position + force
        topright = self._position + Vector2(self._size, self._size)
        topleft = self._position + Vector2(-self._size, self._size)
        bottomleft = self._position + Vector2(-self._size, -self._size)
        bottomright = self._position + Vector2(self._size, -self._size)

        # self._hitbox = [topright, topleft, bottomleft, bottomright]
        self._hitbox = [self._position._get_x(), self._position._get_y(), self._size, self._size]

def rangecheck(agentlist, agentrange):
    for a in agentlist:
        for b in agentlist:
            if b is a:
                continue
            if b._dist(a) <= agentrange:            
                return True
def collisioncheck(a, b):
    # if a in b:
    # do stuff
    # if any corner from a, is in b
    if a._hitbox[0] <= b._hitbox[0] + b._hitbox[2] and a._hitbox[0] + a._hitbox[2] >= b._hitbox[0] and a._hitbox[1] <= b._hitbox[1] + b._hitbox[3] and a._hitbox[3] + a._hitbox[1] >= b._hitbox[1]:
        # print 'COLLISION'
        return True

    return False

agentone = ColliderAgent('agentone', 1)
agenttwo = ColliderAgent('agenttwo', 1)
agentone._setpos(Vector2(1, 2))
agenttwo._setpos(Vector2(6, 2))
agentone._run(Vector2(0, 0))
agenttwo._run(Vector2(0, 0))

counter = 0
done = False
while counter < 100 and not done:
    os.system("cls")
    print agentone._position
    print agenttwo._position

    if rangecheck([agentone,agenttwo], 2) is True:
        print 'AGENT IN RANGE'
        
    if collisioncheck(agentone, agenttwo) is True:
        print 'collision'
        break

    # if agentone._position == agenttwo._position:
        # done = True
    # agentone._run(Vector2(1, 0))
    # agenttwo._run(Vector2(-1, 0))
    counter += 1
