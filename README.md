# sop-python
Standard Operation Procedure for Python

This SOP outlines the procedures and best practices for Python development to ensure consistency, quality, and maintainability of code.

## 1 Setup repo
- Create (public) GitHub repo
-  create `.gitignore` using [gh collection of useful .gitignore templates](https://github.com/github/gitignore)

## 2. Environment Setup

### 2.1 Install Python
- ~~Download the latest version of Python from [python.org](https://www.python.org/downloads/).~~ -> use `pyenv` or devcontainer

### 2.2 Set Up Virtual Environment
- Use virtual environments to manage dependencies for different projects.
-  Do not use `python -m venv`

#### 2.2a Setup `pyenv` or use devcontainer
- (install python version):
```bash
pyenv install 3.12
```
- Create a virtual environment:
```bash
pyenv virtualenv 3.12 myenv-3.12
```
- Set a local Python version (specific to a directory):
```bash
pyenv local myenv-3.12
```

#### 2.2b Setup devcontainer
- use pre-build Python image
- use [devcontainer gh repo](https://github.com/devcontainers)
  - [templates](https://github.com/devcontainers/templates) or
  - [pre-built](https://github.com/devcontainers/images)

### 2.3 Install Dependencies
- Create a `requirements.txt` file to list project dependencies.
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## 3. Coding Standards

### 3.1 Follow PEP 8
- Adhere to PEP 8, the Python style guide: [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use tools like `flake8` or `pylint` to check for compliance.

### 3.2 Naming Conventions
- Use descriptive names for variables, functions, and classes.
- Follow these conventions:
  - Variables and functions: `snake_case`
  - Classes: `CamelCase`
  - Constants: `UPPER_CASE`

### 3.3 Commenting and Documentation
- Use docstrings for modules, classes, and functions.
- Follow PEP 257 for docstring conventions: [PEP 257](https://www.python.org/dev/peps/pep-0257/)
- Example:
  ```python
  def add(a, b):
      """
      Add two numbers.

      Parameters:
      a (int): The first number.
      b (int): The second number.

      Returns:
      int: The sum of the two numbers.
      """
      return a + b
  ```

## 4. Version Control

### 4.1 Use Git
- Initialize a Git repository:
  ```bash
  git init
  ```
- Create a `.gitignore` file to exclude unnecessary files.

### 4.2 Branching Strategy
- Use a branching strategy like Git Flow or feature branches.
- Example:
  - `main` or `master` for production code.
  - `develop` for development.
  - Feature branches: `feature/feature-name`

### 4.3 Commit Messages
- Write clear and concise commit messages.
- Follow this structure:
  ```
  feat: Add new feature
  fix: Fix a bug
  docs: Update documentation
  style: Improve code style (e.g., formatting)
  refactor: Refactor code (no functional changes)
  test: Add or update tests
  chore: Miscellaneous tasks (e.g., build process)
  ```


