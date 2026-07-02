from src.class_grid import Grid
import unittest

class TestGrid(unittest.TestCase):

    def test_grid(self):
        g = Grid()
        grid = g.grid

        # grid row and col size validation
        self.assertEqual(len(grid), 10)
        print(len(grid), len(grid[0]))
        self.assertEqual(len(grid[0]),20)

        # cells should be "."
        for row in grid:
            for cells in row:
                self.assertEqual(cells, ".")


    # Fruit validation
    def test_add_fruit(self):
        g = Grid()
        g.add_fruit(2,3)
        grid = g.get_grid()

        self.assertEqual(grid[2][3], "F")

    # Lava validation
    def test_add_lava(self):
        g = Grid()
        g.add_lava(6,10)
        grid = g.get_grid()

        self.assertEqual(grid[6][10], "L")


    # Trap validation
    def test_add_trap(self):
        g = Grid()
        g.add_trap(6,4)
        grid = g.get_grid()

        self.assertEqual(grid[6][4], "T")

    # Shovel validation
    def test_add_shovel(self):
        g = Grid()
        g.add_shovel(5,5)
        grid = g.get_grid()

        self.assertEqual(grid[5][5], "S")


   # to run only this test file
    if __name__ == "__main__":
        unittest.main()