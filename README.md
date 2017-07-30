# Setup
---
## Prerequisite

**Python3** installed

## Installing Python

First, check to see if **Python3** is already installed on your machine:

```` sh
# Mac Terminal:
which python3 # check for Python Version 3.x

# Windows Command Prompt:
where python
````

If **Python3** is not installed, follow the OS-specific instructions below to install it.

If Python version 2.x is installed, [please upgrade to 3.x](https://wiki.python.org/moin/Python2orPython3)

Once **Python3** is installed, you should be able to run `python3` and `pip3`, from the command-line. And you should be able to check which version of each you have installed:

```shell
# Using Python 3:
python3 --version #> Python 3.x.x
pip3 --version #> pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
```
### Windows OS

Download Python 3 from the [Python website](https://www.python.org/downloads/).

Note: Make sure you check the option, "Add Python 3.6 to PATH" when you are installing Python from the downloaded installer. 

### Mac OS

You may download Python 3 from the [Python website](https://www.python.org/downloads/), but you are encouraged to use the [Homebrew](https://brew.sh/) package manager to install it.

Check to see if Homebrew is installed:

```` sh
which brew
````

Install Homebrew if necessary:

```` sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

[Use Homebrew to install Python 2.x or 3.x](http://docs.brew.sh/Homebrew-and-Python.html) and follow any post-installation instructions:

To install Python 2.x (not recommended):

```` sh
brew install python
brew linkapps python
````

To install Python 3.x (recommended):

```` sh
brew install python3
````

> NOTE: If you choose to install Python 3 on a Mac using Homebrew, be aware that if you see references to running `python` you should instead run `python3`, and if you see references to `pip` you should instead run `pip3`.

## Install Required Packages
