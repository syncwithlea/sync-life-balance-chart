from flask import Flask, request, send_file
from chart import generate_chart

app = Flask(__name__)

CATEGORIES = [
    "SELF-CARE", "FAMILY", "RELATIONSHIPS",
    "WORK OR PURPOSE", "HEALTH", "CREATIVITY OR PLAY",
    "REST", "PERSONAL GROWTH", "FINANCIAL WELLBEING"
]

@app.route("/", methods=["GET"])
def home():
    return "SYNC Life Balance Chart API is running."

@app.route("/chart", methods=["POST"])
def chart():
    data = request.json
    try:
        scores = [float(data.get(key.lower().replace(" ", "_"), 0)) for key in CATEGORIES]
        path = generate_chart(scores, CATEGORIES)
        return send_file(path, mimetype='image/png')
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
