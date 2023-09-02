# Difference game

-------------------------------------
Getting Started
To get started, you will need to have Python 3.8+ installed. You can install the dependencies by running the following commands:

```cd differences/back```

```poetry install```

```poetry shell```

This will install all the dependencies in the poetry.lock file and create a virtual environment.

Then for starting the backend 

```python app.py```

Once the dependencies are installed, you can start the front by running the following commands:

```cd differences```

```npm install```

```npm run dev```

create a .env file int the root with the variable SQLALCHEMY_DATABASE_URI="your database url"  and another one inside the trivia-front folder with the name VITE_BACKEND_URL="the url of your backend"
  
Then for setting up the db (inside the poetry shell)

```flask db init```

```flask db migrate```

```flask db upgrade```
