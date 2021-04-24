# se-backend
CSC 510 Project Backend

# Required Dependencies
- Python 3
- Flask
- A local MySql installation 
- Postman (for testing only)

# Testing 
1. Start the MySQL service if not running. Generally the MySQL uses port 3306.
2. Run db/SE-DDL.sql file in MySQL. This should create the 'dbms' database and create all required tables.
3. Run db/SE-DML.sql file in MySQL. This should populate the 'dbms' database tables with some test data.
4. Start the server by running the app.py module. If there are no build errors, the server should start and show a URL on the localhost for accessing the APIs.
5. Test the APIs present in flask_api.py using Postman.
