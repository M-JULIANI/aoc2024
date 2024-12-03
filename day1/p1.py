import pandas as pd

class SortedDiff:
    def __init__(self, data_path: str):
        self.data = pd.read_csv(data_path, delim_whitespace=True, header=None, names=['col1', 'col2'])
        # print(self.data[:10])
        self.data['col1'] = self.data['col1'].sort_values().values
        self.data['col2'] = self.data['col2'].sort_values().values
        # print(self.data['col1'][:10])
        # print(self.data['col2'][:10])
        
    def aggregate_diff(self):
        return abs(self.data['col1'] - self.data['col2']).sum()
                

if __name__ == "__main__":
    sorted_diff = SortedDiff("data/day1_p1.csv")
    print(sorted_diff.aggregate_diff())