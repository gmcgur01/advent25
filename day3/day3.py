import re
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    try:
        with open(sys.argv[1]) as file:
           total = 0
           for line in file:
               total += max_joltage(line.strip())
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    print(total)

def max_joltage(battery):

    curr_max = int(battery[-2:])
    for i in reversed(range(len(battery) - 2)):
        if (int(battery[i]) * 10) + 9 > curr_max:
            curr_max = int(battery[i]) * 10 + max([curr_max // 10, curr_max % 10])
        
    return curr_max

   

if __name__ == "__main__":
    main()