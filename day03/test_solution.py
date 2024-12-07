# Advent of Code 2024 Day 3 - Part 1
# Leon Rees 7 Dec 2024
# Solution with limited test data
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

# Test data
test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
result = solve(test_input)
print(f"Test solution: {result}")  # Should print 161