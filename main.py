from flask import Flask, request, send_file
from chart import generate_chart

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "SYNC Life Balance Chart API is running."

@app.route("/chart", methods=["POST"])
def chart():
    data = request.json
    try:
        # We start reading from column index 5 (i.e., column F in your sheet)
        row_keys = list(data.keys())[5:]
        categories = []
        scores = []

        for key in row_keys:
            # Extract the category name: after the number + ". ", before double space
            try:
                label = key.split(". ", 1)[1].split("  ", 1)[0].strip()
                if label.isupper():
                    categories.append(label)
                    scores.append(float(data[key]))
            except (IndexError, ValueError):
                continue  # Skip malformed columns

        if len(categories) != len(scores):
            return {"error": "Mismatch between categories and scores"}, 400

        path = generate_chart(scores, categories)
        return send_file(path, mimetype='image/png')

    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
