# Development using virtual environment
Install conda (Anaconda) to create virtual environments
Add conda-forge channel: conda config --add channels conda-forge



## Preparation
- Kolla versioner för python: conda search python
- Skapa en miljö: conda create --name mypython python=3.13.1
- Aktivera miljö: conda activate mypython

- Installera nödvändiga paket
  - conda install ipykernel
  - conda install pytz
  - conda install astral


py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv machinelearning
.\machinelearning\Scripts\activate
py -m pip install -r requirements.txt

### Creates and activates an environment in folder <name> 
python -m venv <name>
.\<name>\Scripts\activate

## Manage packages packages (pip)
List installed packages: pip list 

## Virtual environment for machine learning
py -m venv machinelearning -r requirements.txt
.\machinelearning\Scripts\activate
