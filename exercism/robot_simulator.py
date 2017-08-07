'''
Robot simulator.
Takes a position (x, y) and facing a direction (bearing), the program moves
the robot according to the instructions.

added two dictionaries, one for the movement and one for the commands
'''

NORTH, EAST, SOUTH, WEST = 1, 2, 3, 4
MOVE = {NORTH : (0, 1), SOUTH: (0, -1), EAST : (1, 0), WEST : (-1, 0)}

class Robot:
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = x, y
        self.bearing = bearing
        self.command = {'R' : self.turn_right, 'L' : self.turn_left, 'A': self.advance}

    def turn_left(self):
        self.bearing -= 1
        if self.bearing < NORTH:
            self.bearing = WEST

    def turn_right(self):
        self.bearing += 1
        if self.bearing > WEST:
            self.bearing = NORTH

    def advance(self):
        dir_x, dir_y = MOVE[self.bearing]
        x, y = self.coordinates
        self.coordinates = x + dir_x, y + dir_y

    def simulate(self, instructions):
        for instruction in instructions:
            self.command[instruction]()