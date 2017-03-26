from Tools._MathLib import Vector2
from FSM._FSM import _FSM

class Agent:
    

    def __init__(self, name):
        self._name = name        
    
    def _init(self, posVec, max_vel, mass):
        self._state_machine = _FSM()
        self._current = None

        self._state_machine.AddState('INIT')
        self._state_machine.AddState('IDLE')
        self._state_machine.AddState('SEEK')
        self._state_machine.AddState('FLEE')

        self._state_machine.AddTransition(('INIT', 'IDLE'))
        self._state_machine.AddTransition(('IDLE', 'SEEK'))
        self._state_machine.AddTransition(('IDLE', 'FLEE'))
        self._state_machine.AddTransition(('SEEK', 'IDLE'))
        self._state_machine.AddTransition(('SEEK', 'FLEE'))
        self._state_machine.AddTransition(('FLEE', 'IDLE'))
        self._state_machine.AddTransition(('FLEE', 'SEEK'))

        self._state_machine.StartMachine('INIT')        
        self._position = posVec
        self._velocity = Vector2(0, 0)
        self._max_velocity = max_vel
        self._heading = Vector2(0, 0)
        self._mass = mass
        
    def _seek(self, target):
        new = self._getdist(target)
        V = new.norm() * self._max_velocity
        force = V - self._velocity
        return force

    def _flee(self, target):
        new = target._getdist(self)
        V = new.norm() * self._max_velocity
        force = V - self._velocity
        return force
    
    def _getpos(self):
        '''RETURNS TUPLE'''
        return (self._position._get_x(), self._position._get_y())
    
    def _getdist(self, target):
        # _xdist = self._getpos()[0] - target._getpos()[0]
        _xdist = target._getpos()[0] - self._getpos()[0]
        # _ydist = self._getpos()[1] - target._getpos()[1]
        _ydist = target._getpos()[1] - self._getpos()[1]
        return Vector2(_xdist, _ydist)

    def _run(self, deltaTime, target):
        self._current = self._state_machine.currentstate              
        if self._current is 'INIT':
            # print "INIT STATE"
            self._state_machine.ChangeState('IDLE')
        if self._current is 'IDLE':
            # self._position = self._position + Vector2(1,1)
            # self._velocity = Vector2(1, 1)
            # self._velocity = self._velocity * deltaTime
            self._position = self._position + ((self._velocity * deltaTime))
            # self._heading = self._velocity.norm()
            print "IDLE STATE"
        if self._current is 'SEEK':
            # WHAT I NEED.
            # VECTOR * VECTOR
            # VECTOR * SCALER            

            # NEEDS WORK

            self._velocity = self._velocity + ((self._seek(target) * deltaTime) * self._mass)
            self._position = self._position + (self._velocity * deltaTime)
            self._heading = self._velocity.norm()
            print "SEEK STATE"

        if self._current is 'FLEE':
            self._velocity = self._velocity + ((self._flee(target) * deltaTime) * self._mass) 
            self._position = self._position + (self._velocity * deltaTime)
            self._heading = self._velocity.norm()
            print "FLEE STATE"