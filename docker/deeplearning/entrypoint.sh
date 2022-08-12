#!/bin/bash

pip install -e ../pybuben-core[dev]
pip install -e .[dev]
python -m notebook ./notebook --ip 0.0.0.0 --no-browser
