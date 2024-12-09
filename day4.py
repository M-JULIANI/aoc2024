import argparse


def convolve_p1(row_pos, col_pos, grid):
    if grid[row_pos][col_pos] != "X": 
        return 0
    
    row_length = len(grid)
    col_length = len(grid[0])
    xmas_count = 0
    
    directions = [
        (1,1),
        (-1,-1),
        (1,-1),
        (-1,1)
    ]
    
    for i in range(0, len(directions)):
        dir_set = set() 
        direction = directions[i]
        if i > 1:
            dir_set = set()
            
        dr, dc = direction
        r = row_pos + dr
        c = col_pos + dc
            
        if 0 <= r < row_length and 0 <= c < col_length:
            dir_set.add(grid[r][c])
        else:
            break
        
        print(f'dir_set: {dir_set}')
        if len(dir_set) == 2:
            xmas_count += 1    
    return xmas_count

def convolve_p2(row_pos, col_pos, grid):
    if grid[row_pos][col_pos] != "A": 
        return 0
    
    row_length = len(grid)
    col_length = len(grid[0])
    xmas_count = 0
    
    direction_pairs = [
        [(1,1), (-1,-1)],   
        [(1,-1), (-1,1)] 
    ]
    
    for pair in direction_pairs:
        dir_set = set()
        
        for dr, dc in pair:
            r = row_pos + dr
            c = col_pos + dc
            
            if 0 <= r < row_length and 0 <= c < col_length:
                target_cell = grid[r][c]
                if target_cell in ["M", "S"]:
                    dir_set.add(target_cell)
        
        if len(dir_set) == 2:
            xmas_count += 1
    
    # both directions were hit
    if xmas_count == 2:
        return 1
    else:
        return 0

def part1():    
    with open("data/day4.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0])
    print(f"Grid size: {rows}x{cols}")
    
    sum = 0
    for i in range(rows):
        for j in range(cols):
            sum += convolve_p1(i, j, grid)
    
    return sum

def part2():    
    with open("data/day4.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0])
    print(f"Grid size: {rows}x{cols}")
    
    sum = 0
    for i in range(rows):
        for j in range(cols):
            sum += convolve_p2(i, j, grid)
    
    return sum


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 4 solution')
    parser.add_argument('-p', '--part', type=int, choices=[1, 2], required=True,
                       help='Run part 1 or part 2 of the solution')
    args = parser.parse_args()
    if args.part == 1:
        print(part1())
    elif args.part == 2:    
        print(part2())
