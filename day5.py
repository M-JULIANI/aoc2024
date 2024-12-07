import argparse

def topological_sort(pairs):
    graph={}
    in_degree={}
    nodes=set()
    
    # populate set
    for src,dst in pairs:
        nodes.add(src)
        nodes.add(dst)    
        
    # init graph
    for node in nodes:
        graph[node] = []
    
    # populate graph
    for src, dst in pairs:
        graph[src].append(dst)
    
    # populate in_degree
    for src, dst in pairs:
        in_degree[dst]=in_degree.get(dst,0)+1
    
    print(f'graph: {graph}')
    print(f'in_degree: {in_degree}')
    print(f'nodes: {nodes}')
    
    # Create a queue of all nodes with in-degree zero
    queue = [node for node in nodes if in_degree.get(node,0) ==0]
    print(f'queue: {queue}')
    result = []
    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if(len(result) != len(nodes)):
        raise ValueError("Graph has at least one cycle")
    
    return result   

def verify_order(list,pairs):
    for src,dst in pairs:
        if src not in list or dst not in list:
            continue
        if list.index(src) > list.index(dst):
            return False
    return True 

def part1():    
    with open("data/day5.txt", "r") as f:
        first_part, second_part = f.read().split('\n\n')
        
        first_lines = first_part.strip().split('\n')
        second_lines = second_part.strip().split('\n')
        
        updates = [[int(num) for num in line.split(',')] for line in second_lines]
        print(f'updates: {updates}')
        pairs = [tuple(map(int, line.split('|'))) for line in first_lines]
        #result = topological_sort(pairs)
        
        middles = []
        for line in updates:
            if verify_order(line,pairs):
                length = len(line)
                index = length//2
                middles.append(line[index])
                print(f'{line} is valid') 
            else:
                print(f'{line} is not valid')
    
    return sum(middles)
def part2():    
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 5 solution')
    parser.add_argument('-p', '--part', type=int, choices=[1, 2], required=True,
                       help='Run part 1 or part 2 of the solution')
    args = parser.parse_args()
    if args.part == 1:
        print(part1())
    elif args.part == 2:    
        print(part2())
