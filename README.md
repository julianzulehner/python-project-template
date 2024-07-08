# MYPROJECT 

This is a template Python project package to start from.

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

As we want to automate the building processes or tests on each push, we will create a
git repository...
```
git init
git add --all
git commit -m "Initial Commit"
```

This repository is only locally available to create a remote repository, refer to the 
instructions of the used provider (github, gitlab, sourcetree, etc.)

- [Create a new repo with GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

Once the repo is created continue with the necessary steps.

```
git remote add origin git@github.com:<github username>/<repository name>.git
git branch -M main
git push -u origin main
```
## Example Documentation

Before using this package be sure you have a version of python 3 installed on your device.
You can get this from the official [Python Website](https://www.python.org/downloads/)

Clone this repository using git 
```
git clone https://github.com/<github username>/<repository name>.git
```

Navigate to the folder in which you cloned the repo and install the package using pip.
```
pip install .
```

This template package uses the documentation builder MkDocs which is markdown based. To 
initiate a new documentation run the following command. In this case this was already 
done, so it is not needed to repeat this step.

```
mkdocs new .
```

To start a live server that hosts the documentation created by MkDocs you can run...
```
mkdocs serve
```
This is especially useful during development. Once this is done, to build the documentation 
run...
```
mkdocs build
```
Now that the documentation is ready, you can host it on github (or a different server). To host
it on github run the following command (assuming that the repository is already available)
```
mkdocs gh-deploy
```
