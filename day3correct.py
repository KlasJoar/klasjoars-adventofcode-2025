import heapq

total_joltage = 0

with open('day3input.txt', 'r') as f:
    for line in f:
        first_digit = max(line[:-2]) # The line contains the newlin character at the end,
                                     # hence the need to only go until index -2

        i = line.index(first_digit)
        second_digit = max(line[i+1:])

        total_joltage += int(first_digit + second_digit)

print('Total joltage: ', total_joltage)