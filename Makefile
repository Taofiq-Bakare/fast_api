# To automate my development process


# generate hashes from the .in file
# and add output it to the requirements file
get-requirements:
	python -m piptools compile --generate-hashes requirements/prod_requirements.in --output-file requirements/prod_requirements.txt &&\
	python -m piptools compile --generate-hashes requirements/dev_requirements.in --output-file requirements/dev_requirements.txt

# install the basic tools needed for the environment
install:
	python -m pip install --upgrade pip &&\
	python -m pip install --upgrade pip-tools &&\
	python -m pip install --upgrade pre-commit &&\
	pre-commit install

install-prod: get-requirements install
	python -m pip install -r requirements/prod_requirements.txt

install-dev: get-requirements install
	python -m pip install -r requirements/dev_requirements.txt

install-all: get-requirements install-dev install-prod

# use the coverage module to run the test
# and display the report of the coverage
test:
	coverage run -m unittest -v tests/cli_functions_test.py &&\
	coverage report -m

run-app:
	python -m main

lint:
	- python -m flake8 . &&\
	python -m interrogate  .
