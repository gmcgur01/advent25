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

    num_timelines = shoot_beam(space)

    print(num_timelines)

def shoot_beam(space):

    space_width = len(space[0])

    for line_index, line in enumerate(space):
        for char_index, char in enumerate(line):
            if char == "S":
                space[line_index+1][char_index] = 1
            if isinstance(char, int):
                if line_index == len(space) - 1:
                    continue
                if space[line_index+1][char_index] != "^":
                    if isinstance(space[line_index+1][char_index], int):
                        space[line_index+1][char_index] += char
                    elif space[line_index+1][char_index] == ".":
                        space[line_index+1][char_index] = char
                else:
                    if char_index != 0 and space[line_index+1][char_index-1] != "^":
                        if isinstance(space[line_index+1][char_index-1], int):
                            space[line_index+1][char_index-1] += char
                        elif space[line_index+1][char_index-1] == ".":
                            space[line_index+1][char_index-1] = char
                    if char_index != space_width-1 and space[line_index+1][char_index+1] != "^":
                        if isinstance(space[line_index+1][char_index+1], int):
                            space[line_index+1][char_index+1] += char
                        elif space[line_index+1][char_index+1] == ".":
                            space[line_index+1][char_index+1] = char

    return sum([char for char in space[-1] if isinstance(char, int)])
        


if __name__ == "__main__":
    main()