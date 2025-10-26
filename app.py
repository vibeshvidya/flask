from flask import Flask, render_template, jsonify
import requests
import datetime

app = Flask(__name__)

# A few Kerala district coordinates (for simplicity)
DISTRICTS = {
    "Thiruvananthapuram": {"lat": 8.5241, "lon": 76.9366},
    "Kochi": {"lat": 9.9312, "lon": 76.2673},
    "Kozhikode": {"lat": 11.2588, "lon": 75.7804},
    "Idukki": {"lat": 9.8497, "lon": 77.1025},
}

API_URL = "https://api.open-meteo.com/v1/forecast"


@app.route("/")
def index():
    return render_template("home.html", districts=list(DISTRICTS.keys()))


@app.route("/api/weather")
def get_weather_data():
    data = []
    for name, coords in DISTRICTS.items():
        response = requests.get(
            API_URL,
            params={
                "latitude": coords["lat"],
                "longitude": coords["lon"],
                "hourly": "precipitation",
                "current_weather": True,
            },
        )
        r = response.json()
        rainfall = r.get("hourly", {}).get("precipitation", [0])[-1]
        temp = r.get("current_weather", {}).get("temperature", 0)
        data.append({"district": name, "temperature": temp, "rainfall": rainfall})
    return jsonify(
        {"timestamp": datetime.datetime.now().strftime("%H:%M:%S"), "data": data}
    )


if __name__ == "__main__":
    app.run(debug=True)
