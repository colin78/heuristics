VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(PYTHON) -m pip

.PHONY: install language-install global-install test format refactor lint all

$(PYTHON):
	python3 -m venv $(VENV)

install: $(PYTHON)
	##non-gpu version
	$(PIP) install --upgrade pip && $(PIP) install -r requirements.txt
	####optimizing for conda in GPU environment
	#conda env create -f environment.yml
	#conda activate heuristics

language-install:
	installs/setup_rust.sh
	installs/setup_swift.sh

global-install: install language-install

test: $(PYTHON)
	#ignores the virus of pandas warnings
	$(PYTHON) -m pytest -vv -p no:warnings test_*.py tests/

format: $(PYTHON)
	$(PYTHON) -m black .

refactor: format lint

lint: $(PYTHON)
	find . -type f -name "*.py" \
	 | xargs $(PYTHON) -m pylint --disable=R,C --ignore-patterns=test_.*?py 

all: install lint test
