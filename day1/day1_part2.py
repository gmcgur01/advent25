import re
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    try:
        with open(sys.argv[1]) as file:
           code = move_dial(file)
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    print(code)

def move_dial(file):
    dial = Dial(100)
    for line in file:
        if matches := re.findall(r"R(\d+)", line):
            dial.move_right(int(matches[0]))
        elif matches := re.findall(r"L(\d+)", line):
            dial.move_left(int(matches[0]))
        else:
            raise ValueError("Invalid line: " + line)
    
    return dial.total_time_on_zero

class Dial:
    def __init__(self, dial_size):
        self.curr_val = 50
        self.total_time_on_zero = 0
        self.dial_size = dial_size

    def move_left(self, amount):
        starting_val = self.curr_val
        unmodded_result = self.curr_val - amount
        self.curr_val = unmodded_result % self.dial_size
        times_passing_zero = -1 * (unmodded_result // self.dial_size)
        if starting_val == 0:
            times_passing_zero -= 1
        self.total_time_on_zero += times_passing_zero
        if self.curr_val == 0:
            self.total_time_on_zero += 1
    
    def move_right(self, amount):
        unmodded_result = self.curr_val + amount
        self.curr_val = unmodded_result % self.dial_size
        self.total_time_on_zero += (unmodded_result // self.dial_size)

if __name__ == "__main__":
    main()