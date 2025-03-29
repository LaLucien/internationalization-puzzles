import re
from datetime import datetime
from zoneinfo import ZoneInfo
import calendar

DAY = 4
FILE = "puzzle.txt"
# FILE = "test.txt"


def getInput():

    with open(f"puzzle_{DAY}/{FILE}", "r", encoding="utf-8") as file:
        input = file.readlines()

    return [
        (input[i].strip("\n"), input[i + 1].strip("\n"))
        for i in range(0, len(input), 3)
    ]


def get_datetime(datetime_str: str) -> datetime:
    """only useful to convert this string: "Departure: Europe/London                  Jan 12, 2020, 06:00" to a datime object"""
    datetime_list_with_tz = re.findall(r"\S+", datetime_str)
    timezone = ZoneInfo(datetime_list_with_tz[1])
    datetime_list = datetime_list_with_tz[2:]
    time_list = datetime_list[-1].split(":")
    return datetime(
        int(datetime_list[2].strip(",")),
        list(calendar.month_abbr).index(datetime_list[0]),
        int(datetime_list[1].strip(",")),
        int(time_list[0]),
        int(time_list[1]),
        tzinfo=timezone,
    )


def solve1(input: list[tuple[str, str]]) -> int:
    duration = 0
    for trip in input:
        departure = get_datetime(trip[0])
        arrival = get_datetime(trip[1])
        duration += (arrival - departure).seconds // 60

    return duration


if __name__ == "__main__":
    input = getInput()
    sol1 = solve1(input)

    print(f"Solution 1: {sol1}")
