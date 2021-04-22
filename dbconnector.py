class dbconnect:
    
    def __init__(self):
        import mysql.connector

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            auth_plugin='mysql_native_password'
        )
        
        cur = mydb.cursor()

    def validate(self, uname, passw):
        
        if val:
            resp = {
                "validate": 1,
                "message": "Login Successful",
                "uname": uname
            }
        else:
            resp = {
                "validate": 0,
                "message": "Login Unsuccessful",
            }
        
        return resp

    def signon(self, uname, passw):
        
        if val:
            resp = {
                "validate": 1,
                "message": "Login Successful",
                "uname": uname
            }
        else:
            resp = {
                "validate": 0,
                "message": "Login Unsuccessful",
            }
        
        return resp

if __name__ == "__main__":
    db = dbconnect()