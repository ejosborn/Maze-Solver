from graphics import Line, Point


class Cell:
    def __init__(self, window):
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

        # drawing walls
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    # this method draws the actual line from cell to cell
    def draw_move(self, next_cell, undo=False):
        self_center_x = (self._x1 + self._x2) / 2
        self_center_y = (self._y1 + self._y2) / 2
        next_center_x = (next_cell._x1 + next_cell._x2) / 2
        next_center_y = (next_cell._y1 + next_cell._y2) / 2
        if undo:
            # make fill color gray
            # to draw line up
            if not self.has_top_wall and not next_cell.has_bottom_wall:
                line = Line(
                    Point(self_center_x, self_center_y),
                    Point(next_center_x, next_center_y),
                )
                self._win.draw_line(line, "gray")

            # to draw line down
            if not self.has_bottom_wall and not next_cell.has_top_wall:
                line = Line(
                    Point(self_center_x, self_center_y),
                    Point(next_center_x, next_center_y),
                )
                self._win.draw_line(line, "gray")

            # to draw line left
            if not self.has_left_wall and not next_cell.has_right_wall:
                line = Line(
                    Point(self_center_x, self_center_y),
                    Point(next_center_x, next_center_y),
                )
                self._win.draw_line(line, "gray")

            # to draw line right
            if not self.has_right_wall and not next_cell.has_left_wall:
                line = Line(
                    Point(self_center_x, self_center_y),
                    Point(next_center_x, next_center_y),
                )
                self._win.draw_line(line, "gray")

        else:
            # make fill color red
            # to draw line up
            if not self.has_top_wall and not next_cell.has_bottom_wall:
                line = Line(
                    Point(self_center_x, self_center_y),
                    Point(next_center_x, next_center_y),
                )
                self._win.draw_line(line, "red")

            # to draw line down
            if not self.has_bottom_wall and not next_cell.has_top_wall:
                line = Line(
                    Point(self_center_x, self_center_y),
                    Point(next_center_x, next_center_y),
                )
                self._win.draw_line(line, "red")

            # to draw line left
            if not self.has_left_wall and not next_cell.has_right_wall:
                line = Line(
                    Point(self_center_x, self_center_y),
                    Point(next_center_x, next_center_y),
                )
                self._win.draw_line(line, "red")

            # to draw line right
            if not self.has_right_wall and not next_cell.has_left_wall:
                line = Line(
                    Point(self_center_x, self_center_y),
                    Point(next_center_x, next_center_y),
                )
                self._win.draw_line(line, "red")
