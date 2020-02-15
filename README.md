# Dependencies 

## Packages

Using python virtual environments is advised. Afterwards use pip to install dependencies.

```
pip install -r requiremnets.txt
```

## Environment variables

To successfully run a flask application, ensure that you set the following environment variables.

### Linux
```
export FLASK_APP=flashcards.py
export FLASK_ENV=development
```

### Windows
```
set FLASK_APP=flashcards.py
set FLASK_ENV=development
```

# Running the application
```
flask run
```
