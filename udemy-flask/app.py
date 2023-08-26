from flask import Flask,jsonify,request
from DB import mongo_db
from DB import enc_dec

app = Flask(__name__)


@app.route('/signup')
def signup():
    return '''<form method="POST" action="/validate">
                <input type="text" name="uname" placeholder="username"><br>
                <input type="email" name="email" placeholder="email address"><br>
                <input type="text" name="password" placeholder="*********"><br>
                <input type="submit" value="submit">
            </form>'''

@app.route("/validate",methods=["POST","GET"])
def validate():
    data = {}
    data["name"] = name = request.form["uname"]
    data["email"] = email = request.form["email"]
    data["password"] = password =  request.form["password"]
    result = enc_dec.encrypt(name,email,password)
    return result



if __name__ == "__main__":
    app.run(debug=True)