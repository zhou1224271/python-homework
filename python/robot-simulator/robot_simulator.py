# Globals for the bearings
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    def advance(self):
        if self.bearing == EAST:
            self.x += 1
        elif self.bearing == WEST:
            self.x -= 1
        elif self.bearing == NORTH:
            self.y += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        else:
            raise ValueError("impossible")

    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = NORTH
        else:
            raise ValueError("impossible")

    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = NORTH
        else:
            raise ValueError("impossible")

    def simulate(self, instructions):
        for instruction in instructions:
            if "A" == instruction:
                self.advance()
            elif "L" == instruction:
                self.turn_left()
            elif "R" == instruction:
                self.turn_right()
            else:
                raise ValueError("impossible")

    @property
    def coordinates(self):
        return self.x, self.y