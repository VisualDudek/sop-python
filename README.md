# sop-python
Standard Operation Procedure for Python

This SOP outlines the procedures and best practices for Python development to ensure consistency, quality, and maintainability of code.

## 1 Setup repo
- Create (public) GitHub repo
-  create `.gitignore` using [gh collection of useful .gitignore templates](https://github.com/github/gitignore)

## 2. Environment Setup

### 2.1 Install Python
- ~~Download the latest version of Python from [python.org](https://www.python.org/downloads/).~~

### 2.2 Set Up Virtual Environment
- Use virtual environments to manage dependencies for different projects.
-  Do not use `python -m venv`

#### 2.2a Setup `pyenv`
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

### 2.3 Install Dependencies
- Create a `requirements.txt` file to list project dependencies.
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

