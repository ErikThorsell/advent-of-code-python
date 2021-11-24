# Advent of Code -- Python

This repository is based on my goto template for Python projects using [Poetry][poetry].
You can find the template [HERE][py-template].

## Setup

1. Follow the instructions in [my template repository][py-template]
2. Run `poetry install`

## Development

1. Create a file: `$REPO/src/advent_of_code/y${year}/d${day}.py`
2. Make sure the file has a function called: `run()`
3. Use the CLI `advent_of_code --year ${year} --${day}` to run the corresponding `run()` function

```
$> poetry install
$> advent_of_code --year $year --day $day
```

<!-- REFERENCES -->
[poetry]: https://python-poetry.org/
[py-template]: https://github.com/erikThorsell/poetry_project_template