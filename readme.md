# IS601 Homework 6-- summer 2024
# Submission Details


# Installation Instructions

1. Install Python/Pip/Virtualenv, or ensure it is installed. 
```
sudo apt update -y
sudo apt install python3-pip
python3 --version
pip3 --version
pip3 install virtualenv
virtualenv --version
```
```
pip install faker
```


2. Clone this repo
```
git clone git@github.com:fcamacho3/IS601homework6--summer-2024.git
cd IS601homework6--summer-2024
```

3. Create virtual environment\
Use `ls` to ensure `venv` folder is created\
Install project requirements
```
virtualenv venv
ls
```
4. Install requirements
```
pip3 install -r requirements.txt
```
If needed install pytest seperately
```
pip3 install pytest pytest-pylint pytest-cov
```

5. Run the pytest to see 100% coverage
```
pytest --pylint --cov
pytest --num_records=20
```

6. Run main.py to see calculator in action
```
python main.py 5 6 add
```

# Note
All code was written on my own except for .pylintrc and pytest.ini



