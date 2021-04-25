from flask import Flask, request, jsonify
from scraper import Scraper
from dbconnector import dbconnect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

db_cursor = dbconnect()

@app.route('/scrape_content', methods=['POST'])
def scrape_content_api():
    if request.method == "POST":
        scraped_content = Scraper(request.form["url"])
        return jsonify(scraped_content)

@app.route('/login_user', methods=['POST'])
def login_user_api():
    if request.method == "POST":
        
        uname = request.form["username"]
        pasw = request.form["password"]

        resp = db_cursor.validate(uname, pasw)

        return jsonify(resp)

@app.route('/signup_user', methods=['POST'])
def signup_user_api():
    if request.method == "POST":
        
        uname = request.form["username"]
        pasw = request.form["password"]
        
        resp = db_cursor.signon(uname, pasw)
                
        return jsonify(resp)

@app.route('/get_user_details', methods=['POST'])
def user_details_api():
    if request.method == "POST":
        
        uname = request.form["username"]
        
        resp = db_cursor.get_user_details(uname)
                
        return jsonify(resp)

@app.route('/insert_user_recipe', methods=['POST'])
def insert_recipe_api():
    if request.method == "POST":
        
        user_email = request.form["useremail"]
        title = request.form["title"]
        ingredients = request.form["ingredients"]
        process = request.form["process"]
        
        resp = db_cursor.insert_user_recipe(user_email, title, ingredients, process)
        
        return jsonify({'inserted_recipe_id':resp})

@app.route('/get_user_recipes', methods=['POST'])
def user_recipes_api():
    if request.method == "POST":
        
        user_email = request.form["user_email"]
        
        resp = db_cursor.get_user_recipes(user_email)
        
        return jsonify(resp)

@app.route('/delete_user_recipe', methods=['POST'])
def delete_user_recipe_api():
    if request.method == "POST":
        
        user_email = request.form["user_email"]
        recipe_id = request.form["recipe_id"]
        
        resp = db_cursor.remove_user_recipe(user_email, recipe_id)
        
        return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True)