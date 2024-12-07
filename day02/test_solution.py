# Advent of Code 2024 Day 2 - Part 1
# Leon Rees 7 Dec 2024
# Solution with limited test data
def check_adjacent_differences(levels):
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_monotonic(levels):
    increasing = all(levels[i] <= levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] >= levels[i + 1] for i in range(len(levels) - 1))
    return increasing or decreasing

def is_safe(levels):
    return check_adjacent_differences(levels) and is_monotonic(levels)

def solve(input_text):
    reports = [[int(x) for x in line.split()] for line in input_text.strip().split('\n')]
    return sum(1 for report in reports if is_safe(report))

# Test data
test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

result = solve(test_input)
print(f"Test solution: {result}")  # Should print 2