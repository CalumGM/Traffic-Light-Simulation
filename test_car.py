import tkinter as tk
from Car import Car
from random import randint, choice
import threading


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
    create_car()
    create_car()
    create_car()


def create_car():
    position = randint(1, 4)
    is_turning = choice([True, False])
    colour = choice(['red', 'blue', 'black', 'green'])
    car_positions.append(position)
    car = Car(c, position, is_turning, colour)
    print(car)


cars = []  # define car array
car_positions = []

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

window.mainloop()
