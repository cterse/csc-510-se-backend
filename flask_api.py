from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from scraper import Scraper
from dbconnector import dbconnect
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://localhost:4200", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials","Access-Control-Allow-Origin"],
    supports_credentials=True, intercept_exceptions=False)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

app.config["DEBUG"] = True

db_cursor = dbconnect()

@app.route('/scrape_content', methods=['POST'])
def scrape_content_api():
    if request.method == "POST":
        myurl = request.args.get('recipeurl')        
        scraped_content = Scraper(myurl)
        return jsonify(scraped_content)

@app.route('/login_user', methods=['POST'])
def login_user_api():
    if request.method == "POST":
        
        uname = request.args.get('username')
        pasw = request.args.get('password')

        resp = db_cursor.validate(uname, pasw)

        return jsonify(resp)

@app.route('/signup_user', methods=['POST'])
def signup_user_api():
    if request.method == "POST":
        
        uname = request.args.get('username')
        pasw = request.args.get('password')
        
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

@app.route('/search_user_recipe', methods=['POST'])
def search_user_recipes_api():
    if request.method == "POST":
        
        user_email = request.form["user_email"]
        recipe_title = request.form["recipe_title"]
        
        resp = db_cursor.search_user_recipes(user_email, recipe_title)
        
        return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True)