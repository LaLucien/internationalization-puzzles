DAY = 1
FILE = "puzzle.txt"
# FILE = "test.txt"


def getInput():

    with open(f"puzzle_{DAY}/{FILE}", "r", encoding="utf-8") as file:
        input = file.readlines()

    return input


def solve1(input: list[str]):
    cost = 0
    for id, line in enumerate(input):
        line = line.replace("\n", "")
        bytes_line = line.encode("utf-8")
        if len(bytes_line) <= 160 and len(line) <= 140:
            # discount
            print(f"line {id} sms & twitter")
            cost += 13
            continue
        if len(bytes_line) <= 160:
            print(f"line {id} sms")
            cost += 11
        if len(line) <= 140:
            print(f"line {id} twitter")
            cost += 7

    return cost


if __name__ == "__main__":
    input = getInput()
    sol1 = solve1(input)

    print(f"Solution 1: {sol1}")
