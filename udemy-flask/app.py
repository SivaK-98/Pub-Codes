from flask import Flask,jsonify,request
from DB import mongo_db
from DB import enc_dec

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    return ''' This is a vault application.  
                <form method="POST" action="/login">
                <input type="submit" value="login">
            </form>

            <form method="POST" action="/validate_signup">
                <input type="text" name="uname" placeholder="username"><br>
                <input type="email" name="email" placeholder="email address"><br>
                <input type="text" name="password" placeholder="*********"><br>
                <input type="submit" value="submit">
            </form>
           '''
@app.route('/login',methods=["POST","GET"])
def login():
    return '''<form method="POST" action="/validate_login">
                <input type="email" name="email" placeholder="email address"><br>
                <input type="text" name="password" placeholder="*********"><br>
                <input type="submit" value="login">
            </form>'''

@app.route('/validate_login',methods=["POST","GET"])
def validate_login():
    data = {}
    data["email"] = email = request.form["email"]
    data["password"] = passowrd = request.form["password"]
    result = mongo_db.validate(email,passowrd)
    return result



@app.route("/validate_signup",methods=["POST","GET"])
def validate_signup():
    data = {}
    data["name"] = name = request.form["uname"]
    data["email"] = email = request.form["email"]
    data["password"] = password =  request.form["password"]
    result = enc_dec.encrypt(name,email,password)
    return result



if __name__ == "__main__":
    app.run(debug=True)