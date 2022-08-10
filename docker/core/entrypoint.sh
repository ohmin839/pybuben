#!/bin/bash

pip install -r requirements.txt
python -m unittest discover tests

# python setup.py develop --user
# source ~/.profile
