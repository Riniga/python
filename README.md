# Development using virtual environment
## Preparation
py -m pip install --upgrade pip
py -m pip install --user virtualenv

### Creates and activates an environment in folder <name> 
python -m venv <name>
.\<name>\Scripts\activate

## Manage packages packages (pip)
List installed packages: pip list 



## Virtual environment for machine learning
py -m venv machinelearning -r requirements.txt
.\machinelearning\Scripts\activate
