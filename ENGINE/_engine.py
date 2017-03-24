import pygame

class Engine(object):
    '''ENGINE'''
    def __init__(self,screenbounds):        
        self.engine = pygame
        self.engine.init()
        self._screen = self.engine.display.set_mode(screenbounds)
        # self._events = self.engine.event.get()
        self._clock = self.engine.time
        self._timer = 0.0        
        self._fps = 30
        self._running = True

    def _startup(self):
        return True

    def _update(self):
        self._timer = float(self._clock.get_ticks()) * 0.001
        for event in self.engine.event.get():
            if event.type == self.engine.KEYDOWN:
                if self.engine.key.get_pressed()[self.engine.K_ESCAPE]:
                    self._running = False

        if self._running is False:
            self._shutdown()
            return False

        return True     

    def _draw(self):
        # func()
        # self.engine.draw.circle(self._screen, (255,255,255), (90,90), 20)
        # self.engine.display.flip()
        return True
        

    def _shutdown(self):
        print "shutdown"
        self.engine.quit()
        