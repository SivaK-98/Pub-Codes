from flask import Flask, render_template
import subprocess


app = Flask(__name__)

@app.route("/")

def data():
  result = subprocess.run(["python3 main.py"],shell=True,capture_output=True,text=True)
  return render_template("mongo_data.html")

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)