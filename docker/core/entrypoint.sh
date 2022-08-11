#!/bin/bash

pip install -e .[dev]
python -m unittest discover tests
