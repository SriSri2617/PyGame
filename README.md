### Fruit Loop – Python Grid Game
The game is a grid-based adventure where the player moves around, collects items, and avoids hazards.

### How to Run the Game

    - Install Python
    - Clone or download this repository
    - Open a terminal in the project folder
    - Run: python -m src.main_game

The game uses msvcrt.getch() so it runs on Windows.

### Controls

    - W – move up
    - A – move left
    - S – move down
    - D – move right
    - I – show inventory
    - Q or X – quit the game

Movement is instant (no Enter key needed).

### Version 1 – Basic Requirements (Completed)

    - Player starts in the center of the grid
    - Movement in all four directions
    - Cannot walk through walls
    - Fruits give 20 point
    - Inventory stores collected items
    - Command i prints inventory
     - Lava floor: lose 1 point per step
    - Walls created using for-loops, no unreachable rooms

All Version 1 requirements are implemented.

### Version 2 – Optional Features (Implemented)

    - Traps: stepping on a trap loses 10 points
    - Shovel: breaks a wall temporarily
    - Fertile soil: every 25 moves a new fruit grows

**Version 3** - few features tested

#### File Structure

    Py_Game 
        - src
            -__init__.py
            - class_grid.py
            - main_game.py
        - tests
            - __init__.py
            - test_grid.py
            - test_main_game.py

- test_grid.py - test the Grid class
- test_main_game.py - test fruit pickup, lava & trap

### How to run test file

    - Open terminal in Py_Game and run python -m unittest discover -s tests ( for all test file)
    - Open Py_Game in terminal & run python -m unittest tests.test_grid / tests.test_main_game (for single test file)

### Grid test verify

    - Grid size
    - Fruit placement
    - Lava Placement
    - Trap placement
    - Shovel placement

### main_game test verify

    - Fruit picu-up score = 20
    - Lava step-in score = -1
    - Trap step-in score = -10

Always run tests from the project root, not inside src or tests.

    
