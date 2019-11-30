# -----------------------
# ---import tkinter---
import tkinter as tk
from random import randint
import time
import threading
import sys
from Car import Car

STEP_DISTANCE = 2
STEP_TIME = 0.01


def exit_program():
    sys.exit()


def create_grid(event):
    w = c.winfo_width()  # Get current width of canvas
    h = c.winfo_height()  # Get current height of canvas
    '''
    # Create all vertical lines at intervals of 100
    for i in range(0, w, 50):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Create all horizontal lines at intervals of 100
    for i in range(0, h, 50):
        c.create_line([(0, i), (w, i)], tag='grid_line')
    '''
    # line(w1, h1, w2, h2)
    c.create_line(w / 2 - 50, 0, w / 2 - 50, h / 2 - 50, fill="black", width=5)
    c.create_line(w / 2 + 50, 0, w / 2 + 50, h / 2 - 50, fill="black", width=5)

    c.create_line(w / 2 - 50, h / 2 + 50, w / 2 - 50, h, fill="black", width=5)
    c.create_line(w / 2 + 50, h / 2 + 50, w / 2 + 50, h, fill="black", width=5)

    c.create_line(0, h / 2 + 50, w / 2 - 50, h / 2 + 50, fill="black", width=5)
    c.create_line(w / 2 + 50, h / 2 + 50, w, h / 2 + 50, fill="black", width=5)

    c.create_line(0, h / 2 - 50, w / 2 - 50, h / 2 - 50, fill="black", width=5)
    c.create_line(w / 2 + 50, h / 2 - 50, w, h / 2 - 50, fill="black", width=5)

    c.create_rectangle(w / 2 + 60, h / 2 - 60, w / 2 + 80, h / 2 - 110)


# Create GUI


window = tk.Tk()

c = tk.Canvas(window, height=600, width=600, bg='white')
c.pack(fill=tk.BOTH, expand=True)

f = tk.Frame(window)
f.pack()
window.title("Traffic Light Simulation")

# The 'configure' event is triggered when the window's size is changed
# It sends a new height and width to the function
c.bind('<Configure>', create_grid)
print("loaded GUI")

# ---Main---


# first research how threading works, then define function that randomly generates cars with various paths
# Car attributes = speed, turing (true/false, if true: left/right)
# Traffic lights: design sprites, define main road, timer to change, only activate if a car is waiting

cars = []  # define car array
car_positions = []


def create_car():
    w = c.winfo_width()  # Get current width of canvas
    h = c.winfo_height()  # Get current height of canvas
    #  car = Car(car_position, turning, colour)
    #  cars.append(car)
    #  not sure how to let the class know about tk
    car_position = randint(1, 4)
    car_positions.append(car_position)
    if car_position == 1:
        print("Made Top Car")
        # Create Top Car
        car = c.create_rectangle(w / 2 + 40, 0, w / 2 + 10, 80, fill="blue")
        cars.append(car)
        return car_positions
    elif car_position == 2:
        print("Made Bottom Car")
        # Create Bottom Car
        car = c.create_rectangle(w / 2 - 40, h, w / 2 - 10, h - 80, fill="blue")
        cars.append(car)
        return car_positions
    elif car_position == 3:
        print("Made Left Car")
        # Create Left Car
        car = c.create_rectangle(0, h / 2 - 10, 80, h / 2 - 40, fill="blue")
        cars.append(car)
        return car_positions
    elif car_position == 4:
        print("Made Right Car")
        # Create Right Car
        car = c.create_rectangle(w, h / 2 + 10, w - 80, h / 2 + 40, fill="blue")
        cars.append(car)
        return car_positions
    # make the cars be added into an array of cars (this will make it easier to move them later on)
    # then give them instructions like turning left/right
    print(cars)


def simulation_loop():
    w = c.winfo_width()  # Get current width of canvas
    h = c.winfo_height()  # Get current height of canvas
    while True:
        time.sleep(STEP_TIME)
        for i in range(len(cars)):  # Pick path for cars to go on
            if car_positions[i] == 1:  # top
                if c.coords(cars[i])[3] == h / 2 - 50:
                    pass
                else:
                    c.move(cars[i], 0, STEP_DISTANCE)
            elif car_positions[i] == 2:  # bottom
                if c.coords(cars[i])[1] == h / 2 + 50:
                    pass
                else:
                    c.move(cars[i], 0, -STEP_DISTANCE)
            elif car_positions[i] == 3:  # left
                c.move(cars[i], STEP_DISTANCE, 0)
            elif car_positions[i] == 4:  # right
                c.move(cars[i], -STEP_DISTANCE, 0)


threading.Thread(target=simulation_loop, name="simulationThread", args=()).start()
# threading.Thread(target=create_car, name="carThread", args=()).start()


exitButton = tk.Button(f, text="EXIT", fg='red', command=exit_program)
exitButton.pack(side=tk.LEFT)
carButton = tk.Button(f, text="Create New Car", fg='red', command=create_car)
carButton.pack(side=tk.RIGHT)

window.mainloop()
