# Simple Pytest Example

This is the code for my video tutorial for getting started with Pytest.

* [Pytest Documentation](https://docs.pytest.org/en/6.2.x/getting-started.html#getstarted)
* [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)

### Install Pytest

```bash
pip install pytest
```

### Run the tests

```bash
pytest
```

### Run a specific file

```bash
pytest test_shopping_cart.py
```

### Run a specific test

```bash
pytest test_shopping_cart.py::test_can_get_total_price
```

# poetry install

## Get Python 3.10.7 Install on windows
https://www.tomshardware.com/how-to/install-python-on-windows-10-and-11

## Update Path with the Python install and Scripts folder

### For Poetry
https://github.com/python-poetry/install.python-poetry.org

### Update Path with the Poetry Install  folder
~\AppData\Roaming\Python\Scripts

### start cmd shell: check poetry version
```bash
poetry --version 
```

### Once Poetry Installed. Go to project folder: to create pyproject.toml file
```bash
poetry init
```

### Modify config parm to change path of venv folder within project
```bash
poetry config virtualenvs.in-project true
```

### Create virtual env using Poetry
```bash
poetry install
```

### Activate virtual env using Poetry
```bash
poetry shell
```

### list packages in venv
```bash
poetry show
```

### add packages in venv
```bash
poetry add <pkgname>
```

### remove packages in venv
```bash
poetry remove <pkgname>
```

### pytest specific function

```bash
pytest test_shopping_cart.py::test_can_get_total_price
```

```bash
pytest test_shopping_cart.py::test_can_get_total_price_p2
```
