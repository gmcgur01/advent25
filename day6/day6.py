import re
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            num_problems = len(lines[0].strip().split())

            problems = [[] for _ in range(num_problems)]

            for i in range(len(lines) - 1):
                line = lines[i]
                for index, num_str in enumerate(line.strip().split()):
                    problems[index].append(int(num_str))

            answers = [0 for _ in range(num_problems)]
            for index, operator in enumerate(lines[len(lines) - 1].strip().split()):
                if operator == "+":
                    answers[index] = sum(problems[index])
                elif operator == "*":
                    answers[index] = product(problems[index]) 
                else:
                    print("Unknown operator " + operator)
                    sys.exit(1)

                    
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    print(sum(answers))

def product(nums):
    product = 1
    for num in nums:
        product *= num
    return product

if __name__ == "__main__":
    main()