import math
import rhinoscriptsyntax as rs

__all__ = ['Turtle']

class Turtle:
    """Represents a turtle in 3D space."""
    def __init__(self):
        """Creates a turtle at the origin, looking along the Y axis with its right side towards the X axis."""
        self._forward = rs.CreateVector(0, 1, 0)
        self._right = rs.CreateVector(1, 0, 0)
        self._position = rs.CreatePoint(0, 0, 0)
        self._lines = []
        self._pen_down = False

    def forward(self, distance):
        """Moves the turtle forward by the given distance. If the pen is down, adds a line along the path moved."""
        new_position = rs.PointAdd(self._position, rs.VectorScale(self._forward, distance))
        if self._pen_down:
            self._lines.append(rs.AddLine(self._position, new_position))
        self._position = new_position

    def backward(self, distance):
        """Moves the turtle backward by the given distance. If the pen is down, adds a line along the path moved."""
        self.forward(-distance)

    def left(self, angle):
        """Turns the turtle to the left by the given angle in degrees."""
        up = rs.VectorCrossProduct(self._right, self._forward)
        self._forward = rs.VectorRotate(self._forward, angle, up)
        self._right = rs.VectorRotate(self._right, angle, up)

    def right(self, angle):
        """Turns the turtle to the right by the given angle in degrees."""
        self.left(-angle)

    def tiltup(self, angle):
        """Tilts the turtle upwards by the given angle in degrees."""
        self._forward = rs.VectorRotate(self._forward, angle, self._right)

    def tiltdown(self, angle):
        """Tilts the turtle downwards by the given angle in degrees."""
        self.tiltup(-angle)

    def spincw(self, angle):
        """Spins the turtle clockwise by the given angle in degrees."""
        self._right = rs.VectorRotate(self._right, angle, self._forward)

    def spinccw(self, angle):
        """Spines the turtle counterclockwise by the given angle in degrees."""
        self.spincw(-angle)

    def setpos(self, x, y=None, z=None):
        """Sets the turtle's position to the given coordinates. If the pen is down, adds a line along the path moved.

        If y and z are omitted, assumes x is a point.
        If z is omitted, assumes z is 0."""
        if y is None and z is None:
            x, y, z = x
        if z is None:
            z = 0
        new_position = rs.CreatePoint(x, y, z)
        if self._pen_down:
            self._lines.append([self._position, new_position])
        self._position = new_position

    def setx(self, x):
        """Sets the X coordinate of the turtle's position to the given coordinates. If the pen is down, adds a line along the path moved."""
        self.setpos(x, self._position.Y, self._position.Z)

    def sety(self, y):
        """Sets the Y coordinate of the turtle's position to the given coordinates. If the pen is down, adds a line along the path moved."""
        self.setpos(self._position.X, y, self._position.Z)

    def setz(self, z):
        """Sets the Z coordinate of the turtle's position to the given coordinates. If the pen is down, adds a line along the path moved."""
        self.setpos(self._position.X, self._position.Y, z)

    #def settilt(self, angle):
    #    pass # uhhhhhh

    #def setturn(self, angle):
    #    pass # uhhhhhh

    #def setspin(self, angle):
    #    pass # uhhhhhhh

    def home(self):
        """Resets the position, direction, pen status, and lines of this turtle."""
        self.__init__()

    def position(self):
        """Gets the position of this turtle as a point."""
        return rs.CreatePoint(self._position)

    def xcor(self):
        """Gets the X coordinate of the turtle's position."""
        return self._position.X

    def ycor(self):
        """Gets the Y coordinate of the turtle's position."""
        return self._position.Y

    def zcor(self):
        """Gets the Z coordinate of the turtle's position."""
        return self._position.Z

    def tilt(self):
        """Gets the turtle's current tilt angle in degrees, with positive angles denoting an upwards tilt."""
        return math.degrees(math.atan2(self._forward.Z, math.sqrt(self._forward.X ** 2 + self._forward.Y ** 2)))

    def turn(self):
        """Gets the turtle's current turn angle in degrees, with positive angles denoting a rightwards turn."""
        return math.degrees(math.atan2(self._forward.X, self._forward.Y))

    def spin(self):
        """Gets the turtle's current spin angle in degrees, with positive angles denoting a clockwise spin."""
        return math.degrees(math.atan2(self._right.Z, math.sqrt(self._right.X ** 2 + self._right.Y ** 2)))

    def pendown(self):
        """Puts the turtle's pen down, so it starts drawing lines."""
        self._pen_down = True

    def penup(self):
        """Lifts the turtle's pen up, so it stops drawing lines."""
        self._pen_down = False

    def lines(self):
        """Gets the list of lines the turtle has drawn."""
        return list(self._lines)

_implicit_turtle = Turtle()
for key in Turtle.__dict__.keys():
    if not key.startswith('__'):
        globals()[key] = getattr(_implicit_turtle, key)
        __all__.append(key)
