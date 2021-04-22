class dbconnect:
    
    def __init__(self):
        import mysql.connector

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            auth_plugin='mysql_native_password',
            database="RESA"
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

    def __del__(): 
        cur.close()
        
if __name__ == "__main__":
    db = dbconnect()