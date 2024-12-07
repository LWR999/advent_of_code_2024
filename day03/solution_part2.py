# Advent of Code 2024 Day 3 - Part 1
# Leon Rees 7 Dec 2024
# Solution with full puzzle input
import re

def solve(input_text):
    enabled = True
    total = 0
    
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    pattern = f'(?P<mul>{mul_pattern})|(?P<do>{do_pattern})|(?P<dont>{dont_pattern})'
    
    for match in re.finditer(pattern, input_text):
        if match.group('do'):
            enabled = True
        elif match.group('dont'):
            enabled = False
        elif match.group('mul') and enabled:
            x, y = map(int, match.group('mul').replace('mul(', '').replace(')', '').split(','))
            total += x * y
    
    return total

def read_input_file():
    with open('input.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    input_text = read_input_file()
    result = solve(input_text)
    print(f"Solution: {result}")