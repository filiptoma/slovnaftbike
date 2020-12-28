import tkinter as tk
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Slovnaft Bike Visualization')

        # width and height are same as dimensions of map.PNG
        self.width = 1183
        self.height = 739
        self.canvas = tk.Canvas(width=self.width, height=self.height)
        self.canvas.pack()

        self.img = ImageTk.PhotoImage(Image.open('map.PNG'))
        self.render_image()

        self.radius = 5
        self.render_bike_locations()

    def render_image(self):
        self.canvas.create_image(0, 0, anchor='nw', image=self.img)

    def render_bike_locations(self):
        # calculating map points scaling
        x_diff = 17.314956 - 16.951199
        y_diff = 48.240728 - 48.089077

        x_scale = x_diff / self.width
        y_scale = y_diff / self.height

        with open('dataset.csv', 'r', encoding='windows-1250') as data:
            while True:
                line = data.readline()
                if not line:
                    break
                line = line.strip().split(';')
                if line[0] != 'ID stanice':
                    lat = float(line[2])
                    lon = float(line[3])

                    # calculating position of bike on canvas
                    x = (lon - 16.951199) / x_scale
                    y = (lat - 48.089077) / y_scale

                    self.canvas.create_oval(
                        x + self.radius,
                        self.height - (y + self.radius),
                        x - self.radius,
                        self.height - (y - self.radius),
                        fill='red'
                    )

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    App().run()
