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

    def _run(self, force):
        self._position = self._position + force

        self._hitbox = [self._position, self._size]


def collisioncheck(a, b):
    # if a in b:
    # do stuff
    # if any corner from a, is in b        

    return True

agentone = ColliderAgent('agentone', (1, 1))
agenttwo = ColliderAgent('agenttwo', (1, 1))
agentone._setpos(Vector2(1, 2))
agenttwo._setpos(Vector2(4, 2))
agentone._run(Vector2(0, 0))
agenttwo._run(Vector2(0, 0))

counter = 0
done = False
while counter < 100 and not done:
    os.system("cls")
    print agentone._position
    print agenttwo._position
    if collisioncheck(agentone, agenttwo) is False:
        done = True

    if agentone._position == agenttwo._position:
        done = True
    agentone._run(Vector2(1, 0))
    agenttwo._run(Vector2(-1, 0))
    counter += 1
