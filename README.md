# React-Django-To-Do-app

Here is a small Django + react application that will manage your tasks :yum:

## Installation 

+ Use a python virtual environment such as [pipenv](https://realpython.com/pipenv-guide/) or [virtualenv](https://pypi.org/project/virtualenv/)

```bash 
pipenv install 
```
Or if you are using virtualenv
```bash
source env/bin/activate && pip install -r requirements.txt
```

+ Move to the **frontend** folder and install the dependencies

```bash
cd frontend/ && npm install
```

## Usage 

First, start the server(our API)
```bash
python manage.py runserver 
```
Second, launch the react application (make sure you are in the **frontend** folder)
```bash
cd frontend/ && npm start
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. :relaxed:
