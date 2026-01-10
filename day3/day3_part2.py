import re
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    try:
        with open(sys.argv[1]) as file:
           total = 0
           for line in file:
               joltage = max_joltage(line.strip())
               total += joltage
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    print(total)

def construct_new_val(digit, other):
    if other == 0:
        return digit
    return (pow(10, len(str(other))) * digit) + other

def max_joltage(battery):

    max_vals = [0 for _ in range(12)]
    
    num_digits_checked = 0
    for index in reversed(range(len(battery))):
        num_digits_checked += 1
        digit = int(battery[index])
        for i in reversed(range(len(max_vals))):
            if i >= num_digits_checked:
                continue
            
            if i == 0:
                max_vals[i] = max([digit, max_vals[i]])
            else:
                max_vals[i] = max([construct_new_val(digit, max_vals[i-1]), max_vals[i]])


    return max_vals[-1]

if __name__ == "__main__":
    main()