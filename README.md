# klasjoars-adventofcode-2025
https://adventofcode.com

## Day 1: Secret Entrance
The 0-99 dial starts at 50. Count the number of times the dial points at 0 given the input.

Idea: Set one variable to 50, representing the current dial pointer value. Loop through the input values.
- Rx means add x.
- Lx means subtact x.
- Whenever the pointer value becomes 0 or any multiple of 100, increase a counter variable.
    - I.e., every time the rest after floor division with 100 is 0
- The answer is the value of the counter variable at the end.

## Day 2: Gift Shop
### Part 1
Idea:
- Store the input intervals in an array
- Loop: For every number in the interval, treat it as a string and divide it in two equal parts
    - Only numbers with an even number of digits are eligable
- If the two parts are identical, add the original number to a variable
- The variable becomes the answer


## Day 3: Lobby
- Loop through the rows (banks). For every row, make it an array of numbers
- Use an array function to find the largest number its position, twice 
    - After finding each number with its index, pop it into a dictionary
    - Add the numbers as strings in sorted order using the indeces
    - Add the number, as int, to a joltage variable

The above is wrong. I need to get the _biggest_ two-digit number possible. Instead:
- For every bank, take out the biggest number from all digits except the rightmost one.
- Then take the biggest number from the right of the first number's index
