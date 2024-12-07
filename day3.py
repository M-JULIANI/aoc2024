import pandas as pd
import argparse
import re


def part1():
    sum = 0
    with open("data/day3.txt", "r") as f:
        lines = f.readlines()
        regex = re.compile(r"mul\((\d{1,3}),\s*(\d{1,3})\)")
        
        for line in lines:
            matches = regex.finditer(line)
            for match in matches:
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                sum += num1 * num2
                print(f"Found numbers: {num1}, {num2}")
    return sum


def part2():
    sum = 0
    last_action = "do()" 
    print(f"Starting calculation with default action: {last_action}")
    
    with open("data/day3.txt", "r") as f:
        lines = f.readlines()
        mul_pattern = re.compile(r"mul\((\d{1,3}),\s*(\d{1,3})\)")
        action_pattern = re.compile(r"(do\(\)|don\'t\(\))")
        
        all_text = ""
        for line_num, line in enumerate(lines):
            print(f"\n{'='*50}")
            print(f"Processing line {line_num}: {line.strip()}")
            
            all_text += line
            
            mul_matches = list(mul_pattern.finditer(line))
            print(f"Found {len(mul_matches)} mul pattern(s) in this line")
            
            running_sum = sum
            for mul_match in mul_matches:
                # Find all actions that precede this mul in ALL previous text
                mul_pos_in_line = mul_match.start()
                mul_pos_in_all = len(all_text) - len(line) + mul_pos_in_line
                preceding_text = all_text[:mul_pos_in_all]
                actions = list(action_pattern.finditer(preceding_text))
                
                # Get last action from all preceding text, or use default
                current_action = actions[-1].group(0) if actions else "do()"
                
                num1 = int(mul_match.group(1))
                num2 = int(mul_match.group(2))
                
                print(f"For mul({num1},{num2}), last preceding action: {current_action}")
                
                if current_action == "do()":
                    sum += num1 * num2
                    print(f"Processing mul({num1},{num2})")
                else:
                    print(f"Skipping mul({num1},{num2})")
    return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Day 3 solution')
    parser.add_argument('-p', '--part', type=int, choices=[1, 2], required=True,
                       help='Run part 1 or part 2 of the solution')
    args = parser.parse_args()
    if args.part == 1:
        print(part1())
    elif args.part == 2:    
        print(part2())
