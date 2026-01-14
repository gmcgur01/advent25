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

    edges = [edge(tiles[i], tiles[i+1 if i+1 < len(tiles) else 0]) for i in range(len(tiles))] 

    max_area = 0
    for index, tile_i in enumerate(tiles):
        for tile_j in tiles[index+1:]:
            area = calc_area(tile_i, tile_j)
            if area > max_area and is_square_valid(tile_i, tile_j, edges):
                max_area = area

    print(max_area)

def calc_area(tile1, tile2):
    return (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)

def is_square_valid(tile1, tile2, edges):
    # two given tiles are confirmed valid, so need to check the opposite corners (for fast fail)

    other_corner1 = (tile1[0], tile2[1])
    other_corner2 = (tile2[0], tile1[1])

    if not is_point_inside(other_corner1[0], other_corner1[1], edges):
        return False
    
    if not is_point_inside(other_corner2[0], other_corner2[1], edges):
        return False
    
    corners = [tile1, other_corner1, tile2, other_corner2]

    for i in range(len(corners)):
        if not is_point_on_inner_edge_outside(corners[i], corners[i+1 if i+1 < len(corners) else 0], edges):
            return False
    
    return True

def is_point_on_inner_edge_outside(coord1, coord2, edges):
    if coord1[0] == coord2[0]:
        if coord1[1] <= coord2[1]:
            lower_y = coord1[1]
            higher_y = coord2[1]
        else:
            lower_y = coord2[1]
            higher_y = coord1[1]

        for y in range(lower_y + 1, higher_y):
            if not is_point_inside(coord1[0], y, edges):
                return False
    elif coord1[1] == coord2[1]:
        if coord1[0] <= coord2[0]:
            lower_x = coord1[0]
            higher_x = coord2[0]
        else:
            lower_x = coord2[0]
            higher_x = coord1[0]

        for x in range(lower_x + 1, higher_x):
            if not is_point_inside(x, coord1[1], edges):
                return False
    else:
        print("edge is not aligned on an axis:", coord1, coord2)
        sys.exit(1)

    return True

def is_point_inside(x, y, edges):
    is_inside = False
    for edge in edges:
        if edge.is_vertical:
            if edge.is_point_on_edge(x, y):
                return True
            elif edge.intersects_in_positive_x(x, y):
                is_inside = not is_inside
        else:
            if edge.is_point_on_edge(x, y):
                return True
            
    return is_inside
        
class edge:

    def __init__(self, coord1, coord2):
        self.is_vertical = coord1[0] == coord2[0]
        if (self.is_vertical and coord1[1] <= coord2[1]) or (not self.is_vertical and coord1[0] <= coord2[0]):
            self.coord1 = coord1
            self.coord2 = coord2
        else:
            self.coord1 = coord2
            self.coord2 = coord1

        # if it is vertical, set coord1 to be the "lower" coord (in terms of )

    def is_point_on_edge(self, x, y):
        if self.is_vertical:
            return x == self.coord1[0] and y >= self.coord1[1] and y <= self.coord2[1]
        else:
            return y == self.coord1[1] and x >= self.coord1[0] and x <= self.coord2[0]

    # using ray cast algo, just need to check collision in the positive x axis
    def intersects_in_positive_x(self, x, y):
        # skip over horizontal vertices
        if not self.is_vertical:
            return False
        
        # check if y range aligns (don't include lower end)
        if y <= self.coord1[1] or y > self.coord2[1]:
            return False
        
        # check if x would intersect (not inclusive)
        return x < self.coord1[0] 


if __name__ == "__main__":
    main()