# unittests-hello-world
Here is an example of how to cover python script by unit tests, analyze code coverage, and review project style.

## How to prepare all the needed modules.
To install all required modules need to execute:
```
pip install -r requirements.txt
```

## Check project state.
To run unit tests and view the results, you need to run the following command:
```
fab unittest
```
To check code coverage, you need to run the following command:
```
fab check-coverage
```
First of all, will be run unit tests. If all tests passed successfully, will be retrieved code coverage. Full code coverage report available in the following folder:
```
htmlcov
```
To check compliance with the PEP8 style, run the following command:
```
fab check-pep
```
To run all checks, you need to do:
```
fab check
```
The following command show all available commands:
```
fab --list
```
