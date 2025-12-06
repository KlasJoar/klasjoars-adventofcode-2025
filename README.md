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