"""Module for fetching AoC Input"""
from pathlib import Path

from requests import get


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
            cookies = dict(session=fh.read().strip())
    except FileNotFoundError:
        print(f"No session cookie found at path: {cookie_path}")
        raise

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = get(url, cookies=cookies)
    response.raise_for_status()

    aoc_input = response.text.strip()
    print("-" * 15, " START OF INPUT ", "-" * 15)
    print(aoc_input)
    print("-" * 16, " END OF INPUT ", "-" * 16)

    with open(input_path, "w") as fh:
        fh.write(aoc_input)

    return aoc_input
