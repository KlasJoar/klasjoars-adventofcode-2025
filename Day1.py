# import os

dial_value = 50
zero_counter = 0


with open('Day1input.txt', 'r') as file:
    for line in file:
        # Clockwise rotetion, adding the number
        if line[0] == 'R':
            dial_value += int(line[1:])
        # Anti-clockwise, subtracting the number
        elif line[0] == 'L':
            dial_value -= int(line[1:])
        
        if dial_value % 100 == 0:
            zero_counter += 1
        # print(line.strip())
        # print(dial_value)

print(zero_counter)
        
        
