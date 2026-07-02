import unittest
from src.class_grid import Grid


class TestMainGame(unittest.TestCase):

    # Fruit pickup validation
    def test_fruit_pickup(self):
        g = Grid()
        g.add_fruit(1, 6)
        score = 0

        if g.get_grid()[1][6] == "F":
            score += 20

        self.assertEqual(score, 20)


     # Lava - score -1 - validation
    def test_lava_damage(self):
        g = Grid()
        g.add_lava(4, 7)
        score = 10

        if g.get_grid()[4][7] == "L":
            score -= 1

        self.assertEqual(score, 9)

    # Trap - step in score -5
    def test_trap_damage(self):
        g = Grid()
        g.add_trap(3, 8)
        score = 10

        if g.get_grid()[3][8] == "T":
            score -= 5

        self.assertEqual(score, 5)

        # to run only this test file

    if __name__ == "__main__":
        unittest.main()

