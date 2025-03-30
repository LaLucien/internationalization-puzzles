DAY = 5
FILE = "puzzle.txt"
# FILE = "test.txt"


def getInput():

    with open(f"puzzle_{DAY}/{FILE}", "r", encoding="utf-8") as file:
        input = file.readlines()

    return [[c for c in line.strip("\n")] for line in input]


def solve1(input):
    shit_count = 0

    column_length = len(input[0])
    column = 0
    for row in input:
        if row[column] == "💩":
            shit_count += 1
        column = (column + 2) % column_length

    return shit_count


if __name__ == "__main__":
    input = getInput()
    sol1 = solve1(input)

    print(f"Solution 1: {sol1}")
