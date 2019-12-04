class TrafficLight:
    def __init__(self, canvas, colour):
        self.canvas = canvas
        self.colour = colour

    def turn_red(self):
        self.colour = 'red'

    def turn_green(self):
        self.colour = 'green'
