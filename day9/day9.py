import re
import sys
from dataclasses import dataclass
import math


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    tiles = []

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                coords = line.strip().split(",")
                tiles.append((int(coords[0]), int(coords[1])))
                    
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    max_area = 0
    for index, tile_i in enumerate(tiles):
        for tile_j in tiles[index+1:]:
            area = calc_area(tile_i, tile_j)
            if area > max_area:
                max_area = area

    print(max_area)

        
def calc_area(tile1, tile2):
    return (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)

if __name__ == "__main__":
    main()