# Advent of Code -- Python

This repository is based on my goto template for Python projects using [Poetry][poetry].
You can find the template [HERE][py-template].

## Setup

1. Follow the instructions in [my template repository][py-template]
2. Run `poetry install`

## Development

```
$> poetry install
$> advent_of_code --year $year --day $day
```

The above will create one solution file: `src/advent_of_code/y${year}/d${day}.py` and one
test file in `tests/y${year}/test_d${day}.py`.
Write your solution in the solution file and re-run the `advent_of_code ...` command to run
your solution.
Run your tests by running: `pytest`.

<!-- REFERENCES -->
[poetry]: https://python-poetry.org/
[py-template]: https://github.com/erikThorsell/poetry_project_template
