class Car:
    def __init__(self, position=1, turning=False, colour='blue'):
        self.position = position
        self.turning = turning
        self.colour = colour

    def __str__(self):
        return "Car at the {} is {} turning. Colour is {}".format("get_position()", "is_turning()", self.colour)

    def get_position(self):
        if self.position == 1:
            return "Top"
        elif self.position == 2:
            return "Bottom"
        elif self.position == 3:
            return "Left"
        elif self.position == 4:
            return "Right"




