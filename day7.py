import argparse
import itertools

operators = [lambda x, y: x * y, lambda x, y: x + y, lambda x,y: int(str(x) + str(y))]
def try_compute(result, parts): 
    # print(f"result: {result}, parts: {parts}")
    
    combinations = {}
    for i in range(len(parts)-1):
        combinations[i] = []
        for op in operators:
            combinations[i].append(op)
    
    for combo in itertools.product(*combinations.values()):
        partial_result = parts[0]
        for i, operator in enumerate(combo):
            partial_result = operator(partial_result, parts[i + 1])
            # print(f'partial_result: {partial_result}')
        
        if partial_result == result:
            return partial_result
    return 0

    
     
def part1():   
    result_total = 0
    with open("data/day7.txt", "r") as f:
        for line in f:
            split = line.strip().split(':')
            result, parts_str = split
            parts_str = parts_str.strip()
            parts = list(map(int, parts_str.split()))
            result_total += try_compute(int(result), parts)        
        print(result_total)
    

def part2():    
    result_total = 0
    with open("data/day7.txt", "r") as f:
        for line in f:
            split = line.strip().split(':')
            result, parts_str = split
            parts_str = parts_str.strip()
            parts = list(map(int, parts_str.split()))
            result_total += try_compute(int(result), parts)       
            
        print('grand total: ', result_total)
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 7 solution')
    parser.add_argument('-p', '--part', type=int, choices=[1, 2], required=True,
                       help='Run part 1 or part 2 of the solution')
    args = parser.parse_args()
    if args.part == 1:
        print(part1())
    elif args.part == 2:    
        print(part2())
