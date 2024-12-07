# Advent of Code 2024 Day 2 - Part 2
# Leon Rees 7 Dec 2024
# Solution with full puzzle input
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
    # First check if safe without removing any level
    if check_adjacent_differences(levels) and is_monotonic(levels):
        return True
    
    # Try removing each level one at a time
    for i in range(len(levels)):
        test_levels = levels[:i] + levels[i+1:]
        if check_adjacent_differences(test_levels) and is_monotonic(test_levels):
            return True
    
    return False

def solve(input_text):
    reports = [[int(x) for x in line.split()] for line in input_text.strip().split('\n')]
    return sum(1 for report in reports if is_safe(report))

def read_input_file():
    with open('input.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    input_text = read_input_file()
    result = solve(input_text)
    print(f"Solution: {result}")