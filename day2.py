intervals = []
answersum = 0

with open('day2input.txt', 'r') as f:
    intervals = f.read().split(',')

for interval in intervals:
    # Parse out the range  as numbers
    interval_as_array = interval.split('-')
    start = int(interval_as_array[0])
    stop = int(interval_as_array[1])
    
    for number in range(start, stop + 1):
 
        # Treat the number as a string
        number_s = str(number)

        # Only look at numbers of even length
        if len(number_s) % 2 != 0:
            pass

        # Split the number in two parts
        splitindex = len(number_s) // 2
        first_part = number_s[:splitindex]
        second_part = number_s[splitindex:len(number_s)]

        # If the two are equal, add the number to the answersum
        if first_part == second_part:
            answersum += number

print(answersum)