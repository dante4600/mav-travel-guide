from flask import Flask

app = Flask(__name__)
stations = [
    {
        "name": "Budapest",
        "county": "Pest",
        "connections": [
            {
                "distance": 150,
                "name": "Szekesfehervar",
                "county": "Fejer"
            }
        ]
    },
    {
        "name": "Szekesfehervar",
        "county": "Fejer",
        "connections": [
            {
                "distance": 150,
                "name": "Budapest",
                "county": "Fejer"
            }
        ]
    }
]


@app.route("/stations", methods=["GET"])
def get_stations():
    return stations


@app.route("/stations/<index>", methods=["GET"])
def get_station(index):
    i = int(index)
    return stations[i]


# main driver function
if __name__ == '__main__':
    app.run(debug=True)
