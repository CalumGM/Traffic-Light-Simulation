'''
the light will just be one circle object but changing fill colour and position depending on the condition
'''


class TrafficLight:
    def __init__(self, canvas, position, colour):
        self.canvas = canvas
        self.position = position
        self.colour = colour
        self.light_circle = None

    def turn_red(self):
        self.colour = 'red'
        if self.position == 1:  # top
            self.canvas.move(self.light_circle, 0, 40)
            self.canvas.itemconfig(self.light_circle, fill=self.colour)
        elif self.position == 2:  # bottom
            self.canvas.move(self.light_circle, 0, -40)
            self.canvas.itemconfig(self.light_circle, fill=self.colour)
        elif self.position == 3:  # left
            self.canvas.move(self.light_circle, 40, 0)
            self.canvas.itemconfig(self.light_circle, fill=self.colour)
        elif self.position == 4:  # right
            self.canvas.move(self.light_circle, -40, 0)
            self.canvas.itemconfig(self.light_circle, fill=self.colour)

    def turn_green(self):
        self.colour = 'green'
        if self.position == 1:  # top
            self.canvas.move(self.light_circle, 0, -40)
            self.canvas.itemconfig(self.light_circle, fill=self.colour)
        elif self.position == 2:  # bottom
            self.canvas.move(self.light_circle, 0, 40)
            self.canvas.itemconfig(self.light_circle, fill=self.colour)
        elif self.position == 3:  # left
            self.canvas.move(self.light_circle, -40, 0)
            self.canvas.itemconfig(self.light_circle, fill=self.colour)
        elif self.position == 4:  # right
            self.canvas.move(self.light_circle, 40, 0)
            self.canvas.itemconfig(self.light_circle, fill=self.colour)

    def create(self, top, bottom, left, right):
        self.light_circle = self.canvas.create_oval(top, bottom, left, right, fill=self.colour)

    def change_colour(self):
        if self.colour == 'red':
            self.turn_green()
        else:
            self.turn_red()