# Advent of Code 2024 Day 1 - Part 2
# Leon Rees 6 Dec 2024
# Solution with limited test data

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

# Test with example input
example_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

result = solve(example_input)
print(f"Example solution: {result}")  # Should print 31