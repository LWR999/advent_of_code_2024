# Advent of Code 2024 Day 3 - Part 1
# Leon Rees 7 Dec 2024
# Solution with full puzzle input
import re

def solve(input_text):
    # Find all valid mul(X,Y) patterns
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, input_text)
    
    total = 0
    for match in matches:
        x, y = map(int, match.groups())
        total += x * y
    
    return total

def read_input_file():
    with open('input.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    input_text = read_input_file()
    result = solve(input_text)
    print(f"Solution: {result}")