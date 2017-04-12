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
        self._range = 100
        self._collidepos = None

    def _addAgent(self, agent):
        if agent not in self._agentList:
            self._agentList.append(agent)

    def _helpmenu(self):
        width = self._boundary[0] / 2
        height = self._boundary[1] / 2
        _menu = self.engine.Surface((width, height), 0, self._screen)
        _menulist = []

        _add_agent = self.engine.font.Font(None, 40)
        _seek = self.engine.font.Font(None, 40)
        _flee = self.engine.font.Font(None, 40)
        _idle = self.engine.font.Font(None, 40)
        _wander = self.engine.font.Font(None, 40)
        _exit = self.engine.font.Font(None, 40)

        show_add_agent = _add_agent.render('(TAB KEY) -> ADD AGENT', 0, (255, 255, 255))
        show_seek = _seek.render('(F1 KEY)(LMB) -> SEEK BEHAVIOR', 0, (255, 255, 255))
        show_flee = _flee.render('(F2 KEY)(RMB) -> FLEE BEHAVIOR', 0, (255, 255, 255))
        show_idle = _idle.render('(F3 KEY)(MMB) -> WANDER BEHAVIOR', 0, (255, 255, 255))
        show_wander = _wander.render('(F4 KEY) -> IDLE BEHAVIOR', 0, (255, 255, 255))
        show_exit = _exit.render('(ESC KEY) -> EXIT APPLICATION', 0, (255, 255, 255))
        

        _menulist.append(show_exit)
        _menulist.append(show_add_agent)
        _menulist.append(show_seek)
        _menulist.append(show_flee)
        _menulist.append(show_idle)
        _menulist.append(show_wander)
        

        x = 10
        y = 10
        for text in _menulist:
            _menu.blit(text, (x, y))            
            y += 40
      
        return _menu

    def _rangecheck(self, a, b, arange):
        if b._dist(a) < arange:           
            return True

    def _collisioncheck(self):
        # NEEDS WORK
        if self._collidepos is not None:
            help_agent = SteerAgent('help_agent')
            help_agent._position = Vector2(self._collidepos[0], self._collidepos[1])
            if self._rangecheck(self._mouseAgent, help_agent, 25):
                x = self._boundary[0] / 4
                y = self._boundary[1] / 4
                self._screen.blit(self._helpmenu(), (x, y))
                print 'MENU'
       
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

        _menu = self.engine.font.Font(None, 60)
        show_menu = _menu.render('?', 0, (255, 255, 255))
        menu_position = (18, 12)
        self._collidepos = (30, 30)
        self._screen.blit(show_menu, menu_position)
        self.engine.draw.circle(self._screen, (255,255,255), self._collidepos, 30, 4)

        for agent in self._agentList:
            # self.engine.draw.circle(self._screen, (0, 255, 0), (int(agent._getpos()[0]), int(agent._getpos()[1])), agent._mass)
            if agent._current is 'WANDER':
                self.engine.draw.line(self._screen, (255, 255, 255), (int(agent._getpos()[0]), int(agent._getpos()[1])), (int(agent._wandercirc._getpos()[0]), int(agent._wandercirc._getpos()[1])), 4)
            
            topright = (agent._hitbox[0] + agent._hitbox[2], agent._hitbox[1] - agent._hitbox[3])
            topleft = (agent._hitbox[0] - agent._hitbox[2], agent._hitbox[1] - agent._hitbox[3])
            bottomleft = (agent._hitbox[0] - agent._hitbox[2], agent._hitbox[1] + agent._hitbox[3])
            bottomright = (agent._hitbox[0] + agent._hitbox[2], agent._hitbox[1] + agent._hitbox[3])
            self.engine.draw.lines(self._screen, (244,244,244), True, [topright, topleft, bottomleft, bottomright], 1)
            if agent._name is 'agent_one':
                self.engine.draw.lines(self._screen, (255,0,255), True, [topright, topleft, bottomleft, bottomright], 1)
        
            
        self.engine.draw.circle(self._screen, (255,255,255), (int(self._mouseAgent._getpos()[0]), int(self._mouseAgent._getpos()[1])), self._range, 4)
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
                                agent._state_machine.ChangeState('FLEE')                     

                        if self.engine.key.get_pressed()[self.engine.K_F3]:
                            for agent in self._agentList:
                                agent._state_machine.ChangeState('WANDER')
                        
                        if self.engine.key.get_pressed()[self.engine.K_F4]:
                            for agent in self._agentList:
                                agent._state_machine.ChangeState('IDLE')

                        if self.engine.key.get_pressed()[self.engine.K_TAB]:
                            count = len(self._agentList)
                            agent = SteerAgent('AGENT(' + str(count) + ')')
                            agent._init(Vector2(self._boundary[0] / 2, self._boundary[1] / 2), 10 + count , 1)
                            self._addAgent(agent)

                    if event.type == self.engine.QUIT:
                        self._running = False
                    if event.type == self.engine.MOUSEBUTTONDOWN:
                        if self.engine.mouse.get_pressed()[0]:
                            for agent in self._agentList:
                                if self._rangecheck(agent, self._mouseAgent, 100):
                                    # agent._force = agent._seek(self._mouseAgent) # ONLY HAPPENS PER CLICK
                                    agent._state_machine.ChangeState('SEEK')

                        if self.engine.mouse.get_pressed()[1]:
                            for agent in self._agentList:
                                if self._rangecheck(agent, self._mouseAgent, 100):
                                    # agent._force = agent._wander(100, 1, 1) # ONLY HAPPENS PER CLICK
                                    agent._state_machine.ChangeState('WANDER')

                        if self.engine.mouse.get_pressed()[2]:
                            for agent in self._agentList:
                                if self._rangecheck(agent, self._mouseAgent, 100):
                                    # agent._force = agent._flee(self._mouseAgent) # ONLY HAPPENS PER CLICK
                                    agent._state_machine.ChangeState('FLEE')
                
                self._collisioncheck() 
                self._update()
                self._draw()
                self.engine.display.flip()
        super(SteerApp, self)._shutdown()

app = SteerApp((1200, 600))

agent_one = SteerAgent('agent_one')
agent_two = SteerAgent('agent_two')
# agent_one._init(Vector2(0, app._boundary[1] / 2), 10, 1)
agent_one._init(Vector2(app._boundary[0] / 2, app._boundary[1] / 2), 10, 1)
agent_two._init(Vector2(app._boundary[0], app._boundary[1] / 2), 100, 1)

app._addAgent(agent_one)
# app._addAgent(agent_two)
app.run()
