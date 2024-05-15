from flask import Flask, render_template, request
import requests
import mongo_db

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    new_city = request.form.get('city')
    if new_city:
      url = "http://api.weatherapi.com/v1/current.json?key=c140be0e7ff340e3ba761845231409&q={}&aqi=no".format(
          new_city)

      response = requests.get(url).json()
      print(response)
      data = response['current']
      location = response['location']
      weather = {
          "city": new_city,
          "temp_c": data["temp_c"],
          "temp_f": data["temp_f"],
          "icon": data['condition']['icon'],
          "message": data['condition']['text'],
          "location": location
      }
      mongo_db.insert_entries(weather)
      return render_template('weather.html', weather=weather)
  else:
    data = mongo_db.table.find_one({"city": "Puducherry"})
    weather = {
        "city": data['city'],
        "temp_c": data["temp_c"],
        "temp_f": data["temp_f"],
        "icon": data['icon'],
        "message": data['message']
    }
    return render_template("weather.html", weather=weather)


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8000)
