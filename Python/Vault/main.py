from flask import Flask, render_template, request
import mongo_db

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
  return render_template("index.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
  data = {"username": "None", "email": "None", "password": "None"}
  if request.method == "POST":
    username = request.form.get("uname")
    email = request.form.get("email")
    password = request.form.get("password")
    data = {"username": username, "email": email, "password": password}
    result = mongo_db.insert_into(username, email, password)
    if result == "success":
      return render_template("user_data.html")


@app.route("/user", methods=["POST", "GET"])
def userdata():
  if request.method == "POST":
    choice = request.form.get("operation")
    appuser = request.form.get("appuser")
    appname = request.form.get("appname")
    password = request.form.get("password")
    if choice == "add":

      return choice


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8000)
