# -----------------------
# ---import tkinter---
import tkinter as tk
from random import randint, choice
import time
import threading
import sys
from Car import Car

STEP_DISTANCE = 2
STEP_TIME = 0.01
BREAK_THREAD = False


def exit_program():
    global BREAK_THREAD
    BREAK_THREAD = True
    sys.exit()


def create_grid(event):
    w = canvas.winfo_width()  # Get current width of canvas
    h = canvas.winfo_height()  # Get current height of canvas
    '''
    # Create all vertical lines at intervals of 100
    for i in range(0, w, 50):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Create all horizontal lines at intervals of 100
    for i in range(0, h, 50):
        c.create_line([(0, i), (w, i)], tag='grid_line')
    '''
    # line(w1, h1, w2, h2)
    canvas.create_line(w / 2 - 50, 0, w / 2 - 50, h / 2 - 50, fill="black", width=5)
    canvas.create_line(w / 2 + 50, 0, w / 2 + 50, h / 2 - 50, fill="black", width=5)

    canvas.create_line(w / 2 - 50, h / 2 + 50, w / 2 - 50, h, fill="black", width=5)
    canvas.create_line(w / 2 + 50, h / 2 + 50, w / 2 + 50, h, fill="black", width=5)

    canvas.create_line(0, h / 2 + 50, w / 2 - 50, h / 2 + 50, fill="black", width=5)
    canvas.create_line(w / 2 + 50, h / 2 + 50, w, h / 2 + 50, fill="black", width=5)

    canvas.create_line(0, h / 2 - 50, w / 2 - 50, h / 2 - 50, fill="black", width=5)
    canvas.create_line(w / 2 + 50, h / 2 - 50, w, h / 2 - 50, fill="black", width=5)

    canvas.create_rectangle(w / 2 + 60, h / 2 - 60, w / 2 + 80, h / 2 - 110)


# Create GUI


window = tk.Tk()

canvas = tk.Canvas(window, height=600, width=600, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

f = tk.Frame(window)
f.pack()
window.title("Traffic Light Simulation")

# The 'configure' event is triggered when the window's size is changed
# It sends a new height and width to the function
canvas.bind('<Configure>', create_grid)
print("loaded GUI")

# ---Main---

# Car attributes = speed, turing (true/false, if true: left/right)
# Traffic lights: design sprites, define main road, timer to change, only activate if a car is waiting

cars = []  # define car array


def create_car():
    position = randint(1, 4)
    is_turning = choice([True, False])
    colour = choice(['red', 'blue', 'black', 'green'])
    car = Car(canvas, position, is_turning, colour)
    car.create(cars)
    cars.append(car)


def simulation_loop():
    w = canvas.winfo_width()  # Get current width of canvas
    h = canvas.winfo_height()  # Get current height of canvas

    while not BREAK_THREAD:
        time.sleep(STEP_TIME)
        for i in range(len(cars)):  # iterate through all the cars and move them accordingly
            if cars[i].position == 1:  # top
                # stop at the 'lights'
                if cars[i].colliding(cars):
                    cars[i].move_backward(STEP_DISTANCE)
                else:
                    cars[i].move_forward(STEP_DISTANCE)
            elif cars[i].position == 2:  # bottom
                if cars[i].colliding(cars):
                    cars[i].move_backward(cars)
                else:
                    cars[i].move_forward(STEP_DISTANCE)
            elif cars[i].position == 3:  # left
                if cars[i].colliding(cars):
                    cars[i].move_backward(cars)
                else:
                    cars[i].move_forward(STEP_DISTANCE)
            elif cars[i].position == 4:  # right
                if cars[i].colliding(cars):
                    cars[i].move_backward(cars)
                else:
                    cars[i].move_forward(STEP_DISTANCE)


threading.Thread(target=simulation_loop, name="simulationThread", args=()).start()
# threading.Thread(target=create_car, name="carThread", args=()).start()


exitButton = tk.Button(f, text="EXIT", fg='red', command=exit_program)
exitButton.pack(side=tk.LEFT)
carButton = tk.Button(f, text="Create New Car", fg='red', command=create_car)
carButton.pack(side=tk.RIGHT)

window.mainloop()
