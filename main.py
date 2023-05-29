from flask import Flask, render_template, request
import mongodb

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/login/", methods=["POST"])
def login_account():
    if request.method == "POST":
        username = request.form.get("uname")
        print(username)
        password = request.form.get("pword")
        print(password)
        response = mongodb.login(username,password)
        return response


@app.route("/create/", methods=["POST"])
def create_account():
    result = ""
    if request.method == "POST":
        username = request.form.get("uname")
        print(username)
        password = request.form.get("pword")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        result = mongodb.signup(username, password, email, mobile)
    return result


@app.route("/signup/", methods=["POST"])
def signup():
    return render_template("signup.html")


@app.route("/about/<username>")
def about(username):
    return f'About page of {username}'


@app.route("/forward/", methods=["POST"])
def move_forward():
    forward_message = "Moving Forward..."
    return forward_message


if __name__ == "__main__":
    app.run(debug=True)
