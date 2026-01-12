import re
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    intervals = []
    ids = []

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if match := re.match(r"(\d+)-(\d+)", line):
                    intervals.append(Interval(int(match.group(1)), int(match.group(2))))
                elif match := re.match(r"(\d+)", line):
                    ids.append(int(match.group(1)))
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")
    
    print(len([id for id in ids if is_valid_id(id, intervals)]))

def is_valid_id(id, intervals):
    for interval in intervals:
        if interval.contains(id):
            return True
    return False

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def contains(self, val):
        return self.start <= val and self.end >= val

if __name__ == "__main__":
    main()