from Tools._MathLib import Vector2
from FSM._FSM import _FSM
from AGENT._agent import Agent
import random
import math

class SteerAgent(Agent):
    '''STEER AGENT'''

    def __init__(self, name):
        super(SteerAgent, self).__init__(name)
    
    def _init(self, posVec, max_vel, mass):
        self._state_machine = _FSM()
        self._current = None

        self._state_machine.AddState('INIT')
        self._state_machine.AddState('IDLE')
        self._state_machine.AddState('SEEK')
        self._state_machine.AddState('FLEE')
        self._state_machine.AddState('WANDER')

        self._state_machine.AddTransition(('INIT', 'IDLE'))
        self._state_machine.AddTransition(('IDLE', 'SEEK'))
        self._state_machine.AddTransition(('IDLE', 'FLEE'))
        self._state_machine.AddTransition(('IDLE','WANDER'))
        self._state_machine.AddTransition(('SEEK', 'IDLE'))
        self._state_machine.AddTransition(('SEEK', 'FLEE'))
        self._state_machine.AddTransition(('SEEK', 'WANDER'))        
        self._state_machine.AddTransition(('FLEE', 'IDLE'))
        self._state_machine.AddTransition(('FLEE', 'SEEK'))
        self._state_machine.AddTransition(('FLEE', 'WANDER'))
        self._state_machine.AddTransition(('WANDER', 'IDLE'))
        self._state_machine.AddTransition(('WANDER', 'SEEK'))
        self._state_machine.AddTransition(('WANDER', 'FLEE'))
        
        self._state_machine.StartMachine('INIT')        
        self._position = posVec
        self._velocity = Vector2(0, 0)
        self._max_velocity = max_vel
        self._heading = Vector2(0, 0)
        self._mass = mass
        self._wandercirc = SteerAgent(self._name + "(" + "wander" + ")")
        
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
    
    def _wander(self, rad, dist, jit, strength):
        startrange = Vector2(-(rad * math.cos(jit)), -(rad * math.sin(jit)))
        stoprange = Vector2(rad * math.cos(jit), rad * math.sin(jit))

        print str(self._getpos())
        origin = self._heading * dist
        start = origin + startrange
        stop = origin + stoprange
        target = SteerAgent('wander')
        target._init(self._choice(start, stop), 0, 0)
        self._wandercirc = target
        return self._seek(target)

        
    def _getpos(self):
        '''RETURNS TUPLE'''
        return (self._position._get_x(), self._position._get_y())
    
    def _getdist(self, target):
        # _xdist = self._getpos()[0] - target._getpos()[0]
        _xdist = target._getpos()[0] - self._getpos()[0]
        # _ydist = self._getpos()[1] - target._getpos()[1]
        _ydist = target._getpos()[1] - self._getpos()[1]
        return Vector2(_xdist, _ydist)
    
    def _choice(self, start, stop):
        # x = random.randint(int(start._get_x()), int(stop._get_x()))
        # y = random.randint(int(start._get_y()), int(stop._get_y()))

        x = random.uniform(start._get_x(), stop._get_x())
        y = random.uniform(start._get_y(), stop._get_y())

        return Vector2(x, y)
    
    def _run(self, deltaTime, target):
        if super(SteerAgent, self)._run():

            self._current = self._state_machine.currentstate

            if self._current is 'INIT':
                self._state_machine.ChangeState('IDLE')

            if self._current is 'IDLE':
                accel = self._velocity * deltaTime
                force = accel * self._mass
                self._position = self._position + force
                self._heading = self._velocity.norm()
                print self._heading._get_x(), self._heading._get_y()          
                # print "IDLE STATE"

            if self._current is 'SEEK':
                self._velocity = self._velocity + (self._seek(target) * deltaTime)
                self._position = self._position + (self._velocity * deltaTime) * self._mass
                self._heading = self._velocity.norm()
                print self._heading._get_x(), self._heading._get_y() 
                # print "SEEK STATE"

            if self._current is 'FLEE':
                self._velocity = self._velocity + (self._flee(target) * deltaTime)
                self._position = self._position + (self._velocity * deltaTime) * self._mass
                self._heading = self._velocity.norm()
                print self._heading._get_x(), self._heading._get_y()
                # print "FLEE STATE"

            if self._current is 'WANDER':
                self._velocity = self._velocity + (self._wander(60, 10, 45, 2) * deltaTime)
                self._position = self._position + (self._velocity * deltaTime) * self._mass
                self._heading = self._velocity.norm()
                print self._heading._get_x(), self._heading._get_y()
                # self._wandercirc = self._wander(60, 100, 45, 2)
                # print "WANDER"
                
