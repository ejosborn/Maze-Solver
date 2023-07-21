from graphics import Line, Point


# cell.py initalizes and draws cells based on the number of columns and rows.
# It then goes cell by cell and draws the move from cell1 to cell2


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    # this method gets the x/y coordinates of two points to draw the cell
    # itself and checks if the cell is missing any walls or not
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # each if checks if the cell has the wall, else will draw a white
        # line for that wall for it to look open
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    # this method draws the move from self.cell to the next cell
    def draw_move(self, next_cell, undo=False):
        if self._win is None:
            return
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2

        next_x_mid = (next_cell._x1 + next_cell._x2) / 2
        next_y_mid = (next_cell._y1 + next_cell._y2) / 2

        fill_color = "red"

        # this is to show that the line leads to a dead end
        if undo:
            fill_color = "gray"

        # these if statements will draw a line from middle of self to end of self
        # and then end of self to middle of the next cell

        # move left
        if self._x1 > next_cell._x1:
            line = Line(Point(self._x1, center_y), Point(center_x, center_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(next_x_mid, next_y_mid), Point(next_cell._x2, next_y_mid))
            self._win.draw_line(line, fill_color)

        # move right
        elif self._x1 < next_cell._x1:
            line = Line(Point(center_x, center_y), Point(self._x2, center_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(next_cell._x1, next_y_mid), Point(next_x_mid, next_y_mid))
            self._win.draw_line(line, fill_color)

        # move up
        elif self._y1 > next_cell._y1:
            line = Line(Point(center_x, center_y), Point(center_x, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(next_x_mid, next_cell._y2), Point(next_x_mid, next_y_mid))
            self._win.draw_line(line, fill_color)

        # move down
        elif self._y1 < next_cell._y1:
            line = Line(Point(center_x, center_y), Point(center_x, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(next_x_mid, next_y_mid), Point(next_x_mid, next_cell._y1))
            self._win.draw_line(line, fill_color)
