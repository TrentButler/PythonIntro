import math

class Vector2(object):
    '''VECTOR2'''

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def _get_x(self):
        return self._x

    def _get_y(self):
        return self._y

    def mag(self):
        '''MAGNITUDE'''
        return math.sqrt((self._x * self._x) + (self._y * self._y))

    def norm(self):
        '''NORMALIZE'''
        return Vector2(self._x / self.mag(), self._y / self.mag())

    def dot(self, vec2):
        '''DOT'''
        return (self._x * vec2._getX()) + (self._y * vec2._getY())


class Vector3(object):
    '''VECTOR3'''

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def _get_x(self):
        return self._x

    def _get_y(self):
        return self._y

    def _get_z(self):
        return self._z

    def mag(self):
        '''MAGNITUDE'''
        return math.sqrt((self._x * self._x) + (self._y * self._y) + (self._z * self._z))

    def norm(self):
        '''NORMALIZE'''
        return Vector3(self._x / self.mag(), self._y / self.mag(), self._z / self.mag())

    def dot(self, vec3):
        '''DOT'''
        return (self._x * vec3._get_x()) + (self._y * vec3._get_y()) + (self._z * vec3._get_z())
