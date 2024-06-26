#!/usr/bin/env bash

pre-commit run black --all-files
pre-commit run ruff --all-files
pre-commit run mypy --all-files
