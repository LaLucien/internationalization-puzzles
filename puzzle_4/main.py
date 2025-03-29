import re

DAY = 4
FILE = "puzzle.txt"
FILE = "test.txt"


def getInput():

    with open(f"puzzle_{DAY}/{FILE}", "r", encoding="utf-8") as file:
        input = file.readlines()

    return [
        (input[i].strip("\n"), input[i + 1].strip("\n"))
        for i in range(0, len(input), 3)
    ]


def solve1(input: list[tuple[str, str]]) -> int:
    for trip in input:
        departure_str = trip[0]
        arrivel_str = trip[1]

        dep_tz_match = max(
            re.search(r"([A-Z,a-z,_]+/)+[A-Z,a-z,_]+", departure_str).regs
        )
        dep_tz = departure_str[dep_tz_match[0] : dep_tz_match[1]]
        print(dep_tz)

    return


if __name__ == "__main__":
    input = getInput()
    sol1 = solve1(input)

    print(f"Solution 1: {sol1}")
