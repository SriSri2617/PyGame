import msvcrt
from src.class_grid import Grid

g = Grid()

# add walls
g.add_walls()

# Place fruit inside the box
g.add_fruit(1, 6)
g.add_fruit(4, 10)
g.add_fruit(7, 12)

# Place traps
g.add_trap(3, 8)
g.add_trap(6, 4)

# addd shovel
g.add_shovels()

# get the grid
grid = g.get_grid()

# Add the player and starting from center of the grid
rows = len(g.data)
cols = len(g.data[0])

# Finding the center
player_row = rows // 2
player_col = cols // 2

# score and inventory
score = 0
inventory = []
open_wall = None

# to count moves
moves = 0

# Grace steps for pickups(fruit, shovel)
grace_steps = 0


while True:
    g.print_grid(player_row, player_col)
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

    # Wall open after shovel pickup
    if g.data[new_row][new_col] == "#":

        # If a wall is already open, don't open another
        if open_wall is not None and (new_row, new_col) != open_wall:
            print("Move in through the opening before breaking another wall.")
            continue

        if "shovel" in inventory:
            print("You used the shovel to break the wall!")
            inventory.remove("shovel")

            # Opened wall
            open_wall = (new_row, new_col)

            # Temporarily open the wall
            g.data[new_row][new_col] = "."
        else:
            continue


    # Fruit collection
    if g.data[new_row][new_col] == "F":
        score += 20
        inventory.append("Fruit")

        # Activate the grace steps
        grace_steps = 5

        print("You collected a fruit! Score:", score)
        print("Grace period activated! 5 free steps.")


    # Trap lose 10 points
    if g.data[new_row][new_col] == "T":
        score -= 10
        print("You stepped on a trap! -10 points. Score:", score)

    # Shovel pickup
    if g.data[new_row][new_col] == "S":
        inventory.append("shovel")
        print("You picked up a shovel!")


    # Update to new position
    player_row = new_row
    player_col = new_col


    #Every step lose -1 point
    score -= 1
    print("Step cost: -1 point. Score:", score)

    # Close the wall
    if open_wall is not None:
        r, c = open_wall

        # Close if player is not on it
        if (player_row, player_col) != (r, c):
            g.data[r][c] = "#"
            open_wall = None

    # Count for 25 moves
    moves += 1

    # Fertile soil: spawn fruit every 25 moves
    if moves % 25 == 0:
        for r in range(rows):
            for c in range(cols):
                if g.data[r][c] == ".":
                    g.data[r][c] = "F"
                    print("A new fruit has grown on the fertile soil!")
                    break
            else:
                continue
            break
