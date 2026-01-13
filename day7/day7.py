import re
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    space = []

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                space.append(list(line.strip()))
                    
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    num_times_split = shoot_beam(space)

    print(num_times_split)

def shoot_beam(space):

    num_times_split = 0

    space_width = len(space[0])

    for line_index, line in enumerate(space):
        for char_index, char in enumerate(line):
            if char == "S":
                space[line_index+1][char_index] = "|"
            if char == "|":
                if line_index == len(space) - 1:
                    continue
                if space[line_index+1][char_index] == ".":
                    space[line_index+1][char_index] = "|"
                elif space[line_index+1][char_index] == "^":
                    num_times_split += 1
                    if char_index != 0 and space[line_index+1][char_index-1] == ".":
                        space[line_index+1][char_index-1] = "|"
                    if char_index != space_width-1 and space[line_index+1][char_index+1] == ".":
                        space[line_index+1][char_index+1] = "|"

    return num_times_split
        


if __name__ == "__main__":
    main()