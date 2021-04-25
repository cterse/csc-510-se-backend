# se-backend
CSC 510 Project Backend

# How to Run
1. Start the MySQL service if not running. Generally the MySQL uses port 3306.
2. Run db/SE-DDL.sql file in MySQL. This should create the 'dbms' database and create all required tables.
3. Run db/SE-DML.sql file in MySQL. This should populate the 'dbms' database tables with some test data.
4. Run `pip install -U pipenv` if pipenv is not installed.
5. Run `pipenv install` to install the required application dependencies.
6. Start the server by running `pipenv run python flask_api.py`. If there are no build errors, the server should start and show a URL on the localhost for accessing the APIs.
7. Test the APIs present in flask_api.py using Postman.
