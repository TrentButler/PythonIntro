import pygame

class Engine(object):
    '''SUPER ENGINE'''
    def __init__(self,screenbounds):
        '''INITILIZE PYGAME WITH SPECIFIC BOUNDS, TIMER, SET FPS'''
        self.engine = pygame
        self.engine.init()
        self._screen = self.engine.display.set_mode(screenbounds)
        self._clock = self.engine.time.Clock()
        self._timer = 0.0        
        self._fps = 60
        self._running = True

    def _startup(self, func):
        '''INVOKE START UP FUNCTION, RETURN TRUE IF SUCCESSFUL'''
        func()
        return True

    def _update(self):
        '''CALCULATE DELTATIME, QUERY EVENTS, RETURN TRUE IF SUCCESSFUL'''
        self._timer = float(self._clock.get_time()) / 1000.0

        for event in self.engine.event.get():
            if event.type == self.engine.KEYDOWN:
                if self.engine.key.get_pressed()[self.engine.K_ESCAPE]:
                    self._running = False

        if self._running is False:
            return False

        return True     

    def _draw(self):
        '''DRAW, RETURN TRUE IF SUCCESSFUL'''
        return True

    def _shutdown(self):
        '''UNINITILIZE PYGAME'''
        print "SHUTDOWN"
        self.engine.quit()
        