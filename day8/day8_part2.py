import re
import sys
from dataclasses import dataclass
import math


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    junction_boxes = []

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                nums = line.strip().split(",")
                junction_boxes.append(junction_box(int(nums[0]), int(nums[1]), int(nums[2])))
                    
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    edges = []

    for i in range(len(junction_boxes)):
        for j in range(i+1, len(junction_boxes)):
            edges.append(connection(junction_boxes[i], junction_boxes[j]))

    edges.sort(key=lambda edge: edge.distance)

    circuits = {}
    for edge in edges:
        
        box1 = edge.boxes[0]
        box2 = edge.boxes[1]

        if box1 not in circuits and box2 not in circuits:
            new_circuit = {box1, box2}
            circuits[box1] = new_circuit
            circuits[box2] = new_circuit
        elif box1 not in circuits:
            box2_circuit = circuits[box2]
            box2_circuit.add(box1)
            circuits[box1] = box2_circuit
        elif box2 not in circuits:
            box1_circuit = circuits[box1]
            box1_circuit.add(box2)
            circuits[box2] = box1_circuit
        else:
            box1_circuit = circuits[box1]
            box2_circuit = circuits[box2]
            if box1_circuit is not box2_circuit:
                new_circuit = box1_circuit | box2_circuit
                for box in new_circuit:
                    circuits[box] = new_circuit

        circuit = circuits[box1]
        if len(circuit) == len(junction_boxes):
            print(box1.x * box2.x)
            return


        

def euclidean_dist(box1, box2):
    return math.sqrt(((box1.x - box2.x)**2) + ((box1.y - box2.y)**2) + ((box1.z - box2.z)**2))

class connection:
    def __init__(self, box1, box2):
        self.boxes = [box1, box2]
        self.distance = euclidean_dist(box1, box2)

@dataclass(frozen=True)
class junction_box:
    x: int
    y: int
    z: int


if __name__ == "__main__":
    main()