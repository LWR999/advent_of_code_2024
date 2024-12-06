# Advent of Code 2024 Day 1
# Leon Rees 6 Dec 2024

def parse_input(input_text):
    lines = input_text.strip().split('\n')
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    # Sort both lists independently
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    total_distance = 0
    # Calculate distance between corresponding elements after sorting
    for left, right in zip(sorted_left, sorted_right):
        distance = abs(left - right)
        total_distance += distance
        
    return total_distance

def solve(input_text):
    left_list, right_list = parse_input(input_text)
    return calculate_total_distance(left_list, right_list)

def read_input_file():
    with open('input.txt', 'r') as file:
        return file.read()

if __name__ == '__main__':
    input_text = read_input_file()
    result = solve(input_text)
    print(f"Solution: {result}")