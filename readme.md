# Project Title

## Overview
This project is designed to Machine Learning Response API Detection. It uses Python 3.13 and several essential packages such as `requests`, `ipython`, `pandas`, and `scikit-learn`.

## Prerequisites
- Python 3.13.0
- `pip` (Python package installer)

## Depedencies
- `joblib`
- `flask`
- `pymongo`
- `scikit-learn`
- `python-dotenv`

These dependencies are managed by `pipenv` and are specified in the `Pipfile`.

## Installation

### Step 1: Install `pipenv`
`pipenv` is a tool that aims to bring the best of all packaging worlds (bundled, development, and deployment) to the Python world. It automatically creates and manages a virtual environment for your projects and adds/removes packages from your `Pipfile` as you install/uninstall packages.

To install `pipenv`, run the following command:
```
pip install pipenv
```

### Step 2: Set Up the Project Environment
Navigate to the project directory and install the dependencies specified in the `Pipfile`:
```
cd path/to/your/project
pipenv install
```
This will create a virtual environment and install all the packages listed in the `Pipfile`.

### Step 3: Activate the Virtual Environment
To activate the virtual environment created by `pipenv`, run:
```
pipenv shell
```

### Step 4: Run the Python Script
Once the virtual environment is activated, you can run the main Python script using the following command:
```
pipenv run start
```