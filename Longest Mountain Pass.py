# https://www.codewars.com/kata/660595d3bd866805d00ec4af/train/python

def longest_mountain_pass(mountains, E):
    max_length = 0
    start_index = 0
    current_length = 0
    current_energy = E
    
    for i in range(len(mountains) - 1):
        energy_cost = mountains[i + 1] - mountains[i]
        
        if energy_cost <= 0 or energy_cost > current_energy:
            current_length = 0
            start_index = i + 1
            current_energy = E
        else:
            current_energy -= energy_cost
            current_length += 1
            if current_length > max_length:
                max_length = current_length
    
    return (max_length + 1, start_index)

# Test ca


print(longest_mountain_pass([10, 9, 8, 7, 6, 5, 4, 3, 2, 3], 1))
print(longest_mountain_pass([9, 1, 2, 3, 4, 5, 6, 9], 7))
print(longest_mountain_pass([1, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
print(longest_mountain_pass([], 0))
print(longest_mountain_pass([10, 10, 10], 0))
print(longest_mountain_pass([1, 2, 3, 4, 5], 0))
# 10 0
#  7 0
#  9 1
#  0 0
#  3 0
#  1 0