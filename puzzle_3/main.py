DAY = 3
FILE = "puzzle.txt"
# FILE = "test.txt"


def getInput():

    with open(f"puzzle_{DAY}/{FILE}", "r", encoding="utf-8") as file:
        input = file.readlines()

    return [pw.strip() for pw in input]


def solve1(input: list[str]) -> int:
    valid_count = 0
    for line, pw in enumerate(input):
        if len(pw) not in range(4, 13):
            continue
        if not any([char.isdigit() for char in pw]):
            continue
        if not any([char.isupper() for char in pw]):
            continue
        if not any([char.islower() for char in pw]):
            continue
        if all([ord(char) in range(32, 128) for char in pw]):
            continue

        # valid password
        print(f"line {line+1}: {pw} is considered valid")
        valid_count += 1

    return valid_count


if __name__ == "__main__":
    input = getInput()
    sol1 = solve1(input)

    print(f"Solution 1: {sol1}")
