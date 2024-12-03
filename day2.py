import pandas as pd
import argparse

class Solver:
    def __init__(self, data_path: str):
        with open(data_path, 'r') as f:
            lines = f.readlines()
            data = [list(map(int, line.strip().split())) for line in lines]
            self.data = pd.DataFrame(data)
        
    def is_safe(self, x):
        dir = 1 if x[0] - x[1] > 0 else -1
        for i in range(len(x)-1):
            if pd.isna(x[i]) or pd.isna(x[i+1]):
                continue
                
            diff = x[i] - x[i+1]
            if dir > 0:
                if diff < 1 or diff > 3:
                    print(f"Unsafe: {x}")
                    return False
            else:
                if diff > -1 or diff <-3:
                    print(f"Unsafe: {x}")
                    return False
        print(f"Safe: {x}")
        return True 
    
    def check_diff_unsafe(self, val1, val2, dir):
        if pd.isna(val1) or pd.isna(val2):
            return False
        
        diff = val1 - val2
        if dir > 0:
            return diff < 1 or diff > 3
        else:
            return diff > -1 or diff < -3
    
    def is_safe_lax(self, x):
        dir = 1 if x[0] - x[1] > 0 else -1
        i = 0 
        while i < len(x)-1:
            if pd.isna(x[i]) or pd.isna(x[i+1]):
                i += 1
                continue
                
            diff = x[i] - x[i+1]
            if dir > 0:
                if diff < 1 or diff > 3:
                    print(f"Possible Unsafe: {x}")
                    if i+2 < len(x):
                        if not self.check_diff_unsafe(x[i], x[i+2], dir):
                            i += 1
                            continue
                    return False
            else:
                if diff > -1 or diff < -3:
                    print(f"Possible Unsafe: {x}")
                    if i+2 < len(x):
                        if not self.check_diff_unsafe(x[i], x[i+2], dir):
                            i += 1
                            continue
                    return False
            i += 1
                
        print(f"Safe: {x}")
        return True 
        
    def part1(self):
        res=self.data.apply(lambda row: self.is_safe(row), axis=1)
        val_counts = res.value_counts()
        print(val_counts)
        return val_counts[True]
    
    def part2(self):
        res=self.data.apply(lambda row: self.is_safe_lax(row), axis=1)
        val_counts = res.value_counts()
        print(val_counts)
        return val_counts[True]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 2 solution')
    parser.add_argument('-p', '--part', type=int, choices=[1, 2], required=True,
                       help='Run part 1 or part 2 of the solution')
    solver = Solver("data/day2.csv")
    args = parser.parse_args()
    if args.part == 1:
        print(solver.part1())
    elif args.part == 2:
        print(solver.part2())
