from tkinter import Tk, BOTH, Canvas


class Window:
    # setting init constructor
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas(self.__root, bg="White", win_width=width, win_height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # redraws all graphics in the window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # if program is running, this method keeps updating the graphics
    def wait_for_close(self):
        self.__is_running = True
        while self.is_running:
            self.redraw()
        print("Maze Solver Ended")

    # closes the window and ends program
    def close(self):
        self.__is_running = False
