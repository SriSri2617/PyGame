import msvcrt
from class_grid import Grid

g = Grid()

# add walls
g.add_walls()

# Place fruit inside the box
g.add_fruit(1, 6)
g.add_fruit(4, 10)
g.add_fruit(7, 12)

# Place lava inside the box
g.add_lava(3, 5)
g.add_lava(6, 10)
g.add_lava(4, 7)

# Place traps
g.add_trap(3, 8)
g.add_trap(6, 4)

# Place shovel
g.add_shovel(5, 5)

# get the grid
grid = g.get_grid()

# Add the player and strating from center of the grid
rows = len(grid)
cols = len(grid[0])

# Finding the center
player_row = rows // 2
player_col = cols // 2

# positioning the player
grid[player_row][player_col] = "@"

# score and inventory
score = 0
inventory = []
open_wall = None

# to count moves
moves = 0


while True:
    g. print_grid()
    print("Move (WASD, Q to quit): ")

    cmd = msvcrt.getch().decode().lower()

    # Check inventory
    if cmd == "i":
        print("Inventory:", inventory)
        continue

    # WSAD up and down movement
    # Exit
    if cmd == "q" or cmd == "x":
        print("Goodbye!")
        break

    elif cmd == "w":
        new_row = player_row - 1
        new_col = player_col
    elif cmd =="s":
        new_row = player_row + 1
        new_col = player_col
    elif cmd =="a":
        new_row = player_row
        new_col = player_col - 1
    elif cmd =="d":
        new_row = player_row
        new_col = player_col + 1
    else:
        continue

    # Shovel pickup
    if grid[new_row][new_col] == "#":
        if "shovel" in inventory:
            print("You used the shovel to break the wall!")
            inventory.remove("shovel")

            # Opened wall
            open_wall = (new_row, new_col)

            # Temporarily open the wall
            grid[new_row][new_col] = "."
        else:
            continue


    # Fruit collection
    if grid[new_row][new_col] == "F":
        score += 20
        inventory.append("Fruit")
        print("You collected a fruit! Score:", score)

    # Lava -1 points
    if grid[new_row][new_col] == "L":
        score -= 1
        print("Ouch! Lava -1 point. Score:", score)

    # Trap lose 10 points
    if grid[new_row][new_col] == "T":
        score -= 10
        print("You stepped on a trap! -10 points. Score:", score)

    # Shovel pickup
    if grid[new_row][new_col] == "S":
        inventory.append("shovel")
        print("You picked up a shovel!")

    # Remove old player
    grid[player_row][player_col] = "."

    # Update to new position
    player_row = new_row
    player_col = new_col

    grid[player_row][player_col] = "@"

    # Close the wall
    if open_wall is not None:
        r, c = open_wall

        # Close if player is not on it
        if (player_row, player_col) != (r, c):
            grid[r][c] = "#"
            open_wall = None

    # Count for 25 moves
    moves += 1

    # Fertile soil: spawn fruit every 25 moves
    if moves % 25 == 0:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ".":
                    grid[r][c] = "F"
                    print("A new fruit has grown on the fertile soil!")
                    break
            else:
                continue
            break







