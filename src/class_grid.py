
class Grid:
    # Create grid with 10*20 filled with dots
    def __init__(self, rows = 10, cols = 20):
        self.rows = rows
        self.cols = cols
        self.grid = [["." for c in range(cols)] for r in range(rows)]
        self.data = [["." for c in range(cols)] for r in range(rows)]

    # create walls #
    def add_walls(self):
        # Col wall
        for c in range(self.cols):
            self.data[0][c] = "#"
            self.data[self.rows - 1][c] = "#"

        # Row wall
        for r in range(self.rows):
            self.data[r][0] = "#"
            self.data[r][self.cols - 1] = "#"

        # New interior walls using for-loops
        # Custom horizontal wall
        for c in range(3, 5):
            self.data[3][c] = "#"

        # Custom vertical wall
        for r in range(5, 6):
            self.data[r][5] = "#"

    def add_shovels(self):
        # Shovel 1
        for c in range(2, 3):
            if self.data[6][c] == ".":
                self.data[6][c] = "S"

        # Shovel 2
        for r in range(3, 4):
            if self.data[r][14] == ".":
                self.data[r][14] = "S"

    # print the grid
    def print_grid(self, player_row, player_col):
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                if r == player_row and c == player_col:
                    row_str += "@"
                else:
                    row_str += self.data[r][c]
            print(row_str)


    # get the grid
    def get_grid(self):
        return self.grid

    # add the fruit
    def add_fruit(self, row, col):
        # Only place fruit if it's not a wall
        if self.data[row][col] == ".":
            self.data[row][col] = "F"

    # add the lava
    def add_lava(self, row, col):
        if self.data[row][col] == ".":
            self.data[row][col] = "L"


    # add the trap
    def add_trap(self, row, col):
        if self.data[row][col] == ".":
            self.data[row][col] = "T"

    # add a shovel
    def add_shovel(self, row, col):
        if self.data[row][col] == ".":
            self.data[row][col] = "S"
