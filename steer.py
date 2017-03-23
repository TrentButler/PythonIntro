from Tools._MathLib import Vector2
from _agent import Agent
import pygame

# NEEDS WORK
 
class SteerApp:
    def __init__(self, screenBounds):
        self.engine = pygame
        self.engine.init()
        self._screen = self.engine.display.set_mode(screenBounds)
        self._running = True
        self._agentList = []
        self._boundary = screenBounds
        self._mouseAgent = Agent('DEBUG', Vector2(4,4))        
        self._size = 20
        self._target = Agent('target', 0)
        self._target._init(Vector2(self._boundary[0] / 2, self._boundary[1] / 2))

    def _addAgent(self, agent):
        self._agentList.append(agent)

    def _collisioncheck(self, offset):
        # NEEDS WORK
        for agent in self._agentList:
            # if agent._velocity > Vector2(agent._max_velocity, agent._max_velocity):
                # agent._velocity = Vector2(0, 0)
                # agent._position = agent._position - Vector2(agent._max_velocity, agent._max_velocity)

            if agent._getpos()[0] >= self._boundary[0]:
                agent._velocity = Vector2(0, 0)
                agent._position = agent._position - Vector2(agent._max_velocity, agent._max_velocity)                            

            if agent._getpos()[0] <= 0:
                agent._velocity = Vector2(0, 0)
                agent._position = agent._position + Vector2(agent._max_velocity, agent._max_velocity)
        
            if agent._getpos()[1] >= self._boundary[1]:
                agent._velocity = Vector2(0, 0)
                agent._position = agent._position - Vector2(agent._max_velocity, agent._max_velocity)

            if agent._getpos()[1] <= 0:
                agent._velocity = Vector2(0, 0)
                agent._position = agent._position + Vector2(agent._max_velocity, agent._max_velocity)

    def _update(self, deltaTime):
        for agent in self._agentList:
            agent._run(deltaTime, self._target)        

    def _draw(self):
        for agent in self._agentList:
            self.engine.draw.circle(self._screen, (0, 255, 0), (int(agent._getpos()[0]), int(agent._getpos()[1])), self._size)
        self.engine.draw.circle(self._screen, (255,255,255), (int(self._mouseAgent._getpos()[0]), int(self._mouseAgent._getpos()[1])), 40, 4)
        self.engine.draw.circle(self._screen, (255,255,255), (int(self._target._getpos()[0]), int(self._target._getpos()[1])), 30)

    def run(self):
        # NEEDS WORK
        clock = self.engine.time.Clock()
        while self._running is True:
            clock.tick(30)
            timer = float(clock.get_time()) * 0.001
            self._screen.fill((0,0,0))
            self._mouseAgent._position = Vector2(self.engine.mouse.get_pos()[0], self.engine.mouse.get_pos()[1])
            for event in self.engine.event.get():
                if event.type == self.engine.KEYDOWN:
                    if self.engine.key.get_pressed()[self.engine.K_ESCAPE]:
                        self._running = False

                    if self.engine.key.get_pressed()[self.engine.K_F1]:
                        for agent in self._agentList:
                            agent._state_machine.ChangeState('SEEK')

                    if self.engine.key.get_pressed()[self.engine.K_F2]:
                        for agent in self._agentList:
                            agent._state_machine.ChangeState('IDLE')                     

                if event.type == self.engine.QUIT:
                    self._running = False
        
            
            
            
            
            self._collisioncheck(self._size)            
            self._update(timer)
            self._draw()
            self.engine.display.flip()            

        self.engine.quit()

app = SteerApp((1000, 600))

agent_one = Agent('agent_one', 60)
agent_two = Agent('agent_two', 60)
agent_one._init(Vector2(0, 0))
agent_two._init(Vector2(0, app._boundary[1]))


app._addAgent(agent_one)
app._addAgent(agent_two)
app.run()
