from random import randint

STEP_DISTANCE = 2


class Car:
    def __init__(self, canvas, position=1, is_turning=False, colour='blue'):
        self.canvas = canvas
        self.position = position
        self.is_turning = is_turning
        self.colour = colour
        self.car_rectangle = None

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
        if self.position == 1:  # Create Top Car
            car_rectangle = self.canvas.create_rectangle(w / 2 + 40, 0, w / 2 + 10, 80, fill=self.colour)
            self.car_rectangle = car_rectangle
        elif self.position == 2:
            # Create Bottom Car
            car_rectangle = self.canvas.create_rectangle(w / 2 - 40, h, w / 2 - 10, h - 80, fill=self.colour)
            self.car_rectangle = car_rectangle
        elif self.position == 3:
            # Create Left Car
            car_rectangle = self.canvas.create_rectangle(0, h / 2 - 10, 80, h / 2 - 40, fill=self.colour)
            self.car_rectangle = car_rectangle
        elif self.position == 4:
            # Create Right Car
            car_rectangle = self.canvas.create_rectangle(w, h / 2 + 10, w - 80, h / 2 + 40, fill=self.colour)
            self.car_rectangle = car_rectangle

    def move_forward(self, distance):
        w = self.canvas.winfo_width()  # Get current width of canvas
        h = self.canvas.winfo_height()  # Get current height of canvas
        if self.position == 1:  # top
            # if self.canvas.coords(self.car_rectangle)[3] == h / 2 - 50:  # stop at the 'lights'
            #    pass
            # else:
            self.canvas.move(self.car_rectangle, 0, STEP_DISTANCE)
        elif self.position == 2:  # bottom
            # if self.canvas.coords(self.car_rectangle)[1] == h / 2 + 50:
            #    pass
            # else:
            self.canvas.move(self.car_rectangle, 0, -STEP_DISTANCE)
        elif self.position == 3:  # left
            self.canvas.move(self.car_rectangle, STEP_DISTANCE, 0)
        elif self.position == 4:  # right
            self.canvas.move(self.car_rectangle, -STEP_DISTANCE, 0)

    def move_backward(self, distance):
        w = self.canvas.winfo_width()  # Get current width of canvas
        h = self.canvas.winfo_height()  # Get current height of canvas
        if self.position == 1:  # top
            # if self.canvas.coords(self.car_rectangle)[3] == h / 2 - 50:  # stop at the 'lights'
            #    pass
            # else:
            self.canvas.move(self.car_rectangle, 0, -STEP_DISTANCE)
        elif self.position == 2:  # bottom
            # if self.canvas.coords(self.car_rectangle)[1] == h / 2 + 50:
            #    pass
            # else:
            self.canvas.move(self.car_rectangle, 0, STEP_DISTANCE)
        elif self.position == 3:  # left
            self.canvas.move(self.car_rectangle, -STEP_DISTANCE, 0)
        elif self.position == 4:  # right
            self.canvas.move(self.car_rectangle, STEP_DISTANCE, 0)

    def colliding(self, front_car):
        if self.position == 1:  # top
            if (self.canvas.coords(self.car_rectangle)[3] >= (self.canvas.coords(front_car.car_rectangle)[1] -
                                                              20)) and id(self) != id(front_car):
                return True
        elif self.position == 2:  # bottom
            if (self.canvas.coords(self.car_rectangle)[1] <= (self.canvas.coords(front_car.car_rectangle)[3] +
                                                              20)) and id(self) != id(front_car):
                return True
        elif self.position == 3:  # left
            if (self.canvas.coords(self.car_rectangle)[2] >= (self.canvas.coords(front_car.car_rectangle)[0] -
                                                              20)) and id(self) != id(front_car):
                return True
        elif self.position == 4:  # right
            if (self.canvas.coords(self.car_rectangle)[0] <= (self.canvas.coords(front_car.car_rectangle)[2] +
                                                              20)) and id(self) != id(front_car):
                return True

    def delete_redundant_cars(self):
        w = self.canvas.winfo_width()  # Get current width of canvas
        h = self.canvas.winfo_height()  # Get current height of canvas
        if self.position == 1 and self.canvas.coords(self.car_rectangle)[1] > h:  # top
            return self
        elif self.position == 2 and self.canvas.coords(self.car_rectangle)[3] > 0:  # bottom
            return self
        elif self.position == 3 and self.canvas.coords(self.car_rectangle)[0] > w:  # left
            return self
        elif self.position == 4 and self.canvas.coords(self.car_rectangle)[2] > 0:  # right
            return self
