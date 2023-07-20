from cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self._x = x1
        self._y = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window

        self._cells = []
        self._create_cells()

    # starts forming the matrix
    def _create_cells(self):
        # creates cells
        for col in range(self._num_cols):
            column_cells = []
            for row in range(self._num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)

        # draws each cell giving x/y coordinate
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cells(col, row)

    # drawing each cell
    def _draw_cells(self, i, j):
        if self._win is None:
            return
        x1 = self._x + i * self._cell_size_x
        y1 = self._y + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    # updates the window so we can see the cells being made
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
