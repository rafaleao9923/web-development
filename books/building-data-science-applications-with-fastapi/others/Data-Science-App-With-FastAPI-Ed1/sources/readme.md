# <p style="text-align: center;">Building Data Science Applications with FastAPI</p>

## Table of Contents

- [Building Data Science Applications with FastAPI](#building-data-science-applications-with-fastapi)
  - [Table of Contents](#table-of-contents)
  - [Python Development Environment Setup](#python-development-environment-setup)
    - [Technical requirements](#technical-requirements)
    - [Installing a Python distribution using pyenv](#installing-a-python-distribution-using-pyenv)
    - [Creating a Python virtual environment](#creating-a-python-virtual-environment)
    - [Installing Python packages with pip](#installing-python-packages-with-pip)
    - [Installing the HTTPie command-line utility](#installing-the-httpie-command-line-utility)
  - [Python Programming](#python-programming)
  - [Developing a RESTful API](#developing-a-restful-api)
  - [Managing Pydantic Data Models](#managing-pydantic-data-models)
  - [Dependency Injections](#dependency-injections)
  - [Databases and Asynchronous ORMs](#databases-and-asynchronous-orms)
  - [Managing Authentication and Security in FastAPI](#managing-authentication-and-security-in-fastapi)
  - [Defining WebSockets for Two-Way Interactive Communication](#defining-websockets-for-two-way-interactive-communication)
  - [Testing an API Asynchronously with pytest and HTTPX](#testing-an-api-asynchronously-with-pytest-and-httpx)
  - [Deploying](#deploying)
  - [NumPy and pandas](#numpy-and-pandas)
  - [scikit-learn](#scikit-learn)
  - [Creating an Efficient Prediction API Endpoint](#creating-an-efficient-prediction-api-endpoint)

## <p style="text-align: center;">Python Development Environment Setup</p>

### Technical requirements

- Unix-based environment (Linux or macOS)

### Installing a Python distribution using pyenv

```bash
sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

```bash
curl https://pyenv.run | bash
```

```bash
nano ~/.profile
```

Add the following lines before the block containing ~/.bashrc

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
```

```bash
nano ~/.bashrc
```

Add the following line at the end:

```bash
eval "$(pyenv init -)"
```

```bash
source ~/.profile && exec $SHELL
```

install the Python distribution of our choice then set it as the default Python version

```bash
pyenv install 3.7.10
pyenv global 3.7.10
```

### Creating a Python virtual environment

```bash
mkdir fastapi-data-science
cd fastapi-data-science
python -m venv
source venv/bin/activate
```

### Installing Python packages with pip

```bash
pip install fastapi uvicorn[standard]
pip install sqlmodel
```

### Installing the HTTPie command-line utility

```bash
sudo apt-get update; sudo apt-get install httpie
```

## <p style="text-align: center;">Python Programming</p>
## <p style="text-align: center;">Developing a RESTful API</p>
## <p style="text-align: center;">Managing Pydantic Data Models</p>
## <p style="text-align: center;">Dependency Injections</p>
## <p style="text-align: center;">Databases and Asynchronous ORMs</p>
## <p style="text-align: center;">Managing Authentication and Security in FastAPI</p>
## <p style="text-align: center;">Defining WebSockets for Two-Way Interactive Communication</p>
## <p style="text-align: center;">Testing an API Asynchronously with pytest and HTTPX</p>
## <p style="text-align: center;">Deploying</p>
## <p style="text-align: center;">NumPy and pandas</p>
## <p style="text-align: center;">scikit-learn</p>
## <p style="text-align: center;">Creating an Efficient Prediction API Endpoint</p>