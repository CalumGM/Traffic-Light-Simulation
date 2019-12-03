from random import randint


class Car:
    def __init__(self, canvas, position=1, is_turning=False, colour='blue'):
        self.canvas = canvas
        self.position = position
        self.is_turning = is_turning
        self.colour = colour

    def __str__(self):
        return "Car at the {}, Turning: {}, Colour is {}".format(self.get_position(), self.is_turning, self.colour)

    def get_position(self):
        if self.position == 1:
            return "Top"
        elif self.position == 2:
            return "Bottom"
        elif self.position == 3:
            return "Left"
        elif self.position == 4:
            return "Right"

    def create(self, cars):
        w = self.canvas.winfo_width()  # Get current width of canvas
        h = self.canvas.winfo_height()  # Get current height of canvas
        if self.position == 1:
            print("Made Top Car")
            # Create Top Car
            car = self.canvas.create_rectangle(w / 2 + 40, 0, w / 2 + 10, 80, fill="blue")
            cars.append(car)
        elif self.position == 2:
            print("Made Bottom Car")
            # Create Bottom Car
            car = self.canvas.create_rectangle(w / 2 - 40, h, w / 2 - 10, h - 80, fill="blue")
            cars.append(car)
        elif self.position == 3:
            print("Made Left Car")
            # Create Left Car
            car = self.canvas.create_rectangle(0, h / 2 - 10, 80, h / 2 - 40, fill="blue")
            cars.append(car)
        elif self.position == 4:
            print("Made Right Car")
            # Create Right Car
            car = self.canvas.create_rectangle(w, h / 2 + 10, w - 80, h / 2 + 40, fill="blue")
            cars.append(car)
