# Advent of Code -- Python

This repository is based on my goto template for Python projects using [Poetry][poetry].
You can find the template [HERE][py-template].

## Setup

1. Follow the instructions in [my template repository][py-template]
2. Run `poetry install`

## Development

```
$> poetry install
$> pip install setup_tools   # <-- needed for z3-solver
$> advent_of_code --year $year --day $day
```

The above will create one solution file: `src/advent_of_code/y${year}/d${day}.py` and one
test file in `tests/y${year}/test_d${day}.py`.
Write your solution in the solution file and re-run the `advent_of_code ...` command to run
your solution.
Run your tests by running: `pytest`.

## Previous years

- I did [2020 in Golang](https://github.com/ErikThorsell/advent-of-code-go)
- I have done the first days of 2019 in the Golang repository and in this, but I really do not
  like the Intcode missions so I cannot motivate myself to continue past day 5...
- I have solved most of 2018, but not stored the code. I might redo the missions and store them here.


<!-- REFERENCES -->
[poetry]: https://python-poetry.org/
[py-template]: https://github.com/erikThorsell/poetry_project_template
