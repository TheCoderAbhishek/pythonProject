# CLOCK - 1

# import tkinter as tk
# from datetime import datetime
#
# def update_time():
#     current_time = datetime.now().strftime("%H:%M:%S")
#     clock_label.config(text=current_time)
#     clock_label.after(1000, update_time)
#
# root = tk.Tk()
# root.title("Python Clock")
#
# clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
# clock_label.pack(padx=20, pady=20)
#
# update_time()
#
# root.mainloop()


# CLOCK - 2

# import tkinter as tk
# import math
# from datetime import datetime
#
# def update_clock():
#     current_time = datetime.now()
#     hour = current_time.hour % 12
#     minute = current_time.minute
#     second = current_time.second
#
#     hour_angle = (hour * 30) + (minute * 0.5)
#     minute_angle = minute * 6
#     second_angle = second * 6
#
#     canvas.coords(hour_hand, *calc_hand_position(hour_angle, 50, 20))
#     canvas.coords(minute_hand, *calc_hand_position(minute_angle, 70, 10))
#     canvas.coords(second_hand, *calc_hand_position(second_angle, 80, 2))
#
#     root.after(1000, update_clock)
#
# def calc_hand_position(angle, length, width):
#     x = length * math.sin(math.radians(angle))
#     y = -length * math.cos(math.radians(angle))
#     return (150, 150, 150 + x, 150 + y)
#
# root = tk.Tk()
# root.title("Analog Clock")
#
# canvas = tk.Canvas(root, width=300, height=300, bg="black")
# canvas.pack()
#
# canvas.create_oval(50, 50, 250, 250, outline="white", width=4)
#
# for i in range(12):
#     angle = math.radians(i * 30)
#     x1 = 150 + 90 * math.sin(angle)
#     y1 = 150 - 90 * math.cos(angle)
#     x2 = 150 + 100 * math.sin(angle)
#     y2 = 150 - 100 * math.cos(angle)
#     canvas.create_line(x1, y1, x2, y2, fill="white", width=3)
#
# hour_hand = canvas.create_line(150, 150, 150, 100, fill="white", width=8)
# minute_hand = canvas.create_line(150, 150, 150, 70, fill="white", width=5)
# second_hand = canvas.create_line(150, 150, 150, 80, fill="red", width=2)
#
# update_clock()
#
# root.mainloop()


# CLOCK - 3

# import tkinter as tk
# from datetime import datetime
#
# def update_clock():
#     current_time = datetime.now().strftime("%H:%M:%S")
#     clock_label.config(text=current_time)
#     clock_label.after(1000, update_clock)
#     clock_label.config(fg=random_color())
#
# def random_color():
#     import random
#     r = lambda: random.randint(0,255)
#     return '#{:02x}{:02x}{:02x}'.format(r(),r(),r())
#
# root = tk.Tk()
# root.title("Digital Clock")
#
# clock_label = tk.Label(root, font=("Helvetica", 48))
# clock_label.pack(padx=20, pady=20)
#
# update_clock()
#
# root.mainloop()


# CLOCK - 4

# import tkinter as tk
# import time
#
# def update_clock():
#     current_time = time.strftime("%H:%M:%S")
#     clock_label.config(text=current_time)
#     root.after(1000, update_clock)
#
# def resize_font(event):
#     new_size = max(12, min(event.width // 6, event.height // 2))
#     clock_label.config(font=("Helvetica", new_size))
#
# root = tk.Tk()
# root.title("Responsive Digital Clock")
#
# clock_label = tk.Label(root, font=("Helvetica", 48))
# clock_label.pack(expand=True, fill=tk.BOTH)
#
# root.bind("<Configure>", resize_font)
#
# update_clock()
#
# root.mainloop()


# CLOCK - 5

# import tkinter as tk
# import math
# from datetime import datetime
#
# def update_clock():
#     current_time = datetime.now()
#     hour = current_time.hour % 12
#     minute = current_time.minute
#     second = current_time.second
#
#     hour_angle = (hour * 30) + (minute * 0.5)
#     minute_angle = minute * 6
#     second_angle = second * 6
#
#     canvas.coords(hour_hand, *calc_hand_position(hour_angle, 50, 20))
#     canvas.coords(minute_hand, *calc_hand_position(minute_angle, 70, 10))
#     canvas.coords(second_hand, *calc_hand_position(second_angle, 80, 2))
#
#     root.after(1000, update_clock)
#
#     current_datetime = current_time.strftime("%Y-%m-%d %H:%M:%S")
#     date_time_label.config(text=current_datetime)
#
# def calc_hand_position(angle, length, width):
#     x = length * math.sin(math.radians(angle))
#     y = -length * math.cos(math.radians(angle))
#     return (150, 150, 150 + x, 150 + y)
#
# root = tk.Tk()
# root.title("Analog Clock with Date and Time")
#
# canvas = tk.Canvas(root, width=300, height=300, bg="white")
# canvas.pack()
#
# canvas.create_oval(50, 50, 250, 250, outline="black", width=4)
#
# for i in range(12):
#     angle = math.radians(i * 30)
#     x1 = 150 + 90 * math.sin(angle)
#     y1 = 150 - 90 * math.cos(angle)
#     x2 = 150 + 100 * math.sin(angle)
#     y2 = 150 - 100 * math.cos(angle)
#     canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
#
# hour_hand = canvas.create_line(150, 150, 150, 100, fill="black", width=8)
# minute_hand = canvas.create_line(150, 150, 150, 70, fill="black", width=5)
# second_hand = canvas.create_line(150, 150, 150, 80, fill="red", width=2)
#
# date_time_label = tk.Label(root, font=("Helvetica", 14), fg="blue")
# date_time_label.pack()
#
# update_clock()
#
# root.mainloop()


# CLOCK - 6

import math
import tkinter as tk
from datetime import datetime


def update_clock():
    current_time = datetime.now()
    hour = current_time.hour % 12
    minute = current_time.minute
    second = current_time.second

    # Calculate the angles for hour, minute, and second hands
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6
    second_angle = second * 6

    # Update the position of the clock hands
    canvas.coords(hour_hand, *calc_hand_position(hour_angle, 40, 7))
    canvas.coords(minute_hand, *calc_hand_position(minute_angle, 60, 5))
    canvas.coords(second_hand, *calc_hand_position(second_angle, 70, 2))

    # Update the clock every 1000ms (1 second)
    root.after(1000, update_clock)


def calc_hand_position(angle, length, width):
    x = length * math.sin(math.radians(angle))
    y = -length * math.cos(math.radians(angle))
    return (150, 150, 150 + x, 150 + y)


# Create the main window
root = tk.Tk()
root.title("Analog Clock Variant")

# Create a canvas to draw the clock
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Draw the clock face
canvas.create_oval(50, 50, 250, 250, outline="black", width=4)

# Draw clock hands
hour_hand = canvas.create_line(150, 150, 150, 100, fill="black", width=7)
minute_hand = canvas.create_line(150, 150, 150, 70, fill="black", width=5)
second_hand = canvas.create_line(150, 150, 150, 80, fill="red", width=2)

# Run the update_clock function to start updating the clock
update_clock()

# Start the Tkinter event loop
root.mainloop()
