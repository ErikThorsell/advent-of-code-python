"""A very nice main module!"""
import argparse
import importlib


def _parse_args():
    """The argument parser that allows us to specify the year and day!"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--year")
    parser.add_argument("--day")

    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    runner_str = f"advent_of_code.y{args.year}.d{args.day}"
    runner = importlib.import_module(runner_str)
    runner.run()
