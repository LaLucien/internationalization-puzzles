from datetime import datetime, timezone
import numpy as np

DAY = 2
FILE = "puzzle.txt"
# FILE = "test.txt"


def getInput():

    with open(f"puzzle_{DAY}/{FILE}", "r", encoding="utf-8") as file:
        input = [
            datetime.fromisoformat(line.strip()).astimezone(timezone.utc)
            for line in file.readlines()
        ]

    return input


def solve1(input: list[int]):
    counts = np.unique_counts(input)
    valid = counts.values[counts.counts >= 4]

    return "\n".join([datetime.isoformat(date) for date in valid])


if __name__ == "__main__":
    input = getInput()
    sol1 = solve1(input)

    print(f"Solution: \n{sol1}")
