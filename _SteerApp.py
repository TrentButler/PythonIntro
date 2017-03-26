from ENGINE._engine import Engine
from Tools._MathLib import Vector2
from _agent import Agent
import pygame

# NEEDS WORK
 
class SteerApp(Engine):
    def __init__(self, screenBounds):
        super(SteerApp, self).__init__(screenBounds)
        self._agentList = []
        self._boundary = screenBounds
        self._mouseAgent = Agent('DEBUG')
        self._target = Agent('TARGET')
        self._target._init(Vector2(self._boundary[0] / 2, self._boundary[1] / 2), 0, 0)
        self._size = 40

    def _addAgent(self, agent):
        if agent not in self._agentList:
            self._agentList.append(agent)

    def _collisioncheck(self):
        # NEEDS WORK
        for agent in self._agentList:
            if agent._getpos()[0] >= self._boundary[0] - self._size:
                agent._state_machine.ChangeState('IDLE')
                agent._velocity = agent._velocity + (Vector2(-agent._max_velocity, 0) * self._timer)
                # agent._position = agent._position - Vector2(agent._max_velocity, agent._max_velocity)                            

            if agent._getpos()[0] <= 0 + self._size:
                agent._state_machine.ChangeState('IDLE')
                agent._velocity = agent._velocity + (Vector2(agent._max_velocity, 0) * self._timer)
                # agent._position = agent._position + Vector2(agent._max_velocity, agent._max_velocity)
        
            if agent._getpos()[1] >= self._boundary[1] - self._size:
                # agent._state_machine.ChangeState('IDLE')
                agent._velocity = agent._velocity + (Vector2(0, -agent._max_velocity) * self._timer)
                

            if agent._getpos()[1] <= 0 + self._size:
                agent._state_machine.ChangeState('IDLE')
                agent._velocity = agent._velocity + (Vector2(0, agent._max_velocity) * self._timer)
                # agent._position = agent._position + Vector2(agent._max_velocity, agent._max_velocity)

    def _update(self):
        if super(SteerApp, self)._update() is False:
            return False
        for agent in self._agentList:
            agent._run(self._timer, self._mouseAgent)
            # continue
        return True     

    def _draw(self):
        if super(SteerApp, self)._draw() is False:
            return False
        for agent in self._agentList:
            self.engine.draw.circle(self._screen, (0, 255, 0), (int(agent._getpos()[0]), int(agent._getpos()[1])), self._size)
        self.engine.draw.circle(self._screen, (255,255,255), (int(self._mouseAgent._getpos()[0]), int(self._mouseAgent._getpos()[1])), 40, 4)
        self.engine.draw.circle(self._screen, (255,255,255), (int(self._target._getpos()[0]), int(self._target._getpos()[1])), 30)
        return True

    def run(self):
        # NEEDS WORK
        if super(SteerApp, self)._startup(self._collisioncheck):
            while self._running is True:
                self._clock.tick(self._fps)           
                self._screen.fill((0,0,0))
                self._mouseAgent._position = Vector2(self.engine.mouse.get_pos()[0], self.engine.mouse.get_pos()[1])
                for event in self.engine.event.get():
                    if event.type == self.engine.KEYDOWN:
                        if self.engine.key.get_pressed()[self.engine.K_ESCAPE]:
                            self._running = False
                            # super(SteerApp, self)._shutdown()

                        if self.engine.key.get_pressed()[self.engine.K_F1]:
                            for agent in self._agentList:
                                agent._state_machine.ChangeState('SEEK')                                

                        if self.engine.key.get_pressed()[self.engine.K_F2]:
                            for agent in self._agentList:
                                agent._state_machine.ChangeState('IDLE')                     

                        if self.engine.key.get_pressed()[self.engine.K_F3]:
                            for agent in self._agentList:
                                agent._state_machine.ChangeState('FLEE')
                        
                        if self.engine.key.get_pressed()[self.engine.K_TAB]:
                            count = len(self._agentList)
                            agent = Agent('AGENT(' + str(count) + ')')
                            agent._init(Vector2(self._boundary[0] / 2, self._boundary[1] / 2), (60 + (len(self._agentList) * 10) ), 10 + len(self._agentList))
                            self._addAgent(agent)

                    if event.type == self.engine.QUIT:
                        self._running = False                
                
                self._collisioncheck()                  
                self._update()
                self._draw()
                self.engine.display.flip()
        super(SteerApp, self)._shutdown()






app = SteerApp((1440, 800))

agent_one = Agent('agent_one')
agent_two = Agent('agent_two')
agent_one._init(Vector2(0, 0), 100, 100)
agent_two._init(Vector2(0, app._boundary[1]), 60, 200)


# app._addAgent(agent_one)
# app._addAgent(agent_two)
app.run()