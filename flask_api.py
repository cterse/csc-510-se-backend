from flask import Flask, request, jsonify
from scraper import Scraper
from dbconnector import validate, signon

app = Flask(__name__)
app.config["DEBUG"] = True


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

        val = validate(uname, pasw)

        if val:
            resp = {
                "validate": 1,
                "uname": uname
            }
        else:
            resp = {
                "validate": 0
            }
        return jsonify(resp)

@app.route('/signup_user', methods=['POST'])
def signup_user_api():
    if request.method == "POST":
        
        uname = request.form["username"]
        pasw = request.form["password"]
        
        val = signon(uname, pasw)
                
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
        return jsonify(resp)
    
if __name__ == '__main__':
    app.run(debug=True)