#!/bin/bash -xe
poetry run black --target-version py310 src/
poetry run flake8 --max-line-length=120 src/
poetry run mypy src/
