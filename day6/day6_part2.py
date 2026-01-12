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

            operator_columns = []
            for index, c in enumerate(lines[-1]):
                if not c.isspace():
                    operator_columns.append(index)

            space_columns = [index - 1 for index in operator_columns if index > 0]
            space_columns.append(len(lines[0]) - 1)

            for index, column in enumerate(range(len(space_columns))):
                start = 0 if column == 0 else end + 1
                end = space_columns[column]

                problems[index] = [None for _ in range(end - start)]

                for problem_idx, col_index in enumerate(reversed(range(start, end))):
                    for line_index in range(len(lines) - 1):
                        c = lines[line_index][col_index]
                        if not c.isspace():
                            problems[index][problem_idx] = add_digit(int(c), problems[index][problem_idx])

            answers = [0 for _ in range(num_problems)]
            for index, operator in enumerate(lines[len(lines) - 1].strip().split()):
                nums = [num for num in problems[index] if num is not None]
                if operator == "+":
                    answers[index] = sum(nums)
                elif operator == "*":
                    answers[index] = product(nums) 
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

def add_digit(digit, other):
    if other is None:
        return digit
    return other * 10 + digit

if __name__ == "__main__":
    main()