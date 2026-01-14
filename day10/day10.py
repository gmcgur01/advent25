import re
import sys
from dataclasses import dataclass
import math
from collections import deque


def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")


    try:
        with open(sys.argv[1]) as file:
            problems = [problem.parse_line(line) for line in file]
                
                    
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    print(sum([p.solve_problem() for p in problems]))

class problem:

    @staticmethod
    def parse_line(line):
        if match := re.match(r"\[((?:\.|#)+)\] ((?:\((?:\d+,?)+\) ?)+)", line):
            goal = tuple([c == "#" for c in match.group(1)])

            def parse_button(button_str):
                return {int(num) for num in button_str[1:len(button_str)-1].split(",")}
            buttons = [parse_button(button_str) for button_str in match.group(2).split()]
            
            return problem(goal, buttons)
        else:
            print("didn't match: " + line)

    @staticmethod
    def press_button(old_state, button):
        return tuple([not slot if index in button else slot for index, slot in enumerate(old_state)])


    def __init__(self, goal, buttons):
        self.goal = goal
        self.buttons = buttons

    def solve_problem(self):
        start_state = tuple([False for _ in range(len(self.goal))])

        queue = deque([(start_state, 0)])
        seen_states = set()
        while len(queue) != 0:
            state, steps = queue.popleft()
            steps += 1
            for button in self.buttons:
                new_state = problem.press_button(state, button)
                if new_state == self.goal:
                    return steps
                elif new_state not in seen_states:
                    seen_states.add(new_state)
                    queue.append((new_state, steps))

        return -1

if __name__ == "__main__":
    main()