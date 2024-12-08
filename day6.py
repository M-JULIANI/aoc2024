import argparse

def print_map(map):
    # Find the dimensions
    max_row = max(pos[0] for pos in map.keys())
    max_col = max(pos[1] for pos in map.keys())

    for row in range(max_row + 1):
        row_str = ''
        for col in range(max_col + 1):
            row_str += map[(row, col)]
        print(row_str)
        
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def traverse(map, start):
    max_row = max(pos[0] for pos in map.keys()) + 1 
    max_col = max(pos[1] for pos in map.keys()) + 1
    
    direction_index = 0
    direction = directions[direction_index]
    current_cell = start
    while True:
        next_row = current_cell[0] + direction[0]
        next_col = current_cell[1] + direction[1]
        
        if next_row == max_row or next_row < 0:
            break;
        if next_col == max_col or next_col < 0:
            break;
        
        next_cell = (next_row, next_col)
        if map[next_cell] == '#':
            direction_index = (direction_index + 1) % 4
            direction = directions[direction_index]
            continue
        else:
            current_cell = next_cell
            map[next_cell] = 'X'

def part1():   
    map = {} 
    with open("data/day6.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
        
        # populate map
        start = (0,0)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '^':
                    start = (row, col)
                map[(row, col)] = grid[row][col]
                
        traverse(map, start)  
        print_map(map) 
             

    return sum(1 for val in map.values() if val == 'X') + 1
    
    
def part2():    
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 6 solution')
    parser.add_argument('-p', '--part', type=int, choices=[1, 2], required=True,
                       help='Run part 1 or part 2 of the solution')
    args = parser.parse_args()
    if args.part == 1:
        print(part1())
    elif args.part == 2:    
        print(part2())
