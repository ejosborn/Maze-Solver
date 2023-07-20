from graphics import Line, Point


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    # this method draws the cell shape
    def draw(self, x1, y1, x2, y2):
        # getting x/y coord of top left and bottom right coordinate
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        # drawing wallsiko7[]
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

    # this method draws the actual line from cell to cell
    def draw_move(self, next_cell, undo=False):
        self_center_x = (self._x1 + self._x2) / 2
        self_center_y = (self._y1 + self._y2) / 2
        next_center_x = (next_cell._x1 + next_cell._x2) / 2
        next_center_y = (next_cell._y1 + next_cell._y2) / 2
        fill_color = "red"

        if undo:
            fill_color = "gray"

        # to draw line up
        if self._y1 < next_cell._y1:
            line = Line(
                Point(self_center_x, self_center_y),
                Point(next_center_x, self._y1),
            )
            self._win.draw_line(line, fill_color)
            line = Line(
                Point(next_center_x, next_cell._y2), Point(next_center_x, next_center_y)
            )
            self._win.draw_line(line, fill_color)

        # to draw line down
        if self._y1 > next_cell._y1:
            line = Line(
                Point(self_center_x, self_center_y),
                Point(next_center_x, next_cell._y2),
            )

            self._win.draw_line(line, fill_color)
            line = Line(
                Point(next_center_x, next_center_y), Point(next_center_x, next_cell._y1)
            )
            self._win.draw_line(line, fill_color)

        # to draw line left
        if self._x1 > next_cell._x1:
            line = Line(
                Point(self._x1, self_center_y),
                Point(next_center_x, next_center_y),
            )

            self._win.draw_line(line, fill_color)

            line = Line(
                Point(next_center_x, next_center_y), Point(next_cell._x2, next_center_y)
            )
            self._win.draw_line(line, fill_color)

        # to draw line right
        if self._x1 < next_cell._x1:
            line = Line(
                Point(self_center_x, self_center_y),
                Point(self._x2, next_center_y),
            )

            self._win.draw_line(line, fill_color)
            line = Line(
                Point(next_cell._x1, next_center_y), Point(next_center_x, next_center_y)
            )
            self._win.draw_line(line, fill_color)
