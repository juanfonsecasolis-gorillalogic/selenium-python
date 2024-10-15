# selenium-python
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
pip install selenium
pip install pytest
pip list
```

## Run
```
pytest
```

## Dev Chrome tools
```
$x('//input[@id="username"]')
```

## References
1. PyPA. Install packages in a virtual environment using pip and venv. URL: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ (last consulted on Oct 15th 2024)
2. Dmitry Shyshkin. Practice Test Automation. URL: https://www.practicetestautomation.com/practice-test-login (last consulted on Oct 15th 2024)