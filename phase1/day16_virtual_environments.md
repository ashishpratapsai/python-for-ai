# Day 16 — Virtual Environments

## Commands to know forever

### Create
python -m venv venv

### Activate (Mac/Linux)
source venv/bin/activate

### Activate (Windows)
venv\Scripts\activate

### Install package
pip install package_name

### Save packages
pip freeze > requirements.txt

### Install from requirements
pip install -r requirements.txt

### Deactivate
deactivate

## Rules
- Never push venv/ or .venv/ to GitHub
- Always add to .gitignore: venv/ and .venv/
- Every project gets its own virtual environment
- Share requirements.txt not venv folder

## .gitignore must have
venv/
.venv/
__pycache__/
*.pyc
.DS_Store