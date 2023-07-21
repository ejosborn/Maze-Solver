from tkinter import Tk, BOTH, Canvas

# graphics.py contains three classes:

# Window class - This class creates the canvas, updates the canvas, keeps the program open and finally closes the program

# Point class - This class initalizes the Point class so it can be used to draw a line from Point1 to Point 2

# Line calls - This class draws a line from Point1 to Point2


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    # this method updates the canvas
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # this method keeps the program open until the user exits out of the canvas
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")

    # this method draws a line on the canvas
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    # this method closes the program
    def close(self):
        self.__is_running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
