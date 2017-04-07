import sys
# sys.path.insert(0, "C:\Users\Redtrent\Documents\GitHub\PythonIntro")
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

    def _rangecheck(self, agentlist, agentrange):
        for a in agentlist:
            for b in agentlist:
                if b is a:
                    continue
                if b._dist(a) < agentrange:           
                    return True

    def _collisioncheck(self):
        # NEEDS WORK
        
        for a in self._agentList:
            if len(self._agentList) > 1:
                for b in self._agentList:
                    if b is a:
                        continue
                    if self._rangecheck(self._agentList, a._size) is True:
                        if len(a._hitbox) > 3 and len(b._hitbox) > 3:
                            # a._hitbox[]
                            if a._hitbox[0] <= b._hitbox[0] + b._hitbox[2] and a._hitbox[0] + a._hitbox[2] >= b._hitbox[0] and a._hitbox[1] <= b._hitbox[1] + b._hitbox[3] and a._hitbox[3] + a._hitbox[1] >= b._hitbox[1]:
                                pierce_dist = a._position - b._position
                                # a._state_machine.ChangeState('IDLE')
                                # b._state_machine.ChangeState('IDLE')
                                a._position = a._position + (-pierce_dist)
                                b._position = b._position + (-pierce_dist)
                                a._force = a._getdist(b) * (-a._max_velocity)
                                b._force = b._getdist(a) * (-b._max_velocity)
                                
                                print '(' + a._name + ') COLLISION (' + b._name + ')'
                
        for agent in self._agentList:
            if agent._getpos()[0] >= self._boundary[0] - agent._size:
                agent._state_machine.ChangeState('IDLE')
                agent._force = Vector2(-agent._max_velocity, 0)
                # agent._state_machine.ChangeState('WANDER')
                # agent._position = agent._position - Vector2(agent._max_velocity, agent._max_velocity)                            

            if agent._getpos()[0] <= 0 + agent._size:
                agent._state_machine.ChangeState('IDLE')
                agent._force = Vector2(agent._max_velocity, 0)
                # agent._state_machine.ChangeState('WANDER')
                # agent._position = agent._position + Vector2(agent._max_velocity, agent._max_velocity)
        
            if agent._getpos()[1] >= self._boundary[1] - agent._size:
                agent._state_machine.ChangeState('IDLE')
                agent._force = Vector2(0, -agent._max_velocity)
                # agent._state_machine.ChangeState('WANDER')

            if agent._getpos()[1] <= 0 + agent._size:
                agent._state_machine.ChangeState('IDLE')
                agent._force = Vector2(0, agent._max_velocity)
                # agent._state_machine.ChangeState('WANDER')
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
            # self.engine.draw.circle(self._screen, (0, 255, 0), (int(agent._getpos()[0]), int(agent._getpos()[1])), agent._mass)
            if agent._current is 'WANDER':
                self.engine.draw.line(self._screen, (255, 255, 255), (int(agent._getpos()[0]), int(agent._getpos()[1])), (int(agent._wandercirc._getpos()[0]), int(agent._wandercirc._getpos()[1])), 4)
            self.engine.draw.circle(self._screen, (255,255,255), (int(self._mouseAgent._getpos()[0]), int(self._mouseAgent._getpos()[1])), 30, 4)
            topright = (agent._hitbox[0] + agent._hitbox[2], agent._hitbox[1] - agent._hitbox[3])
            topleft = (agent._hitbox[0] - agent._hitbox[2], agent._hitbox[1] - agent._hitbox[3])
            bottomleft = (agent._hitbox[0] - agent._hitbox[2], agent._hitbox[1] + agent._hitbox[3])
            bottomright = (agent._hitbox[0] + agent._hitbox[2], agent._hitbox[1] + agent._hitbox[3])
            self.engine.draw.lines(self._screen, (244,244,244), True, [topright, topleft, bottomleft, bottomright], 1)
        # self.engine.draw.circle(self._screen, (255,255,255), (int(self._target._getpos()[0]), int(self._target._getpos()[1])), 30)
            if agent._name is 'agent_one':
                self.engine.draw.lines(self._screen, (255,0,255), True, [topright, topleft, bottomleft, bottomright], 1)
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
                            agent._init(Vector2(self._boundary[0] / 2, self._boundary[1] / 2), 10 + count , 1)
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
agent_one._init(Vector2(0, app._boundary[1] / 2), 10, 1)
agent_two._init(Vector2(app._boundary[0], app._boundary[1] / 2), 100, 1)

app._addAgent(agent_one)
app._addAgent(agent_two)
app.run()
