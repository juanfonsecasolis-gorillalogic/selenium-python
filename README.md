# selenium-python

[![Python application](https://github.com/juanfonsecasolis-gorillalogic/selenium-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/juanfonsecasolis-gorillalogic/selenium-python/actions/workflows/python-app.yml)

2024 Juan M. Fonseca-Solís

Gorilla Logic, Sabana Business Center 10th Floor, Bv. Ernesto Rohrmoser, San José.

## Description
Practice for course https://gorillalogic.udemy.com/course/selenium-webdriver-python-course

## Install Python
```
brew install python
echo "export PATH=/usr/local/opt/python@3.13/libexec/bin:$PATH" >> ~/.zshrc
pip -V
```

## Virtual environments [1]
Create, activate, and deactivate a virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
which python
deactivate
```

## Setup
```
pip install -r requirements.txt
```

## Run
For short, use:
```
pytest -n=auto --html=reports/report.html
```

All options available:
```
pytest -m <testSuiteMarkName> -n=auto --browser:Chrome --html=reports/report.html
```

Where:
* n is the number of threads (auto means using all available CPUs).

## Inspect web elements using the Dev Chrome tools
```
$x('//input[@id="username"]')
```

## References
1. PyPA. Install packages in a virtual environment using pip and venv. URL: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ (last consulted on Oct 15th 2024)
2. Dmitry Shyshkin. Practice Test Automation. URL: https://www.practicetestautomation.com/practice-test-login (last consulted on Oct 15th 2024)