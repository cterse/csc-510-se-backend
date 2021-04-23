from flask import Flask, request, jsonify
from scraper import Scraper
from dbconnector import dbconnect

app = Flask(__name__)
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
    
if __name__ == '__main__':
    app.run(debug=True)