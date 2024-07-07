# MYPACKAGE 

This is a template package to start from with new packages.

## Starting new project with this template
Copy this template and adjust all the information and names according to the current
project you want to do. 

Delete the venv folder as it should be newly created. Navigate to the projects root 
folder and run...
```
python -m venv venv
venv/Scripts/activate
```
For the documentation of the project some packages are needed first. Install them with 
the activated venv using...
```
pip install mkdocs
pip install "mkdocstrings[python]
pip install mkdocs-material
```
## Example Documentation

Before using this package be sure you have a version of python 3 installed on your device.
You can get this from the official [Python Website](https://www.python.org/downloads/)

Clone this repository using git 
```
git clone https://github.com/julianzulehner/mypackage.git
```

Navigate to the folder in which you cloned the repo and install the package using pip.
```
pip install .
```