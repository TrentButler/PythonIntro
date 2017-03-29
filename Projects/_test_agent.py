from Tools._MathLib import Vector2
from FSM._FSM import _FSM

class Agent:
    

    def __init__(self, name, position, initfunc, runfunc):
        self._name = name
        # self._position = Vector2(position[0], position[1])
        initfunc(position)
        self._runfunc = runfunc
    
    def _run(self, arg):
        self._runfunc(arg)