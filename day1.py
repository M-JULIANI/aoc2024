import pandas as pd
import argparse

class SortedDiff:
    def __init__(self, data_path: str):
        self.data = pd.read_csv(data_path, delim_whitespace=True, header=None, names=['col1', 'col2'])
        # print(self.data[:10])
        self.data['col1'] = self.data['col1'].sort_values().values
        self.data['col2'] = self.data['col2'].sort_values().values
        # print(self.data['col1'][:10])
        # print(self.data['col2'][:10])
        
    def part1(self):
        return abs(self.data['col1'] - self.data['col2']).sum()
    
    def part2(self):
        col2_counts = self.data['col2'].value_counts()
        matches = self.data['col1'].map(lambda x: col2_counts.get(x, 0) * x)
        return matches.sum()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 1 solution')
    parser.add_argument('-p', '--part', type=int, choices=[1, 2], required=True,
                       help='Run part 1 or part 2 of the solution')
    sorted_diff = SortedDiff("data/day1_p1.csv")
    args = parser.parse_args()
    if args.part == 1:
        print(sorted_diff.part1())
    elif args.part == 2:
        print(sorted_diff.part2())
