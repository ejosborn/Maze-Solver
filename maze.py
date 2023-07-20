from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None,
    ):
        self._x = x1
        self._y = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window

        if seed:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    # updates the window so we can see the cells being made
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # removing top wall for start
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)

        # removing bottom wall for exit
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cells(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            possible_dir = 0

            # finds which cells to go to next
            # go left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
                possible_dir += 1

            # go right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
                possible_dir += 1

            # go up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
                possible_dir += 1

            # go right
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
                possible_dir += 1

            # if all out of possible directions, return
            if possible_dir == 0:
                self._draw_cells(i, j)
                return

            # chooses next direction to go
            dir = random.randrange(possible_dir)
            next_dir = to_visit[dir]

            # knock walls out between cells
            # right wall
            if next_dir[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left wall
            if next_dir[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # bottom wall
            if next_dir[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # top wall
            if next_dir[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively calls to visit next cell
            self._break_walls_r(next_dir[0], next_dir[1])

    # resets visited property for solving
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        
