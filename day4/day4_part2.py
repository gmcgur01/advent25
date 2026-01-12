import re
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    rows_of_paper = []

    try:
        with open(sys.argv[1]) as file:
           for line in file:
               rows_of_paper.append([c == '@' for c in line.strip()])
        
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    num_rows = len(rows_of_paper)
    num_cols = len(rows_of_paper[0])

    total_removed = 0
    removed_last_round = -1
    while removed_last_round != 0:

        removed_last_round = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if rows_of_paper[row][col] and is_paper_accessible(row, col, rows_of_paper):
                    removed_last_round += 1
                    rows_of_paper[row][col] = False
        
        total_removed += removed_last_round

    print(total_removed)

def is_paper_accessible(row, col, rows_of_paper):
    num_rows = len(rows_of_paper)
    num_cols = len(rows_of_paper[0])

    total = 0

    for row_adjust in range(-1, 2):

        if row_adjust == -1 and row == 0:
            continue
        if row_adjust == 1 and row == num_rows - 1:
            continue


        for col_adjust in range(-1, 2):

            if col_adjust == -1 and col == 0:
                continue
            if col_adjust == 1 and col == num_cols - 1:
                continue
            if row_adjust == 0 and col_adjust == 0:
                continue

            if rows_of_paper[row + row_adjust][col + col_adjust]:
                 total += 1

    return total < 4




if __name__ == "__main__":
    main()