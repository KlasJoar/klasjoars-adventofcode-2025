import heapq

total_joltage = 0

with open('day3input.txt', 'r') as f:
    for line in f:
        i_largest = {}

        # take the two largest numbers and store their index and value
        for n in heapq.nlargest(2, line):
            i_largest[line.index(n)] = n

        joltage_string = ''
        for i in sorted(i_largest):
            joltage_string += i_largest[i]

            # If there is only one value, double it
            if len(i_largest) == 1:
                joltage_string += joltage_string

        # Add the joltage to the total
        total_joltage += int(joltage_string)

print('Total joltage: ', total_joltage)