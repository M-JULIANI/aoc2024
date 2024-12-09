def print_map(map):
    # find the dimensions
    max_row = max(pos[0] for pos in map.keys())
    max_col = max(pos[1] for pos in map.keys())

    for row in range(max_row + 1):
        row_str = ''
        for col in range(max_col + 1):
            row_str += map[(row, col)]
        print(row_str)
 