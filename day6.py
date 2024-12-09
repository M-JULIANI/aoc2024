import argparse
from utils import print_map

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
    with open("data/day6-s.txt", "r") as f:
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
    
def traverse_2(map, start):
    max_row = max(pos[0] for pos in map.keys()) + 1 
    max_col = max(pos[1] for pos in map.keys()) + 1
    
    direction_index = 0
    direction = directions[direction_index]
    current_cell = start
    visited_states = set()
    
    while True:
        current_state = (current_cell, direction_index)
        if current_state in visited_states:
            return True
        visited_states.add(current_state)
        
        next_row = current_cell[0] + direction[0]
        next_col = current_cell[1] + direction[1]
        
        # left matrix
        if (next_row == max_row or next_row < 0 or 
            next_col == max_col or next_col < 0):
            return False
        
        next_cell = (next_row, next_col)
        if map[next_cell] in ['#', 'O']:
            direction_index = (direction_index + 1) % 4
            direction = directions[direction_index]
        else:
            current_cell = next_cell

def part2():    
    possible_positions = 0
    original_map = {} 
    
    with open("data/day6.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
        
        start = (0,0)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '^':
                    start = (row, col)
                original_map[(row, col)] = grid[row][col]
        
        # try place obstruction at each empty position
        for pos in original_map:
            if pos == start or original_map[pos] == '#':
                continue
                
            # testing map
            test_map = original_map.copy()
            test_map[pos] = 'O'
            
            # position crates loop
            if traverse_2(test_map, start):
                possible_positions += 1
                
    return possible_positions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 6 solution')
    parser.add_argument('-p', '--part', type=int, choices=[1, 2], required=True,
                       help='Run part 1 or part 2 of the solution')
    args = parser.parse_args()
    if args.part == 1:
        print(part1())
    elif args.part == 2:    
        print(part2())
