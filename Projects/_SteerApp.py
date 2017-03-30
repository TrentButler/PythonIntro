import sys
sys.path.insert(0, "C:\Users\\trent.butler\Documents\GitHub\PythonIntro")
from ENGINE._engine import Engine
from Tools._MathLib import Vector2
from steer_agent import SteerAgent
import pygame
import os

# NEEDS WORK
class SteerApp(Engine):
    def __init__(self, screenBounds):
        super(SteerApp, self).__init__(screenBounds)
        self._agentList = []
        self._boundary = screenBounds
        self._mouseAgent = SteerAgent('DEBUG')
        self._target = SteerAgent('TARGET')
        self._target._init(Vector2(self._boundary[0] / 2, self._boundary[1] / 2), 1, 1)
        self._size = 30

    def _addAgent(self, agent):
        if agent not in self._agentList:
            self._agentList.append(agent)

    def _collisioncheck(self):
        # NEEDS WORK
        for agent in self._agentList:
            agentONE = Vector2(int(agent._position._get_x()) + self._size, int(agent._position._get_y()) + self._size)
            for checking in self._agentList:
                agentTWO = Vector2(int(checking._position._get_x()) + self._size, int(checking._position._get_y()) + self._size)
                if checking is agent:
                    continue
                if agentONE == agentTWO:
                    agent._velocity = Vector2(0,0)
                    checking._velocity = Vector2(0,0)
                    print "COLLISION"

                
        for agent in self._agentList:
            if agent._getpos()[0] >= self._boundary[0] - self._size:
                agent._state_machine.ChangeState('IDLE')
                agent._velocity = agent._velocity + (Vector2(-agent._max_velocity, 0) * self._timer)
                agent._state_machine.ChangeState('WANDER')
                # agent._position = agent._position - Vector2(agent._max_velocity, agent._max_velocity)                            

            if agent._getpos()[0] <= 0 + self._size:
                agent._state_machine.ChangeState('IDLE')
                agent._velocity = agent._velocity + (Vector2(agent._max_velocity, 0) * self._timer)
                agent._state_machine.ChangeState('WANDER')
                # agent._position = agent._position + Vector2(agent._max_velocity, agent._max_velocity)
        
            if agent._getpos()[1] >= self._boundary[1] - self._size:
                agent._state_machine.ChangeState('IDLE')
                agent._velocity = agent._velocity + (Vector2(0, -agent._max_velocity) * self._timer)
                agent._state_machine.ChangeState('WANDER')

            if agent._getpos()[1] <= 0 + self._size:
                agent._state_machine.ChangeState('IDLE')
                agent._velocity = agent._velocity + (Vector2(0, agent._max_velocity) * self._timer)
                agent._state_machine.ChangeState('WANDER')
                # agent._position = agent._position + Vector2(agent._max_velocity, agent._max_velocity)

    def _update(self):
        if super(SteerApp, self)._update() is False:
            return False
        for agent in self._agentList:
            agent._run(self._timer, self._mouseAgent)
            # print agent._name + "(" + str(agent._heading._get_x()) + "," + str(agent._heading._get_y()) + ")" + str(agent._getpos())
            # continue
        return True     

    def _draw(self):
        if super(SteerApp, self)._draw() is False:
            return False
        for agent in self._agentList:
            self.engine.draw.circle(self._screen, (0, 255, 0), (int(agent._getpos()[0]), int(agent._getpos()[1])), self._size)
            if agent._current is 'WANDER':
                self.engine.draw.line(self._screen, (255, 255, 255), (int(agent._getpos()[0]), int(agent._getpos()[1])), (int(agent._wandercirc._getpos()[0]), int(agent._wandercirc._getpos()[1])), 4)
            # pointA = (agent._position._get_x() + self._size / 2, agent._position._get_y())
            # pointB = (agent._position._get_x() - self._size / 2, agent._position._get_y())
            # self.engine.draw.lines(self._screen, (0, 255, 0), True, [pointA, pointB, (agent._heading._get_x(), agent._heading._get_y())])
        self.engine.draw.circle(self._screen, (255,255,255), (int(self._mouseAgent._getpos()[0]), int(self._mouseAgent._getpos()[1])), self._size, 4)
        # self.engine.draw.circle(self._screen, (255,255,255), (int(self._target._getpos()[0]), int(self._target._getpos()[1])), 30)
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
                        
                        if self.engine.key.get_pressed()[self.engine.K_F4]:
                            for agent in self._agentList:
                                agent._state_machine.ChangeState('WANDER')

                        if self.engine.key.get_pressed()[self.engine.K_TAB]:
                            count = len(self._agentList)
                            agent = SteerAgent('AGENT(' + str(count) + ')')
                            agent._init(Vector2(self._boundary[0] / 2, self._boundary[1] / 2), (60 + (len(self._agentList) * 10) ), 1 + count)
                            self._addAgent(agent)

                    if event.type == self.engine.QUIT:
                        self._running = False                
                
                self._collisioncheck()                  
                self._update()
                self._draw()
                self.engine.display.flip()
        super(SteerApp, self)._shutdown()

app = SteerApp((1200, 600))

agent_one = SteerAgent('agent_one')
agent_two = SteerAgent('agent_two')
agent_one._init(Vector2(0, app._boundary[1] / 2), 60, 1)
agent_two._init(Vector2(app._boundary[0], app._boundary[1] / 2), 60, 1)

# app._addAgent(agent_one)
# app._addAgent(agent_two)
app.run()