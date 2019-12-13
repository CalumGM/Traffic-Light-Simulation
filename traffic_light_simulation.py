# -----------------------
# ---import tkinter---
import tkinter as tk
from random import randint, choice
import time
import threading
import sys
from Car import Car
from TrafficLight import TrafficLight

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

    # top light
    canvas.create_rectangle(w / 2 + 60, h / 2 - 60, w / 2 + 80, h / 2 - 120)
    canvas.create_oval(w / 2 + 61, h / 2 - 101, w / 2 + 79, h / 2 - 119)
    canvas.create_oval(w / 2 + 61, h / 2 - 81, w / 2 + 79, h / 2 - 99)
    canvas.create_oval(w / 2 + 61, h / 2 - 61, w / 2 + 79, h / 2 - 79)

    # bottom light
    canvas.create_rectangle(w / 2 - 60, h / 2 + 60, w / 2 - 80, h / 2 + 120)
    canvas.create_oval(w / 2 - 61, h / 2 + 101, w / 2 - 79, h / 2 + 119)
    canvas.create_oval(w / 2 - 61, h / 2 + 81, w / 2 - 79, h / 2 + 99)
    canvas.create_oval(w / 2 - 61, h / 2 + 61, w / 2 - 79, h / 2 + 79)

    # left light
    canvas.create_rectangle(w / 2 - 60, w / 2 - 80, h / 2 - 120, h / 2 - 60)
    canvas.create_oval(w / 2 - 61, h / 2 - 79, w / 2 - 79, h / 2 - 61)
    canvas.create_oval(w / 2 - 81, h / 2 - 79, w / 2 - 99, h / 2 - 61)
    canvas.create_oval(w / 2 - 101, h / 2 - 79, w / 2 - 119, h / 2 - 61)

    canvas.create_rectangle(w / 2 + 60, h / 2 + 60, w / 2 + 120, h / 2 + 80)  # right
    canvas.create_oval(w / 2 + 61, h / 2 + 79, w / 2 + 79, h / 2 + 61)
    canvas.create_oval(w / 2 + 81, h / 2 + 79, w / 2 + 99, h / 2 + 61)
    canvas.create_oval(w / 2 + 101, h / 2 + 79, w / 2 + 119, h / 2 + 61)
    # create circles for the lights, make 3, but just use red and green for testing

    # lights = top, bottom, left, right
    lights.append(TrafficLight(canvas, 1, 'green'))
    lights.append(TrafficLight(canvas, 2, 'green'))
    lights.append(TrafficLight(canvas, 3, 'red'))
    lights.append(TrafficLight(canvas, 4, 'red'))

    lights[0].create(w / 2 + 61, h / 2 - 101, w / 2 + 79, h / 2 - 119)
    lights[1].create(w / 2 - 61, h / 2 + 101, w / 2 - 79, h / 2 + 119)
    lights[2].create(w / 2 - 61, h / 2 - 79, w / 2 - 79, h / 2 - 61)
    lights[3].create(w / 2 + 61, h / 2 + 79, w / 2 + 79, h / 2 + 61)

    '''
    lights[0].turn_red()
    lights[1].turn_red()
    lights[2].turn_green()
    lights[3].turn_green()
    '''


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

# Traffic lights: design sprites, define main road, timer to change, only activate if a car is waiting

cars = []  # all car objects are stored in this list
lights = []  # all light objects are stored in this list


def create_car():
    position = randint(1, 4)
    is_turning = choice([True, False])
    colour = choice(['red', 'blue', 'black', 'green'])
    car = Car(canvas, position, is_turning, colour)
    car.create(cars)
    cars.append(car)


def change_lights():
    for light in lights:
        light.change_colour()


def simulation_loop():
    w = canvas.winfo_width()  # Get current width of canvas
    h = canvas.winfo_height()  # Get current height of canvas

    while not BREAK_THREAD:
        time.sleep(STEP_TIME)
        for i in range(len(cars)):  # iterate through all the cars and move them accordingly
            delete_car = cars[i].delete_redundant_cars()
            del delete_car
            if cars[i].position == 1 and lights[0].colour == 'green' and canvas.coords(cars[i].car_rectangle)[0] != h / 2 - 50:  # top
                front_cars = [car for car in cars if car.position == 1 and cars.index(car) < cars.index(cars[i])]
                try:
                    front_car = front_cars[-1]
                    if cars[i].colliding(front_car):
                        cars[i].move_backward(STEP_DISTANCE)
                    else:
                        cars[i].move_forward(STEP_DISTANCE)
                except IndexError:
                    cars[i].move_forward(STEP_DISTANCE)
            elif cars[i].position == 2 and lights[1].colour == 'green' and canvas.coords(cars[i].car_rectangle)[2] != h / 2 + 50:  # bottom
                front_cars = [car for car in cars if car.position == 2 and cars.index(car) < cars.index(cars[i])]
                try:
                    front_car = front_cars[-1]
                    if cars[i].colliding(front_car):
                        cars[i].move_backward(cars)
                    else:
                        cars[i].move_forward(STEP_DISTANCE)
                except IndexError:
                    cars[i].move_forward(STEP_DISTANCE)
            elif cars[i].position == 3 and lights[2].colour == 'green' and canvas.coords(cars[i].car_rectangle)[1] != w / 2 - 50:
                front_cars = [car for car in cars if car.position == 3 and cars.index(car) < cars.index(cars[i])]
                try:
                    front_car = front_cars[-1]
                    if cars[i].colliding(front_car):
                        cars[i].move_backward(cars)
                    else:
                        cars[i].move_forward(STEP_DISTANCE)
                except IndexError:
                    cars[i].move_forward(STEP_DISTANCE)
            elif cars[i].position == 4 and lights[3].colour == 'green' and canvas.coords(cars[i].car_rectangle)[3] != w / 2 + 50:  # right
                front_cars = [car for car in cars if car.position == 4 and cars.index(car) < cars.index(cars[i])]
                try:
                    front_car = front_cars[-1]
                    if cars[i].colliding(front_car):
                        cars[i].move_backward(cars)
                    else:
                        cars[i].move_forward(STEP_DISTANCE)
                except IndexError:
                    cars[i].move_forward(STEP_DISTANCE)


threading.Thread(target=simulation_loop, name="simulationThread", args=()).start()
# threading.Thread(target=create_car, name="carThread", args=()).start()

exitButton = tk.Button(f, text="EXIT", fg='red', command=exit_program)
exitButton.pack(side=tk.LEFT)
carButton = tk.Button(f, text="Create New Car", fg='red', command=create_car)
carButton.pack(side=tk.RIGHT)
lightsButton = tk.Button(f, text="Change Lights", fg='red', command=change_lights)
lightsButton.pack(side=tk.RIGHT)

window.mainloop()
