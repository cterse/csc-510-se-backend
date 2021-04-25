import mysql.connector
class dbconnect:
    
    def __init__(self):
        
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            # auth_plugin='mysql_native_password',
            database="dbms"
        )
        
        self.cur = self.mydb.cursor()

    def validate(self, uname, passw):
        
        self.cur.execute(f"""SELECT USER_PASSWORD from USERS where USER_EMAIL = '{uname}'""")
        pass_db = self.cur.fetchall()
        
        val = 1 if (pass_db[0][0] == passw) else 0
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
        
        
        from datetime import datetime
        date = datetime.now().date()
        val = 0
        print(date)
        self.cur.execute(f"""INSERT INTO USERS VALUES (null, '{uname}','{passw}','{date}');""")
        self.mydb.commit()
        val = 1
            
        if val:
            resp = {
                "validate": 1,
                "message": "Login Successful",
                "uname": uname
            }
        else:
            resp = {
                "validate": 0,
                "message": "User already exists",
            }
        
        return resp

    def get_user_details(self, user_email):
        sql = f" SELECT * FROM USERS WHERE USER_EMAIL = '{user_email}' "
        self.cur.execute(sql)

        return self.cur.fetchall()
    
    def get_user_recipes(self, user_email):
        sql = f" SELECT * FROM RECIPES WHERE RECIPE_ID IN (SELECT RECIPE_ID FROM USER_RECIPES WHERE USER_ID = \
        (SELECT USER_ID FROM USERS WHERE USER_EMAIL = '{user_email}') ) "
        self.cur.execute(sql)

        return self.cur.fetchall()

    def insert_user_recipe(self, user_email, title, ingredients, process):
        inserted_recipe_id = self.insert_recipe(title, ingredients, process)
        self.map_recipe_to_user(user_email, inserted_recipe_id)

        return inserted_recipe_id

    def insert_recipe(self, title, ingredients, process):
        sql = " INSERT INTO RECIPES (RECIPE_ID, RECIPE_TITLE, RECIPE_INGREDIENTS, RECIPE_PROCEDURE, RECIPE_IMAGE ) \
            VALUES (null, %s, %s, %s, null) "
        self.cur.execute(sql, (title, ingredients, process))

        self.mydb.commit()
        return self.cur.lastrowid
    
    def map_recipe_to_user(self, user_email, recipe_id):
        sql = " INSERT INTO USER_RECIPES (USER_ID, RECIPE_ID) VALUES ((SELECT USER_ID FROM USERS WHERE USER_EMAIL = %s), %s) "
        self.cur.execute(sql, (user_email, recipe_id))
        
        self.mydb.commit()
        return 0
    
    def remove_user_recipe(self, user_email, recipe_id):
        sql = " DELETE FROM USER_RECIPES WHERE RECIPE_ID = %s AND USER_ID = (SELECT USER_ID FROM USERS WHERE USER_EMAIL = %s) "
        self.cur.execute(sql, (recipe_id, user_email))

        self.mydb.commit()
        return 0

    def delete_recipe(self, recipe_id):
        sql = "  DELETE FROM RECIPES WHERE RECIPE_ID = %s "
        self.cur.execute(sql, recipe_id)

        self.mydb.commit()
        return 0

    def __exit__(self): 
        self.mydb.close()
        
if __name__ == "__main__":
    db = dbconnect().signon("g@h.com","pass123")
    print(db)