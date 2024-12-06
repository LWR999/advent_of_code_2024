# Advent of Code 2024 Day 1 Part 2
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

def calculate_similarity_score(left_list, right_list):
    total_score = 0
    
    for left_num in left_list:
        occurrences = right_list.count(left_num)
        total_score += left_num * occurrences
        
    return total_score

def solve(input_text):
    left_list, right_list = parse_input(input_text)
    return calculate_similarity_score(left_list, right_list)

def read_input_file():
    with open('input.txt', 'r') as file:
        return file.read()

input_text = read_input_file()
result = solve(input_text)
print(f"Solution: {result}")