from ENGINE._engine import Engine
from _test_agent import Agent
from FSM._FSM import _FSM
from Tools._MathLib import Vector2


class PhysicsApp(Engine):
    def __init__(self, bounds):
        super(PhysicsApp, self).__init__(bounds)
        self._objectlist = []

    def _initilize(self):
        return True

    def _update(self):
        if super(PhysicsApp, self)._update() is False:
            return False
        
        for gameobj in self._objectlist:
            gameobj._run(self._timer)

        return True

    def _draw(self):
        if super(PhysicsApp, self)._draw() is False:
            return False
        self._screen.fill((0, 0 ,0))
        for gameobj in self._objectlist:
            self.engine.draw.circle(self._screen, (255,255,255), (int(gameobj._position._get_x()), int(gameobj._position._get_y())), 50)

        return True

    def run(self):
        if super(PhysicsApp, self)._startup(self._initilize):
            while self._running is True:
                self._clock.tick(self._fps)
                for event in self.engine.event.get():
                    if event.type is self.engine.KEYDOWN:
                        if self.engine.key.get_pressed()[self.engine.K_ESCAPE]:
                            self._running = False
                        if self.engine.key.get_pressed()[self.engine.K_w]:
                            for obj in self._objectlist:
                                obj._velocity = Vector2(0, 20)
                                # needs work
        
                self._update()
                self._draw()
                self.engine.display.flip()

        super(PhysicsApp, self)._shutdown()

    def _addobject(self, gameobj):
        if gameobj not in self._objectlist:
            self._objectlist.append(gameobj)


def init_agent(position):
    # self._state_machine = _FSM()
    setattr(Agent, '_state_machine', _FSM())
    # self._current = None
    setattr(Agent, '_current', None)

    # self._state_machine.AddState('INIT')
    getattr(Agent, '_state_machine').AddState('INIT')
    # self._state_machine.AddState('IDLE')
    getattr(Agent, '_state_machine').AddState('IDLE')

    # self._state_machine.AddTransition('INIT', 'IDLE')
    getattr(Agent, '_state_machine').AddTransition(('INIT', 'IDLE'))

    # self._state_machine.StartMachine('INIT')
    getattr(Agent, '_state_machine').StartMachine('INIT') 

    setattr(Agent, '_position', Vector2(position[0], position[1]))      
    # self._position = posVec
    # self._velocity = Vector2(0, 0)
    setattr(Agent, '_velocity', Vector2(0, 0))
    # self._max_velocity = 60
    setattr(Agent, '_max_velocity', 60)
    # self._heading = Vector2(0, 0)
    setattr(Agent, '_heading', Vector2(0, 0))




def run_agent(deltaTime):
    # self._current = self._state_machine.currentstate
    setattr(Agent, '_current', getattr(Agent, '_state_machine').currentstate)

    if getattr(Agent, '_current') is 'INIT':
        # self._state_machine.ChangeState('IDLE')
        getattr(Agent, '_state_machine').ChangeState('IDLE')

    if getattr(Agent, '_current') is 'IDLE':
        # self._position = self._position + (self._velocity * deltaTime)
        v = getattr(Agent, '_velocity')
        position = getattr(Agent, '_position')
        force = position + v * deltaTime
        setattr(Agent, '_position', force)
        print "IDLE STATE"
   

app = PhysicsApp((1000, 800))
agentone = Agent('one', (600, 600), init_agent, run_agent)
app._addobject(agentone)

app.run()