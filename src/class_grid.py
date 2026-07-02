
class Grid:
    # Create grid with 10*20 filled with dots
    def __init__(self, rows = 10, cols = 20):
        self.rows = rows
        self.cols = cols
        self.grid = []

        # gird filled with dots
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(".")
            self.grid.append(row)

    # create walls #
    def add_walls(self):
        # Top border
        for c in range(self.cols):
            self.grid[0][c] = "#"

        # Bottom border
        for c in range(self.cols):
            self.grid[self.rows - 1][c] = "#"

        # Left border
        for r in range(self.rows):
            self.grid[r][0] = "#"

        # Right border
        for r in range(self.rows):
            self.grid[r][self.cols - 1] = "#"

    # print the grid
    def print_grid(self):
        for row in self.grid:
            print("".join(row))

    # get the grid
    def get_grid(self):
        return self.grid

    # add the fruit
    def add_fruit(self, row, col):
        # Only place fruit if it's not a wall
        if self.grid[row][col] == ".":
            self.grid[row][col] = "F"

    # add the lava
    def add_lava(self, row, col):
        if self.grid[row][col] == ".":
            self.grid[row][col] = "L"


    # add the trap
    def add_trap(self, row, col):
        if self.grid[row][col] == ".":
            self.grid[row][col] = "T"

    # add a shovel
    def add_shovel(self, row, col):
        if self.grid[row][col] == ".":
            self.grid[row][col] = "S"
