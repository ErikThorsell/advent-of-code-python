"""A very nice main module!"""
import argparse
from datetime import datetime
import importlib
from pathlib import Path
from string import Template
import time

from shutil import copyfile


def _parse_args():
    """The argument parser that allows us to specify the year and day!"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--year")
    parser.add_argument("--day")

    return parser.parse_args()


def _pre_processing(year: int, day: int):
    """Check whether the appropriate files exist and create them if needed."""

    data_dir_path = Path(f"src/advent_of_code/data/{year}")
    if not data_dir_path.exists():
        data_dir_path.mkdir(parents=True)
        print(f"The input will be stored in: {data_dir_path}/{day}.input")

    solution_dir_path = Path(f"src/advent_of_code/y{year}")
    solution_path = Path(f"src/advent_of_code/y{year}/d{day}.py")
    if not solution_dir_path.exists():
        solution_dir_path.mkdir(parents=True)

    if not solution_path.exists():
        with open("templates/src.py") as in_f:
            src = Template(in_f.read())
            out = src.substitute({"day": day, "year": year})
        with open(solution_path, 'w') as out_f:
            out_f.write(out)

        print(f"A solution template has been created in: {solution_path}")


def main() -> None:
    args = _parse_args()

    today = datetime.now()

    print()
    if not (args.day or args.year):
        print(f"No year nor day specified, presuming today's puzzle: Day: {today.day}, Year: {today.year}")

        _pre_processing(today.year, today.day)
        runner_str = f"advent_of_code.y{today.year}.d{today.day}"
        runner = importlib.import_module(runner_str)
        runner.run(today.year, today.day)

    elif not args.day:
        python_files = list(Path(f"src/advent_of_code/y{args.year}").glob("*.py"))
        python_files = sorted([int(pf.stem.replace("d", "")) for pf in python_files])

        tic = time.perf_counter()
        for pf in python_files:
            runner_str = f"advent_of_code.y{args.year}.d{pf}"
            runner = importlib.import_module(runner_str)
            runner.run(args.year, pf)
            toc = time.perf_counter()
            print(f"Running total (execution time): {toc-tic:0.4f}s")

        print()
        print(f"🌟 Solutions for year {args.year} acquired in: {toc-tic:0.4f} seconds! 🌟")
    
    elif not args.year:
        print(f"No year specified, presuming this year: {today.year}")

        _pre_processing(today.year, args.day)
        runner_str = f"advent_of_code.y{today.year}.d{args.day}"
        runner = importlib.import_module(runner_str)
        runner.run(today.year, args.day)

    else:
        _pre_processing(args.year, args.day)
        runner_str = f"advent_of_code.y{args.year}.d{args.day}"
        runner = importlib.import_module(runner_str)
        runner.run(args.year, args.day)
