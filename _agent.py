from Tools._MathLib import Vector2
from FSM._FSM import _FSM

class Agent:
    

    def __init__(self, name, max_vel):
        self._name = name
        self._position = Vector2(0, 0)
        self._velocity = Vector2(0, 0)
        self._max_velocity = max_vel
        self._heading = Vector2(0, 0)
        self._state_machine = _FSM()
        self._current = None
    
    def _init(self, posVec):
        self._state_machine.AddState('INIT')
        self._state_machine.AddState('IDLE')
        self._state_machine.AddState('SEEK')

        self._state_machine.AddTransition('INIT', 'IDLE')
        self._state_machine.AddTransition('IDLE', 'SEEK')
        self._state_machine.AddTransition('SEEK', 'IDLE')

        self._state_machine.StartMachine('INIT')        
        self._position = posVec

    def _run(self, deltaTime, target):
        self._current = self._state_machine.currentstate               
        if self._current is 'INIT':
            # print "INIT STATE"
            self._state_machine.ChangeState('IDLE')
        if self._current is 'IDLE':
            # self._position = self._position + Vector2(1,1)
            self._velocity = Vector2(0, 0)
            print "IDLE STATE"
        if self._current is 'SEEK':
            # WHAT I NEED.
            # VECTOR * VECTOR
            # VECTOR * SCALER            

            # NEEDS WORK

            self._velocity = self._velocity + (self._seek(target) * deltaTime)
            self._position = self._position + (self._velocity * deltaTime)
            self._heading = self._velocity.norm()
            print "SEEK STATE"
        
    def _seek(self, target):
        new = self._position - target._position
        V = new.norm() * self._max_velocity
        force = V - self._velocity
        return force

    
    def _getpos(self):
        return (self._position._get_x(), self._position._get_y())
