"""Module for fetching AoC Input"""
from pathlib import Path

from requests import get, HTTPError


def fetch(year: int, day: int) -> str:
    """Downloads (if necessary) and returns the input for the specified year and day.

    The function presumes there's a session cookie available in the repository: $REPO/.cookie
    """
    repo_root = Path(__file__).parent.parent.parent.parent
    cookie_path = Path(repo_root, ".cookie")
    input_path = Path(
        repo_root, "src", "advent_of_code", "data", str(year), f"{day}.input"
    )

    if input_path.exists():
        with open(input_path) as fh:
            return fh.read()

    try:
        with open(cookie_path) as fh:
            cookies = dict(session=fh.read())
    except FileNotFoundError:
        print(f"No session cookie found at path: {cookie_path}")
        raise

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = get(url, cookies=cookies)

    try:
        response.raise_for_status()
    except HTTPError as err:
        print(f"Something went wrong: {err=}")

    aoc_input = response.text.strip()

    with open(input_path, "w") as fh:
        fh.write(aoc_input)

    return aoc_input
