# import tkinter as tk
# import math
# import time
#
#
# class AnalogClock:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Analog Clock")
#         self.canvas = tk.Canvas(root, bg="white")
#         self.canvas.pack(expand=True, fill="both")
#
#         self.draw_clock()
#         self.update_clock()
#
#     def draw_clock(self):
#         width = self.root.winfo_width()
#         height = self.root.winfo_height()
#         min_size = min(width, height)
#         center_x = width / 2
#         center_y = height / 2
#         radius = min_size / 2 - 10
#
#         self.canvas.delete("all")
#         self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
#                                 outline="black", width=2)
#         for i in range(1, 13):
#             angle = math.radians(i * 30 - 90)
#             x = center_x + (radius - 20) * math.cos(angle)
#             y = center_y + (radius - 20) * math.sin(angle)
#             self.canvas.create_text(x, y, text=str(i), font=("Arial", int(min_size / 25)), fill="black")
#
#         self.hour_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius / 2,
#                                                  width=int(min_size / 50), fill="black")
#         self.minute_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius * 0.7,
#                                                    width=int(min_size / 75), fill="black")
#         self.second_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius * 0.8,
#                                                    width=int(min_size / 100), fill="red")
#
#     def update_clock(self):
#         width = self.root.winfo_width()
#         height = self.root.winfo_height()
#         min_size = min(width, height)
#         center_x = width / 2
#         center_y = height / 2
#         radius = min_size / 2 - 10
#
#         current_time = time.localtime()
#         hour = current_time.tm_hour % 12
#         minute = current_time.tm_min
#         second = current_time.tm_sec
#
#         hour_angle = math.radians((hour + minute / 60) * 30 - 90)
#         minute_angle = math.radians((minute + second / 60) * 6 - 90)
#         second_angle = math.radians(second * 6 - 90)
#
#         self.canvas.coords(self.hour_hand, center_x, center_y, center_x + (radius / 2) * math.cos(hour_angle),
#                            center_y + (radius / 2) * math.sin(hour_angle))
#         self.canvas.coords(self.minute_hand, center_x, center_y, center_x + (radius * 0.7) * math.cos(minute_angle),
#                            center_y + (radius * 0.7) * math.sin(minute_angle))
#         self.canvas.coords(self.second_hand, center_x, center_y, center_x + (radius * 0.8) * math.cos(second_angle),
#                            center_y + (radius * 0.8) * math.sin(second_angle))
#
#         self.root.after(1000, self.update_clock)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     analog_clock = AnalogClock(root)
#
#
#     def on_resize(event):
#         analog_clock.draw_clock()
#
#
#     root.bind("<Configure>", on_resize)
#
#     root.mainloop()


# import math
# import time
# import tkinter as tk
#
#
# class AnalogClock:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Analog Clock")
#         self.canvas = tk.Canvas(root, bg="white")
#         self.canvas.pack(expand=True, fill="both")
#
#         self.draw_clock()
#         self.update_clock()
#
#     def draw_clock(self):
#         width = self.root.winfo_width()
#         height = self.root.winfo_height()
#         min_size = min(width, height)
#         center_x = width / 2
#         center_y = height / 2
#         radius = min_size / 2 - 10
#
#         self.canvas.delete("all")
#         self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
#                                 outline="black", width=4, fill="white")
#
#         for i in range(1, 13):
#             angle = math.radians(i * 30 - 90)
#             x = center_x + (radius - 40) * math.cos(angle)
#             y = center_y + (radius - 40) * math.sin(angle)
#             self.canvas.create_text(x, y, text=str(i), font=("Arial", int(min_size / 25)), fill="black")
#
#         self.hour_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius / 2,
#                                                  width=int(min_size / 25), fill="black")
#         self.minute_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius * 0.7,
#                                                    width=int(min_size / 50), fill="black")
#         self.second_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius * 0.8,
#                                                    width=int(min_size / 75), fill="red")
#
#     def update_clock(self):
#         width = self.root.winfo_width()
#         height = self.root.winfo_height()
#         min_size = min(width, height)
#         center_x = width / 2
#         center_y = height / 2
#         radius = min_size / 2 - 10
#
#         current_time = time.localtime()
#         hour = current_time.tm_hour % 12
#         minute = current_time.tm_min
#         second = current_time.tm_sec
#
#         hour_angle = math.radians((hour + minute / 60) * 30 - 90)
#         minute_angle = math.radians((minute + second / 60) * 6 - 90)
#         second_angle = math.radians(second * 6 - 90)
#
#         self.canvas.coords(self.hour_hand, center_x, center_y, center_x + (radius / 2) * math.cos(hour_angle),
#                            center_y + (radius / 2) * math.sin(hour_angle))
#         self.canvas.coords(self.minute_hand, center_x, center_y, center_x + (radius * 0.7) * math.cos(minute_angle),
#                            center_y + (radius * 0.7) * math.sin(minute_angle))
#         self.canvas.coords(self.second_hand, center_x, center_y, center_x + (radius * 0.8) * math.cos(second_angle),
#                            center_y + (radius * 0.8) * math.sin(second_angle))
#
#         self.root.after(1000, self.update_clock)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     analog_clock = AnalogClock(root)
#
#
#     def on_resize(event):
#         analog_clock.draw_clock()
#
#
#     root.bind("<Configure>", on_resize)
#
#     root.mainloop()


import math
import time
import tkinter as tk


class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(expand=True, fill="both")

        self.draw_clock()
        self.update_clock()

    def draw_clock(self):
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        min_size = min(width, height)
        center_x = width / 2
        center_y = height / 2
        radius = min_size / 2 - 10

        self.canvas.delete("all")
        self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                                outline="black", width=4, fill="white")
        self.canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="black")

        self.hour_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius / 2,
                                                 width=int(min_size / 40), fill="black")
        self.minute_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius * 0.7,
                                                   width=int(min_size / 60), fill="black")
        self.second_hand = self.canvas.create_line(center_x, center_y, center_x, center_y - radius * 0.8,
                                                   width=int(min_size / 100), fill="red")

    def update_clock(self):
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        min_size = min(width, height)
        center_x = width / 2
        center_y = height / 2
        radius = min_size / 2 - 10

        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

        hour_angle = math.radians((hour + minute / 60) * 30 - 90)
        minute_angle = math.radians((minute + second / 60) * 6 - 90)
        second_angle = math.radians(second * 6 - 90)

        self.canvas.coords(self.hour_hand, center_x, center_y, center_x + (radius / 2) * math.cos(hour_angle),
                           center_y + (radius / 2) * math.sin(hour_angle))
        self.canvas.coords(self.minute_hand, center_x, center_y, center_x + (radius * 0.7) * math.cos(minute_angle),
                           center_y + (radius * 0.7) * math.sin(minute_angle))
        self.canvas.coords(self.second_hand, center_x, center_y, center_x + (radius * 0.8) * math.cos(second_angle),
                           center_y + (radius * 0.8) * math.sin(second_angle))

        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    analog_clock = AnalogClock(root)


    def on_resize(event):
        analog_clock.draw_clock()


    root.bind("<Configure>", on_resize)

    root.mainloop()
