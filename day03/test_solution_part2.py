# Advent of Code 2024 Day 3 - Part 2
# Leon Rees 7 Dec 2024
# Solution with limited test data
import re

def solve(input_text):
    # Track enabled state and find all relevant instructions
    enabled = True
    total = 0
    
    # Find all instructions in order
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Combine patterns and use named groups
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

# Test data
test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"
result = solve(test_input)
print(f"Test solution: {result}")  # Should print 48