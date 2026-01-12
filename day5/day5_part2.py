import re
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    intervals = []

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if match := re.match(r"(\d+)-(\d+)", line):
                    intervals.append(Interval(int(match.group(1)), int(match.group(2))))
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    intervals.sort(key=lambda interval: interval.start)

    start = intervals[0].start
    furthest = intervals[0].start
    num_invalid = 0
    for interval in intervals:
        if interval.start > furthest:
            num_invalid += interval.start - furthest - 1
        if interval.end > furthest:
            furthest = interval.end

    total_valid = furthest - (start - 1) - num_invalid

    print(total_valid)



class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def contains(self, val):
        return self.start <= val and self.end >= val

if __name__ == "__main__":
    main()