import mysql.connector
class dbconnect:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            auth_plugin='mysql_native_password',
            database="dbms"
        )
        
        self.cur = self.mydb.cursor()

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

    def user_details(self, user_email):
        sql = " SELECT * FROM USERS WHERE USER_EMAIL = %s "

        self.cur.execute(sql, (user_email,))

        return self.cur.fetchall()
        

    def __del__(self): 
        self.cur.close()
        
if __name__ == "__main__":
    db = dbconnect()