def calculate_next_minute(grid):
    new_grid = [['.'] * 5 for _ in range(5)]
    
    for i in range(5):
        for j in range(5):
            lifeforms_count = 0
            empty_spaces_count = 0
            
            # Check the four adjacent tiles
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                
                # Count the adjacent lifeforms and empty spaces
                if 0 <= x < 5 and 0 <= y < 5:
                    if grid[x][y] == 'X':
                        lifeforms_count += 1
                    else:
                        empty_spaces_count += 1
            
            # Apply the rules to update the cell
            if grid[i][j] == 'X':
                if lifeforms_count == 1:
                    new_grid[i][j] = 'X'
                else:
                    new_grid[i][j] = '.'
            else:
                if lifeforms_count == 1 or lifeforms_count == 2:
                    new_grid[i][j] = 'X'
                else:
                    new_grid[i][j] = '.'
    
    return new_grid


def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def calculate_lifeform_score(layout):
    tile_values = [2**i for i in range(25)]
    score = 0
    
    for i in range(5):
        for j in range(5):
            if layout[i][j] == 'X':
                tile_number = i * 5 + j
                score += tile_values[tile_number]
    
    return score


# Example start state
start_state = [
    ['X', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', '.'],
    ['X', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', '.', 'X', 'X'],
]

# Print the start state
print("Start state:")
print_grid(start_state)

# Generate and print the layouts until a repeated layout is encountered
grids = [start_state]  # Keep track of encountered layouts
minute = 1
while True:
    next_grid = calculate_next_minute(grids[-1])
    if next_grid in grids:
        print(f"{minute} minute:")
        print_grid(next_grid)
        print(f"Repeated layout encountered after {minute} minute(s).")
        break
    else:
        grids.append(next_grid)
        minute += 1

lifeform_score = calculate_lifeform_score(next_grid)

print("Lifeform score:", lifeform_score)
