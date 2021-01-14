import rhinoscriptsyntax as rs

__all__ = ['Turtle']

class Turtle:
    def __init__(self):
        self._forward = rs.CreateVector(0, 1, 0)
        self._right = rs.CreateVector(1, 0, 0)
        self._position = rs.CreatePoint(0, 0, 0)
        self._lines = []
        self._pen_down = False

    def forward(self, distance):
        new_position = rs.PointAdd(self._position, rs.VectorScale(self._forward, distance))
        if self._pen_down:
            self._lines.append(rs.AddLine(self._position, new_position))
        self._position = new_position

    def backward(self, distance):
        self.forward(-distance)

    def left(self, angle):
        up = rs.VectorCrossProduct(self._right, self._forward)
        self._forward = rs.VectorRotate(self._forward, angle, up)
        self._right = rs.VectorRotate(self._right, angle, up)

    def right(self, angle):
        self.left(-angle)

    def tiltup(self, angle):
        self._forward = rs.VectorRotate(self._forward, angle, self._right)

    def tiltdown(self, angle):
        self.tiltup(-angle)

    def spincw(self, angle):
        self._right = rs.VectorRotate(self._right, angle, self._forward)

    def spinccw(self, angle):
        self.spincw(-angle)

    def setpos(self, x, y=None, z=None):
        if y is None and z is None:
            x, y, z = x
        if z is None:
            z = 0
        new_position = rs.CreatePoint(x, y, z)
        if self._pen_down:
            self._lines.append([self._position, new_position])
        self._position = new_position

    def setx(self, x):
        self.setpos(x, self._position.Y, self._position.Z)

    def sety(self, y):
        self.setpos(self._position.X, y, self._position.Z)

    def setz(self, z):
        self.setpos(self._position.X, self._position.Y, z)

    def setpitch(self, angle):
        pass # uhhhhhh

    def setyaw(self, angle):
        pass # uhhhhhh

    def setroll(self, angle):
        pass # uhhhhhhh

    def home(self):
        self.__init__()

    def position(self):
        return rs.CreatePoint(self._position)

    def xcor(self):
        return self._position.X

    def ycor(self):
        return self._position.Y

    def zcor(self):
        return self._position.Z

    def pitch(self):
        pass # uhhhhhhhhhhh

    def yaw(self):
        pass # uhhhhhhhhhhhhhhhhhhhhhh

    def roll(self):
        pass # uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

    def pendown(self):
        self._pen_down = True

    def penup(self):
        self._pen_down = False

    def lines(self):
        return list(self._lines)

_implicit_turtle = Turtle()
for key in Turtle.__dict__.keys():
    if not key.startswith('__'):
        globals()[key] = getattr(_implicit_turtle, key)
        __all__.append(key)
